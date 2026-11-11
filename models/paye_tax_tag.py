from odoo import fields, models


class X_paye_tax_tag(models.Model):
    _name = "paye_tax_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Paye Tax Tags"

    color = fields.Integer()
    name = fields.Char(required=True)


class XPayeTaxTagGap(models.Model):
    _inherit = "paye_tax_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    color = fields.Integer()
    name = fields.Char(required=True)
