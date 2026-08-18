# -*- coding: utf-8 -*-
from odoo import fields, models


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    x_studio_check_in_auto = fields.Boolean(string='Check In Auto')
    x_studio_check_out_auto = fields.Boolean(string='Check Out Auto')
    x_studio_company_id = fields.Many2one('res.company', string='Company', readonly=True)
    x_studio_ot_approved = fields.Boolean(string='OT Approved')
    x_studio_ot_approved_by = fields.Many2one('res.users', string='OT Approved By')
    x_studio_ot_entry = fields.Boolean(string='OT Entry')
    x_studio_over_time = fields.Float(string='Over Time', readonly=True, store=False)
