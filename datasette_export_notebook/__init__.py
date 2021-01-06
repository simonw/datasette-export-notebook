from datasette import hookimpl
from datasette.utils.asgi import Response
from datasette.utils import path_with_format
import json


async def render_notebook(datasette, request):
    return Response.html(
        await datasette.render_template(
            "export_notebook.html",
            {
                "csv_stream_url": datasette.absolute_url(
                    request,
                    path_with_format(
                        request=request, format="csv", extra_qs={"_stream": "on"}
                    ),
                ),
                "json_url": datasette.absolute_url(
                    request,
                    path_with_format(
                        request=request, format="json", extra_qs={"_shape": "array"}
                    ),
                ),
                "json": json,
            },
        )
    )


@hookimpl
def register_output_renderer(datasette):
    return {
        "extension": "Notebook",
        "render": render_notebook,
    }
