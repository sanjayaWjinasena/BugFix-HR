# -*- coding: utf-8 -*-
from odoo import models, fields

class XPayeTaxTagGap(models.Model):
    _inherit = 'x_paye_tax_tag'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Name', required=True)
