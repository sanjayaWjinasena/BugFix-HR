from odoo import fields, models


class X_update_ot(models.Model):
    _name = "update_ot"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Update OT"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    as_on_date = fields.Date(string="As on Date")
    accounting_company_id = fields.Many2one(
        comodel_name="res.company", string="Company"
    )
    sequence = fields.Integer(string="Sequence")
    update_ot_line_ids_d5449 = fields.One2many(
        comodel_name="update_ot_line_7eea7",
        inverse_name="update_ot_id",
        string="New Lines",
    )


class XUpdateOtGap(models.Model):
    _inherit = "update_ot"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    update_ot_line_ids_d5449 = fields.One2many(
        comodel_name="update_ot_line_7eea7",
        inverse_name="update_ot_id",
        string="New Lines",
    )
