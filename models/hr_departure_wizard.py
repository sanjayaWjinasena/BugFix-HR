# -*- coding: utf-8 -*-
from odoo import models


class HrDepartureWizard(models.TransientModel):
    _inherit = 'hr.departure.wizard'

    def action_register_departure(self):
        # Stock archives the allocations directly, which raises for allocations in
        # confirm/validate state. End those at the departure date instead and let
        # stock run with the archive option switched off.
        wizards = self.filtered('archive_allocation')
        for wizard in wizards:
            allocations = self.env['hr.leave.allocation'].sudo().search([
                ('employee_id', '=', wizard.employee_id.id),
                ('state', 'in', ('confirm', 'validate')),
            ])
            for allocation in allocations:
                if allocation.date_from and allocation.date_from > wizard.departure_date:
                    continue
                if not allocation.date_to or allocation.date_to > wizard.departure_date:
                    allocation.date_to = wizard.departure_date
        wizards.write({'archive_allocation': False})
        return super().action_register_departure()
