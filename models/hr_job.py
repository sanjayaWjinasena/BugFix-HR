from odoo import fields, models


class HrJob(models.Model):
    _inherit = "hr.job"

    leadership_name = fields.Many2one("res.users")
    line_manager_name = fields.Many2one("res.users")
    link = fields.Html()
    test_document = fields.Binary()
    test_document_filename = fields.Char(
        string="Filename for x_studio_binary_field_K4eWr"
    )
