from odoo import fields, models


class X_paye_tax_tag(models.Model):
    _name = "x_paye_tax_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Paye Tax Tags"

    color = fields.Integer(string="Color")
    name = fields.Char(string="Name", required=True)


class XPayeTaxTagGap(models.Model):
    _inherit = "x_paye_tax_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    color = fields.Integer(string="Color")
    name = fields.Char(string="Name", required=True)
