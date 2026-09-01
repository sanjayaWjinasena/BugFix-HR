# -*- coding: utf-8 -*-
from odoo import api, fields, models


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

    # Current-user permission gates (3 computed booleans, store=False).
    # Compute = does env.user match the corresponding M2O role field on
    # this record. Used by view 5550 as readonly gates on the mark-entry
    # and selection fields (so only the assigned approver can edit their
    # section). Studio's original declaration used depends=<self> as a
    # placeholder; real depends is on the M2O + env.user (per-session).
    x_studio_cu_line_manager = fields.Boolean(
        string='CU - Line Manager', store=False,
        compute='_compute_cu_line_manager')
    x_studio_cu_leadership = fields.Boolean(
        string='CU - Leadership', store=False,
        compute='_compute_cu_leadership')
    x_studio_cu_recruiter = fields.Boolean(
        string='CU - Recruiter', store=False,
        compute='_compute_cu_recruiter')

    @api.depends('x_studio_line_manager_name')
    def _compute_cu_line_manager(self):
        me = self.env.user
        for rec in self:
            rec.x_studio_cu_line_manager = (rec.x_studio_line_manager_name == me)

    @api.depends('x_studio_leadership_name')
    def _compute_cu_leadership(self):
        me = self.env.user
        for rec in self:
            rec.x_studio_cu_leadership = (rec.x_studio_leadership_name == me)

    @api.depends('x_studio_recruiter')
    def _compute_cu_recruiter(self):
        me = self.env.user
        for rec in self:
            rec.x_studio_cu_recruiter = (rec.x_studio_recruiter == me)
