from contextlib import contextmanager
from flask import Flask
import functools
from multiprocessing import Process
import os.path
import time


@contextmanager
def server(port, use_ssl=False):

    app = Flask('abc')

    @app.route('/')
    def route():
        return 'abc'

    def run():
        app.run(
            port=port,
            ssl_context=ssl_context() if use_ssl else None,
        )

    s = Process(target=run)
    s.start()
    try:
        time.sleep(0.5)
        yield
    finally:
        s.terminate()
        s.join()


def ssl_context():
    return (file('cert.pem'), file('key.pem'))


def file(name):
    return os.path.join(os.path.dirname(__file__), name)


def with_server(*args, **kwargs):
    def decorate(f):
        @functools.wraps(f)
        def wrapped(*wrapped_args, **wrapped_kwargs):
            with server(*args, **kwargs):
                return f(*wrapped_args, **wrapped_kwargs)
        return wrapped
    return decorate
