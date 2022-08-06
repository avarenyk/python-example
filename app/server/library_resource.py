import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler

from app.library.library import Library, Book


class LibraryResource:
    _library: Library = None

    def __init__(self, library: Library):
        self._library = library

    def add_book(self, req: BaseHTTPRequestHandler):
        self._library.add_book(Book("Harry Potter", "Fantasy", "J.K. Rowling"))

        req.send_response(HTTPStatus.OK)
        req.send_header("Content-type", "application/json")
        req.end_headers()
        req.wfile.write(
            json.dumps({'server_name': 'Simple HTTP server', 'author': 'Andrey Varenyk', 'path': req.path,
                        'method': req.command, 'library books': self._library.books.__str__()}).encode())

    def send_email(self, req: BaseHTTPRequestHandler):
        print("getting message from body...")
        length = int(req.headers.get('content-length'))
        message = (req.rfile.read(length)).decode()
        print("I am sending email to andrey.varenyk@gmail.com with message " + message)
        req.send_response(HTTPStatus.OK)
        req.send_header("Content-type", "application/json")
        req.end_headers()
        req.wfile.write(
            json.dumps({'email': 'andrey.varenyk@gmail.com', 'message': message}).encode())
