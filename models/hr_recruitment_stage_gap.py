# -*- coding: utf-8 -*-
from odoo import models, fields

class HrRecruitmentStageGap(models.Model):
    _inherit = 'hr.recruitment.stage'

    x_color = fields.Integer(string='Color')
