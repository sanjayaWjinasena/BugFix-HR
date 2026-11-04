from odoo import fields, models


class X_paye_tax(models.Model):
    _name = "x_paye_tax"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Paye Tax"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Code")
    x_studio_end_date = fields.Date(string="End Date")
    x_studio_from_value = fields.Float(string="From Value")
    sequence = fields.Integer(string="Sequence")
    x_studio_start_date = fields.Date(string="Start Date")
    x_studio_tag_ids = fields.Many2many(comodel_name="x_paye_tax_tag", string="Tags")
    x_studio_tax_amount = fields.Float(string="Tax Amount")
    x_studio_to_value = fields.Float(string="To Value")
    x_studio_user_id = fields.Many2one(comodel_name="res.users", string="Responsible")


class XPayeTaxGap(models.Model):
    _inherit = "x_paye_tax"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Code")
