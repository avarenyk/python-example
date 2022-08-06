from app.server.library_resource import LibraryResource
from typing import Callable
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
import json


def get_routes(library_resource: LibraryResource) -> [dict]:
    routes = [
        {
            'method': 'GET',
            'path': '/v1/library/books',
            'call': handler_func('get books')
        },
        {
            'method': 'GET',
            'path': '/v1/library/books/history',
            'call': handler_func('get history book')
        },
        {
            'method': 'POST',
            'path': '/v1/library/books',
            'call': library_resource.add_book
        },
        {
            'method': 'GET',
            'path': '/v1/library/contact',
            'call': handler_func('get library contacts')
        },
        {
            'method': 'POST',
            'path': '/v1/library/send_email',
            'call': library_resource.send_email
        },
    ]

    return routes


def handler_func(name: str) -> Callable:
    def handler(req: BaseHTTPRequestHandler) -> None:
        req.send_response(HTTPStatus.OK)
        req.send_header("Content-type", "application/json")
        req.end_headers()
        req.wfile.write(
            json.dumps({'server_name': 'Simple HTTP server', 'author': 'Andrey Varenyk', 'path': req.path,
                        'method': req.command, 'func': name}).encode())

    return handler
