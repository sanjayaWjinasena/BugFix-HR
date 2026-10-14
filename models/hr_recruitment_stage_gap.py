from odoo import fields, models


class HrRecruitmentStageGap(models.Model):
    _inherit = 'hr.recruitment.stage'

    x_color = fields.Integer(string='Color')
