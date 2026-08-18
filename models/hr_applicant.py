# -*- coding: utf-8 -*-
from odoo import fields, models


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    x_studio_2nd_selection = fields.Selection([], string='Leadership Selection')
    x_studio_appreciation = fields.Selection([], string='Application')
    x_studio_cu_leadership = fields.Boolean(string='CU - Leadership', readonly=True, store=False)
    x_studio_cu_line_manager = fields.Boolean(string='CU - Line Manager', readonly=True, store=False)
    x_studio_cu_recruiter = fields.Boolean(string='CU - Recruiter', readonly=True, store=False)
    x_studio_hr_responsible = fields.Many2one('hr.employee', string='HR Responsible')
    x_studio_interview_marks_1 = fields.Integer(string='Line Manager Marks %')
    x_studio_interview_marks_2 = fields.Integer(string='Leadership Marks %')
    x_studio_interview_marks_3 = fields.Integer(string='Recruiter Marks %')
    x_studio_leadership_name = fields.Many2one('res.users', string='Leadership Name', readonly=True)
    x_studio_line_manager_name = fields.Many2one('res.users', string='Line Manager Name', readonly=True)
    x_studio_marks_1 = fields.Integer(string='Recruiter Assignment Marks %')
    x_studio_priority = fields.Selection([], string='Line Manager Selection')
    x_studio_recruiter = fields.Many2one('res.users', string='Recruiter', readonly=True)
    x_studio_total_marks = fields.Float(string='Total Marks', readonly=True)
