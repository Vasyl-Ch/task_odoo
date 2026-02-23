from odoo import models, fields, api
from odoo.exceptions import ValidationError  # Імпортуємо клас для валідації помилок


class LibraryRent(models.Model):
    """
    Модель оренди: книга видається партнеру.
    """
    _name = "library.rent"
    _description = "Library Rent"

    # Посилання на партнера (читача)
    partner_id = fields.Many2one(
        "res.partner",
        string="Customer",
        required=True  # Обов'язкове поле - кожна оренда повинна мати читача
    )
    # Посилання на книгу
    book_id = fields.Many2one(
        "library.book",
        string="Book",
        required=True  # Обов'язкове поле - кожна оренда повинна мати книгу
    )
    # Дата видачі книги
    rent_date = fields.Date(
        default=fields.Date.today,  # Автоматично встановлюємо поточну дату
        readonly=True  # Поле тільки для читання
    )
    # Дата повернення книги (порожня, якщо книга не повернена)
    return_date = fields.Date()

    # Обмеження для перевірки доступності книги
    @api.constrains("book_id", "return_date")  # Декоратор викликає метод при зміні полів
    def _check_book_availability(self) -> None:
        """
        Запобігає подвійній оренді тієї ж книги,
        якщо вона не була повернена.
        """
        for rent in self:  # Перебираємо всі записи оренди
            # Перевіряємо, чи книга вказана і чи не повернена
            if rent.book_id and not rent.return_date:
                # Шукаємо активні оренди тієї ж книги
                active_rents = self.search(
                    [
                        ("book_id", "=", rent.book_id.id),  # Та сама книга
                        ("return_date", "=", False)  # Не повернена
                    ]
                )
                # Якщо знайдено більше 1 активної оренди - помилка
                if len(active_rents) > 1:
                    raise ValidationError(
                        "Книга вже видана і не повернена!"
                    )

    def action_return_book(self) -> None:
        """
        Фіксує повернення книги:
        встановлює дату повернення та робить книгу доступною.
        """
        self.return_date = fields.Date.today()  # Встановлюємо поточну дату повернення
        self.book_id.is_available = True  # Робимо книгу знову доступною для видачі
