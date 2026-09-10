# -*- coding: utf-8 -*-
from odoo import models, fields

class XUpdateOtLine7eea7Gap(models.Model):
    _inherit = 'x_update_ot_line_7eea7'

    x_name = fields.Char(string='Description', required=True)
    x_update_ot_id = fields.Many2one(comodel_name='x_update_ot', string='X Update Ot')
