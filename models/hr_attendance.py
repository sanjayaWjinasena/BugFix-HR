# -*- coding: utf-8 -*-
from odoo import fields, models


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    x_studio_check_in_auto = fields.Boolean(string='Check In Auto', copy=True)
    x_studio_check_out_auto = fields.Boolean(string='Check Out Auto', copy=True)
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_ot_approved = fields.Boolean(string='OT Approved', copy=True)
    x_studio_ot_approved_by = fields.Many2one('res.users', string='OT Approved By', copy=True)
    x_studio_ot_entry = fields.Boolean(string='OT Entry', copy=True)
    x_studio_over_time = fields.Float(string='Over Time', store=False, readonly=True)
