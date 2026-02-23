from odoo import models, fields


class LibraryBook(models.Model):
    """
    Модель книги для бібліотеки.
    """
    _name = "library.book"
    _description = "Library Book"

    # Назва книги - обов'язкове поле
    name = fields.Char(
        string="Book Title",
        required=True  # Кожна книга повинна мати назву
    )
    # Автор книги
    author = fields.Char(
        string="Author"
    )
    # Дата публікації книги
    published_date = fields.Date(
        string="Published Date"
    )
    # Статус доступності книги для видачі
    is_available = fields.Boolean(
        string="Available",
        default=True  # За замовчуванням книга доступна
    )

    def action_open_rent_wizard(self) -> dict:
        """
        Відкриває майстер оренди для поточної книги.
        """
        return {
            "type": "ir.actions.act_window",  # Тип дії - відкриття вікна
            "res_model": "library.rent.wizard",  # Модель майстра оренди
            "view_mode": "form",  # Режим відображення - форма
            "target": "new",  # Відкрити в новому вікні (модальне)
            "context": {"default_book_id": self.id},  # Передаємо ID книги як значення за замовчуванням
        }
