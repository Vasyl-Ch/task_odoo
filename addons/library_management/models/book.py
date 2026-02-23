from odoo import models, fields


class LibraryBook(models.Model):
    """
   # Book model for library.
    """
    _name = "library.book"
    _description = "Library Book"

    name = fields.Char(
        string="Book Title",
        required=True
    )
    author = fields.Char(
        string="Author"
    )
    published_date = fields.Date(
        string="Published Date"
    )
    is_available = fields.Boolean(
        string="Available",
        default=True
    )
