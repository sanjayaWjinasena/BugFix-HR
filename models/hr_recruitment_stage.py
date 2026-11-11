from odoo import fields, models


class HrRecruitmentStage(models.Model):
    _inherit = "hr.recruitment.stage"

    color = fields.Integer(copy=True)


class HrRecruitmentStageGap(models.Model):
    _inherit = "hr.recruitment.stage"

    color = fields.Integer()
