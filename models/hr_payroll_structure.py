from odoo import api, models


class HrPayrollStructure(models.Model):
    _inherit = 'hr.payroll.structure'

    @api.model
    def _bugfix_hr_setup_workers_payroll(self):
        """Workers Payroll as on v17-final: no country (a country hides the structure from
        companies of other countries) and the Salary Payment journal set for the journal's own
        company (journal_id is company dependent)."""
        st = self.env.ref('BugFix-HR.workers_payroll_structure', raise_if_not_found=False)
        if not st:
            return
        st.country_id = False
        journal = self.env['account.journal'].sudo().search(
            [('code', '=', 'SALPY'), ('name', '=', 'Salary Payment')], limit=1)
        if not journal:
            return
        self.env['ir.property'].sudo().search([
            ('name', '=', 'journal_id'),
            ('res_id', '=', 'hr.payroll.structure,%s' % st.id),
            ('company_id', '!=', journal.company_id.id),
        ]).unlink()
        st.with_company(journal.company_id).sudo().journal_id = journal
