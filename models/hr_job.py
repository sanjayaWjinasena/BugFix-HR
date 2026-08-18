# -*- coding: utf-8 -*-
from odoo import fields, models


class HrJob(models.Model):
    _inherit = 'hr.job'

    x_studio_leadership_name = fields.Many2one('res.users', string='Leadership Name')
    x_studio_line_manager_name = fields.Many2one('res.users', string='Line Manager Name')
    x_studio_link = fields.Html(string='Link')
    x_studio_test_document = fields.Binary(string='Test Document')
    x_studio_test_document_filename = fields.Char(string='Filename for x_studio_binary_field_K4eWr')
