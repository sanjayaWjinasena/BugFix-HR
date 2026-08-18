# -*- coding: utf-8 -*-
from odoo import fields, models


class HrRecruitmentStage(models.Model):
    _inherit = 'hr.recruitment.stage'

    x_color = fields.Integer(string='Color')
