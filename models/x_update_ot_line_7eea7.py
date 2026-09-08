# -*- coding: utf-8 -*-
from odoo import models, fields

class X_update_ot_line_7eea7(models.Model):
    _name = 'x_update_ot_line_7eea7'
    _description = 'Update Ot  Lines'

    x_name = fields.Char(string='Description', required=True)
    x_studio_approve_ot = fields.Boolean(string='Approve OT')
    x_studio_attendance_id = fields.Many2one(comodel_name='hr.attendance', string='Attendance Id')
    x_studio_check_in = fields.Datetime(string='Check In')
    x_studio_check_out = fields.Datetime(string='Check Out')
    x_studio_employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee ID')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_update_ot_id = fields.Many2one(comodel_name='x_update_ot', string='X Update Ot')
