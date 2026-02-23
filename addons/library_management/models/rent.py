from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryRent(models.Model):
    """
    Rent model: book is given to a partner.
    """
    _name = "library.rent"
    _description = "Library Rent"

    partner_id = fields.Many2one(
        "res.partner",
        string="Customer",
        required=True
    )
    book_id = fields.Many2one(
        "library.book",
        string="Book",
        required=True
    )
    rent_date = fields.Date(
        default=fields.Date.today,
        readonly=True
    )
    return_date = fields.Date()

    # Constraint для перевірки Якщо книга не повернена
    @api.constrains("book_id", "return_date")
    def _check_book_availability(self) -> None:
        """
        Prevents renting the same book twice
        if it was not returned.
        """
        for rent in self:
            if rent.book_id and not rent.return_date:
                active_rents = self.search(
                    [
                        ("book_id", "=", rent.book_id.id),
                        ("return_date", "=", False)
                    ]
                )
                if len(active_rents) > 1:
                    raise ValidationError(
                        "Книга вже видана і не повернена!"
                    )

    def action_return_book(self) -> None:
        """
        Captures the return of the book:
        sets the date and makes the book available.
        """
        self.return_date = fields.Date.today()
        self.book_id.is_available = True
