# -*- coding: utf-8 -*-
from odoo import models, fields

class X_paye_tax(models.Model):
    _name = 'x_paye_tax'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Paye Tax'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Code')
    x_studio_end_date = fields.Date(string='End Date')
    x_studio_from_value = fields.Float(string='From Value')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_start_date = fields.Date(string='Start Date')
    x_studio_tag_ids = fields.Many2many(comodel_name='x_paye_tax_tag', string='Tags')
    x_studio_tax_amount = fields.Float(string='Tax Amount')
    x_studio_to_value = fields.Float(string='To Value')
    x_studio_user_id = fields.Many2one(comodel_name='res.users', string='Responsible')
