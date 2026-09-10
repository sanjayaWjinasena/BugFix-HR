# -*- coding: utf-8 -*-
from odoo import models, fields

class XUpdateOtGap(models.Model):
    _inherit = 'x_update_ot'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_update_ot_line_ids_d5449 = fields.One2many(comodel_name='x_update_ot_line_7eea7', inverse_name='x_update_ot_id', string='New Lines')
