"""
A simple web application to act as incoming interface

This is a proof of concept.  In practice, this web interface
could be as involved as necessary.
"""

from fastapi import FastAPI
import fastapi
import uvicorn

from multiprocessing import Process

def build_app(*args, **kwargs):
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "hello from an interface webapp"}

    return app


def serve_app(
    app: fastapi.FastAPI, 
    host: str = '127.0.0.1', 
    port: int = 8080,
    log_level: str = 'debug'
    ):
    def start_server():
        uvicorn.run(app, host=host, port=port, log_level=log_level)
    
    server_process = Process(target=start_server)
    server_process.start()

    # We pass the process back so the interface can terminate.
    return server_process