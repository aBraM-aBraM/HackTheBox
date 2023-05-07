from flask import Flask, render_template
import click
import consts
import urllib.parse
import json
from flask import request
from pathlib import Path
import uuid

app = Flask(__name__)
g_output_dir = consts.CURRENT_DIR / "output"


@app.route("/")
def default_route():
    args = request.args.to_dict()
    content = args.get("content")
    if content:
        with open(f"{g_output_dir / str(uuid.uuid4())}.html", "w") as html_file_object:
            html_file_object.write(content)
    print(json.dumps(request.args.to_dict()))
    return "bruh"


@app.route("/test")
def test_route():
    return "test"


@click.command()
@click.argument("host", type=str, default="0.0.0.0")
@click.argument("port", type=int, default=consts.PORT)
@click.argument("output_dir", type=click.types.Path(file_okay=False), default=g_output_dir)
def main(host: str, port: int, output_dir: Path):
    """Opens a server that saves requests (use with xss.py)"""
    global g_output_dir
    g_output_dir = output_dir
    if not g_output_dir.exists():
        g_output_dir.mkdir()
    app.run(host=host, port=port)


if __name__ == '__main__':
    main()
