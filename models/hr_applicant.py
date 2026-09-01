# -*- coding: utf-8 -*-
from odoo import fields, models


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    # Recruitment workflow selections
    x_studio_priority = fields.Selection(
        [('Yes', 'Yes'), ('May Be', 'May Be'), ('No', 'No')],
        string='Line Manager Selection', copy=True)
    x_studio_2nd_selection = fields.Selection(
        [('Yes', 'Yes'), ('No', 'No')],
        string='Leadership Selection', copy=True)
    x_studio_appreciation = fields.Selection(
        [('Normal', 'Normal'), ('Low', 'Low'), ('High', 'High'), ('Very High', 'Very High')],
        string='Application', copy=True)

    # Interview scoring (integer percentages)
    x_studio_marks_1 = fields.Integer(string='Recruiter Assignment Marks %', copy=True)
    x_studio_interview_marks_1 = fields.Integer(string='Line Manager Marks %', copy=True)
    x_studio_interview_marks_2 = fields.Integer(string='Leadership Marks %', copy=True)
    x_studio_interview_marks_3 = fields.Integer(string='Recruiter Marks %', copy=True)
    # Total Marks: Studio declared as store=True with depends on the 4 marks
    # fields above, but no visible compute method. Declared as plain stored
    # Float here (manual entry / external-automation-populated). If a real
    # compute formula surfaces later, add compute='_compute_total_marks'.
    x_studio_total_marks = fields.Float(string='Total Marks')

    # Approver roles (M2O to res.users / hr.employee)
    x_studio_recruiter = fields.Many2one('res.users', string='Recruiter', ondelete='set null')
    x_studio_line_manager_name = fields.Many2one('res.users', string='Line Manager Name', ondelete='set null')
    x_studio_leadership_name = fields.Many2one('res.users', string='Leadership Name', ondelete='set null')
    x_studio_hr_responsible = fields.Many2one('hr.employee', string='HR Responsible', ondelete='set null', copy=True)

    # DEFERRED (see manifest v0.0.15 changelog):
    #   * x_studio_cu_leadership   Boolean (current-user leadership check)
    #   * x_studio_cu_line_manager Boolean (current-user line manager check)
    #   * x_studio_cu_recruiter    Boolean (current-user recruiter check)
    # Studio pattern: store=False + depends=<self>. Real semantics = "does
    # current user match one of the M2O role fields above". Need to write
    # a proper compute method that checks env.user against these fields.
    # View 5550 blocked on these (uses readonly="x_studio_cu_line_manager
    # == False" gating). Port in a follow-up version.
