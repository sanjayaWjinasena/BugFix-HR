# -*- coding: utf-8 -*-
from odoo import models, fields

class XPayeTaxGap(models.Model):
    _inherit = 'x_paye_tax'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Code')
