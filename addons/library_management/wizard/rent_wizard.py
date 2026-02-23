from odoo import models, fields


class LibraryRentWizard(models.TransientModel):
    """
    Майстер видачі книг — дозволяє вибрати читача
    та створити запис про оренду.
    """
    _name = "library.rent.wizard"
    _description = "Rent Book Wizard"

    # Поле для вибору читача (партнера)
    partner_id = fields.Many2one(
        "res.partner",
        required=True,  # Обов'язкове поле для вибору читача
        string="Reader"
    )
    # Поле для вибору книги, яку видаємо
    book_id = fields.Many2one(
        "library.book",
        string="Book"
    )

    def action_confirm(self) -> dict:
        """Створює запис оренди та позначає книгу як недоступну."""
        # Створюємо новий запис про оренду книги
        self.env["library.rent"].create([{
            "partner_id": self.partner_id.id,  # ID читача
            "book_id": self.book_id.id,        # ID книги
        }])
        # Позначаємо книгу як недоступну для видачі
        self.book_id.is_available = False
        # Закриваємо вікно майстра після підтвердження
        return {"type": "ir.actions.act_window_close"}
