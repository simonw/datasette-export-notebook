from datasette import hookimpl
from datasette.utils.asgi import Response
from .utils import detect_types
import json


async def render_notebook(datasette, request, data, rows):
    original_path = request.path.replace(".Notebook", "")
    back_url = original_path
    json_url = original_path + ".json"
    if request.query_string:
        back_url += "?" + request.query_string
        json_url += "?" + request.query_string + "&_shape=array"
    else:
        json_url += "?_shape=array"
    json_url = datasette.absolute_url(
        request,
        json_url,
    )
    total_count = None
    count = len(rows)
    if "filtered_table_rows_count" in data:
        total_count = data["filtered_table_rows_count"]

    csv_stream_url = None
    if data.get("next"):
        csv_path = original_path + ".csv"
        if request.query_string:
            csv_path += "?" + request.query_string + "&_stream=on"
        else:
            csv_path += "?_stream=on"
        csv_stream_url = datasette.absolute_url(request, csv_path)

    return Response.html(
        await datasette.render_template(
            "export_notebook.html",
            {
                "cors_enabled": datasette.cors,
                "allow_csv_stream": datasette.setting("allow_csv_stream"),
                "back_url": back_url,
                "csv_stream_url": csv_stream_url,
                "pandas_stream_code": pandas_stream_code(
                    csv_stream_url, detect_types(rows)
                ),
                "json_url": json_url,
                "count": count,
                "total_count": total_count,
                "has_next": bool(data.get("next")),
                "json": json,
            },
        )
    )


def pandas_stream_code(csv_stream_url, column_types):
    dtype = ""
    non_string_types = {
        col: type for col, type in column_types.items() if type != "str"
    }
    if non_string_types:
        lines = [", dtype={"]
        for column, type in non_string_types.items():
            lines.append("    {}: {},".format(json.dumps(column), type))
        lines.append("}")
        dtype = "\n".join(lines)
    return "df = pandas.read_csv(\n    {}{})".format(json.dumps(csv_stream_url), dtype)


@hookimpl
def register_output_renderer(datasette):
    return {
        "extension": "Notebook",
        "render": render_notebook,
    }
