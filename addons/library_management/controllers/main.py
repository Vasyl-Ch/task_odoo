from odoo import http
from odoo.http import request
import json  # Імпортуємо модуль для роботи з JSON форматом


class LibraryController(http.Controller):
    # Контролер для обробки HTTP-запитів до бібліотеки

    @http.route(
        "/library/books",  # URL-шлях для доступу до списку книг
        auth="public",     # Доступ без автентифікації
        methods=["GET"],    # Тільки GET-запити
        type="http"        # Тип HTTP-маршруту
    )
    def get_books(self) -> http.Response:
        """
        Повертає JSON-список всіх книг з їх статусом.
        """
        # Отримуємо всі книги з бази даних (sudo() для обходу прав доступу)
        books = request.env["library.book"].sudo().search([])
        # Формуємо список книг у форматі JSON
        data = [
            {
                "id": book.id,  # Унікальний ідентифікатор книги
                "name": book.name,  # Назва книги
                "author": book.author,  # Автор книги
                "published_date": str(
                    book.published_date
                ) if book.published_date else None,  # Дата публікації (перетворена в рядок)
                "is_available": book.is_available,  # Статус доступності
            }
            for book in books
        ]
        # Формуємо HTTP-відповідь з JSON-даними
        return request.make_response(
            json.dumps(data),  # Перетворюємо список в JSON-рядок
            headers=[("Content-Type", "application/json")]  # Встановлюємо заголовок Content-Type
        )
