from odoo import models, fields


class LibraryRentWizard(models.TransientModel):
    """
    Book Issuance Wizard — Allows you to select
    reader and creates a lease record.
    """
    _name = "library.rent.wizard"
    _description = "Rent Book Wizard"

    partner_id = fields.Many2one(
        "res.partner",
        required=True,
        string="Reader"
    )
    book_id = fields.Many2one(
        "library.book",
        string="Book"
    )

    def action_confirm(self):
        """Creates a lease record and marks the book as unavailable."""
        self.env["library.rent"].create([{
            "partner_id": self.partner_id.id,
            "book_id": self.book_id.id,
        }])
        self.book_id.is_available = False
        return {"type": "ir.actions.act_window_close"}
