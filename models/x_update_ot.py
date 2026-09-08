# -*- coding: utf-8 -*-
from odoo import models, fields

class X_update_ot(models.Model):
    _name = 'x_update_ot'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Update OT'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_as_on_date = fields.Date(string='As on Date')
    x_studio_company_id = fields.Many2one(comodel_name='res.company', string='Company')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_update_ot_line_ids_d5449 = fields.One2many(comodel_name='x_update_ot_line_7eea7', inverse_name='x_update_ot_id', string='New Lines')
