from odoo import fields, models


class HrJob(models.Model):
    _inherit = "hr.job"

    leadership_name = fields.Many2one("res.users", string="Leadership Name")
    line_manager_name = fields.Many2one(
        "res.users", string="Line Manager Name"
    )
    link = fields.Html(string="Link")
    test_document = fields.Binary(string="Test Document")
    test_document_filename = fields.Char(
        string="Filename for x_studio_binary_field_K4eWr"
    )
