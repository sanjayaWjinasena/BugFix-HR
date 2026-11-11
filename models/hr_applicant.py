from odoo import api, fields, models


class HrApplicant(models.Model):
    _inherit = "hr.applicant"

    # Recruitment workflow selections
    custom_reports_priority = fields.Selection(
        [("Yes", "Yes"), ("May Be", "May Be"), ("No", "No")],
        string="Line Manager Selection",
        copy=True,
    )
    hr_2nd_selection = fields.Selection(
        [("Yes", "Yes"), ("No", "No")], string="Leadership Selection", copy=True
    )
    appreciation = fields.Selection(
        [
            ("Normal", "Normal"),
            ("Low", "Low"),
            ("High", "High"),
            ("Very High", "Very High"),
        ],
        string="Application",
        copy=True,
    )

    # Interview scoring (integer percentages)
    marks_1 = fields.Integer(string="Recruiter Assignment Marks %", copy=True)
    interview_marks_1 = fields.Integer(string="Line Manager Marks %", copy=True)
    interview_marks_2 = fields.Integer(string="Leadership Marks %", copy=True)
    interview_marks_3 = fields.Integer(string="Recruiter Marks %", copy=True)
    # Total Marks: real compute as simple sum of the 4 mark percentages
    # (matches Studio's depends declaration). View 5550 displays this
    # with widget='progressbar' so max useful value is 400 (4 * 100%).
    # If a weighted formula surfaces later, adjust _compute_total_marks.
    total_marks = fields.Float(store=True, compute="_compute_total_marks")

    # Approver roles (M2O to res.users / hr.employee)
    recruiter = fields.Many2one("res.users", ondelete="set null")
    line_manager_name = fields.Many2one("res.users", ondelete="set null")
    leadership_name = fields.Many2one("res.users", ondelete="set null")
    hr_responsible = fields.Many2one(
        "hr.employee", string="HR Responsible", ondelete="set null", copy=True
    )

    # Current-user permission gates (3 computed booleans, store=False).
    # Compute = does env.user match the corresponding M2O role field on
    # this record. Used by view 5550 as readonly gates on the mark-entry
    # and selection fields (so only the assigned approver can edit their
    # section). Studio's original declaration used depends=<self> as a
    # placeholder; real depends is on the M2O + env.user (per-session).
    cu_line_manager = fields.Boolean(
        string="CU - Line Manager", store=False, compute="_compute_cu_line_manager"
    )
    cu_leadership = fields.Boolean(
        string="CU - Leadership", store=False, compute="_compute_cu_leadership"
    )
    cu_recruiter = fields.Boolean(
        string="CU - Recruiter", store=False, compute="_compute_cu_recruiter"
    )

    @api.depends("line_manager_name")
    def _compute_cu_line_manager(self):
        me = self.env.user
        for rec in self:
            rec.cu_line_manager = rec.line_manager_name == me

    @api.depends("leadership_name")
    def _compute_cu_leadership(self):
        me = self.env.user
        for rec in self:
            rec.cu_leadership = rec.leadership_name == me

    @api.depends("recruiter")
    def _compute_cu_recruiter(self):
        me = self.env.user
        for rec in self:
            rec.cu_recruiter = rec.recruiter == me

    @api.depends(
        "marks_1",
        "interview_marks_1",
        "interview_marks_2",
        "interview_marks_3",
    )
    def _compute_total_marks(self):
        for rec in self:
            rec.total_marks = float(
                (rec.marks_1 or 0)
                + (rec.interview_marks_1 or 0)
                + (rec.interview_marks_2 or 0)
                + (rec.interview_marks_3 or 0)
            )
