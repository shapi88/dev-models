"""Basic smoke test for the skeleton."""
import pytest

from myapp.main import create_app


def test_app_is_callable():
    app = create_app()
    assert callable(app)


def test_placeholder_response():
    app = create_app()
    # Very naive WSGI call just to prove the skeleton runs
    environ = {"REQUEST_METHOD": "GET"}
    captured = {}

    def start_response(status, headers):
        captured["status"] = status
        captured["headers"] = headers

    result = app(environ, start_response)
    assert captured["status"] == "200 OK"
    assert b"Hello from the dev-models" in b"".join(result)