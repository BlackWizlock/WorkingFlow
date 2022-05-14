from flask import Flask, json

app = Flask(__name__)


@app.route(
    "/",
)
def page_index():
    return " "


@app.route(
    "/to_kbytes/<int:kbytes>/",
)
def page_kbytes(kbytes):
    return str(kbytes * 1024)


@app.route(
    "/to_bytes/<int:bytes>/",
)
def page_bytes(bytes):
    return str(bytes * 1024)


if __name__ == "__main__":
    app.run(debug=True)
