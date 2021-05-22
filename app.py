import flask


app = flask.Flask(__name__)


@app.template_global()
def identity(arg: str) -> str:
    return arg
