# -*- coding: utf-8 -*-
from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    x_studio_employee_rate = fields.Float(string='Employee Rate')
    x_studio_epf_no = fields.Char(string='EPF No')
    x_studio_etf_no = fields.Char(string='ETF No')
    x_studio_occupation_code = fields.Char(string='Occupation Code')
    x_studio_ot_hours = fields.Float(string='OT Hours', readonly=True, store=False)
    x_studio_ot_hours_month_display = fields.Char(string='New Text')
    x_studio_ot_month = fields.Float(string='OT Hours (month)', readonly=True)
    x_studio_ot_month_display = fields.Char(string='OT Hours (month) Display', readonly=True, store=False)
    x_studio_ot_rate = fields.Float(string='OT Rate')
    x_studio_purpose_code = fields.Char(string='Purpose Code')
