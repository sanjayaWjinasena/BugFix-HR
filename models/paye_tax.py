from odoo import fields, models


class X_paye_tax(models.Model):
    _name = "paye_tax"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Paye Tax"

    active = fields.Boolean()
    name = fields.Char(string="Code")
    end_date = fields.Date()
    from_value = fields.Float()
    sequence = fields.Integer()
    start_date = fields.Date()
    tag_ids = fields.Many2many(
        comodel_name="paye_tax_tag",
        relation="x_paye_tax_x_paye_tax_tag_rel",
        column1="x_paye_tax_id",
        column2="x_paye_tax_tag_id",
        string="Tags",
    )
    tax_amount = fields.Float()
    to_value = fields.Float()
    user_id = fields.Many2one(comodel_name="res.users", string="Responsible")


class XPayeTaxGap(models.Model):
    _inherit = "paye_tax"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char(string="Code")
