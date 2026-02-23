from odoo import http
from odoo.http import request
import json


class LibraryController(http.Controller):

    @http.route(
        "/library/books",
        auth="public",
        methods=["GET"],
        type="http"
    )
    def get_books(self) -> http.Response:
        """
        Returns a JSON list of all workbooks with their status.
        """
        books = request.env["library.book"].sudo().search([])
        data = [
            {
                "id": book.id,
                "name": book.name,
                "author": book.author,
                "published_date": str(
                    book.published_date
                ) if book.published_date else None,
                "is_available": book.is_available,
            }
            for book in books
        ]
        return request.make_response(
            json.dumps(data),
            headers=[("Content-Type", "application/json")]
        )
