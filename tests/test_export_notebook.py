from datasette.app import Datasette
import pytest
import sqlite_utils


@pytest.fixture
def db_path(tmpdir):
    db_path = str(tmpdir / "db.db")
    db = sqlite_utils.Database(db_path)
    db["blah"].insert_all({"id": i} for i in range(80))
    db["big"].insert_all({"id": i} for i in range(800))
    return db_path


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "path,expected_json_url,expected_csv_url",
    [
        ("/db/blah.Notebook", "http://localhost/db/blah.json?_shape=array", ""),
        (
            "/db/big.Notebook",
            "http://localhost/db/big.json?_shape=array",
            "http://localhost/db/big.csv?_stream=on",
        ),
    ],
)
async def test_export_notebook(
    db_path,
    path,
    expected_json_url,
    expected_csv_url,
):
    datasette = Datasette([db_path])
    response = await datasette.client.get(path)
    assert 200 == response.status_code
    assert (
        "df = pandas.read_json(&#34;{}&#34;)".format(expected_json_url) in response.text
    )
    assert "rows = d3.json(&#34;{}&#34;)".format(expected_json_url) in response.text
    if not expected_csv_url:
        assert ".csv" not in response.text
    else:
        assert (
            "df = pandas.read_csv(&#34;{}&#34;)".format(expected_csv_url)
            in response.text
        )
        assert "rows = d3.csv(&#34;{}&#34;)".format(expected_csv_url) in response.text
