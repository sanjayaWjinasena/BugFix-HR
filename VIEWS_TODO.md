# BugFix-HR — views to hand-port

46 views need hand-porting from Clear-DB. Do NOT 
auto-copy the arch — each has Studio xpath quirks that need 
human review before commit.

| # | Clear-DB view ID | Type | Target model | Name | Inherits |
|---|---|---|---|---|---|
| 1 | 6363 | form | `hr.expense.split.wizard` | Expense split | — |
| 2 | 5550 | form | `hr.applicant` | Odoo Studio: Jobs - Recruitment Form customization | Jobs - Recruitment Form |
| 3 | 5520 | tree | `hr.attendance` | Odoo Studio: hr.attendance.tree customization | hr.attendance.tree |
| 4 | 4930 | form | `hr.contract` | Odoo Studio: hr.contract.form customization | hr.contract.form |
| 5 | 4929 | form | `hr.employee` | Odoo Studio: hr.employee.form customization | hr.employee.form |
| 6 | 8349 | tree | `hr.employee` | Odoo Studio: hr.employee.tree customization | hr.employee.tree |
| 7 | 5553 | form | `hr.expense.sheet` | Odoo Studio: hr.expense.sheet.form customization | hr.expense.sheet.form |
| 8 | 4949 | form | `hr.expense` | Odoo Studio: hr.expense.view.form customization | hr.expense.view.form |
| 9 | 5551 | form | `hr.job` | Odoo Studio: hr.job.form customization | hr.job.form |
| 10 | 9511 | tree | `hr.payslip` | Odoo Studio: hr.payslip.tree.bank.data.jinasena customization | hr.payslip.tree.bank.data.jinasena |
| 11 | 5549 | tree | `hr.recruitment.stage` | Odoo Studio: hr.recruitment.stage.tree customization | hr.recruitment.stage.tree |
| 12 | 2867 | activity | `hr.expense` | hr.expense.activity | — |
| 13 | 4301 | form | `hr.expense.approve.duplicate` | hr.expense.approve.duplicate form | — |
| 14 | 2891 | form | `hr.expense` | hr.expense.extract.view.form | hr.expense.view.form |
| 15 | 5546 | form | `hr.expense` | hr.expense.extract.view.form_studio_cus | hr.expense.extract.view.form |
| 16 | 6549 | graph | `hr.expense` | hr.expense.extract.view.graph | hr.expense.graph |
| 17 | 4418 | tree | `hr.expense` | hr.expense.extract.view.list | hr.expense.tree |
| 18 | 2897 | form | `hr.expense` | hr.expense.form.inherit.sale.expense | hr.expense.view.form |
| 19 | 2865 | graph | `hr.expense` | hr.expense.graph | — |
| 20 | 2861 | kanban | `hr.expense` | hr.expense.kanban | — |
| 21 | 2862 | kanban | `hr.expense` | hr.expense.kanban | hr.expense.kanban |
| 22 | 2863 | kanban | `hr.expense` | hr.expense.kanban | hr.expense.kanban |
| 23 | 2864 | pivot | `hr.expense` | hr.expense.pivot | — |
| 24 | 2852 | form | `hr.expense.refuse.wizard` | hr.expense.refuse.wizard.form | — |
| 25 | 2881 | activity | `hr.expense.sheet` | hr.expense.sheet.activity | — |
| 26 | 2873 | tree | `hr.expense.sheet` | hr.expense.sheet.dashboard.tree | hr.expense.sheet.tree |
| 27 | 2874 | form | `hr.expense.sheet` | hr.expense.sheet.form | — |
| 28 | 2901 | form | `hr.expense.sheet` | hr.expense.sheet.form.inherit.sale.expense | hr.expense.sheet.form |
| 29 | 2879 | graph | `hr.expense.sheet` | hr.expense.sheet.graph | — |
| 30 | 2875 | kanban | `hr.expense.sheet` | hr.expense.sheet.kanban | — |
| 31 | 2876 | kanban | `hr.expense.sheet` | hr.expense.sheet.kanban | hr.expense.sheet.kanban |
| 32 | 2877 | kanban | `hr.expense.sheet` | hr.expense.sheet.kanban | hr.expense.sheet.kanban |
| 33 | 2878 | pivot | `hr.expense.sheet` | hr.expense.sheet.pivot | — |
| 34 | 2871 | tree | `hr.expense.sheet` | hr.expense.sheet.tree | — |
| 35 | 6742 | form | `hr.expense.sheet` | hr.expense.sheet.view.form.inherit.sale.expense | hr.expense.sheet.form |
| 36 | 2880 | search | `hr.expense.sheet` | hr.expense.sheet.view.search | — |
| 37 | 6366 | search | `hr.expense.sheet` | hr.expense.sheet.view.search.with.panel | hr.expense.sheet.view.search |
| 38 | 6741 | form | `hr.expense.split.wizard` | hr.expense.split.view.inherit.sale.expense | Expense split |
| 39 | 2856 | tree | `hr.expense` | hr.expense.tree | — |
| 40 | 2857 | tree | `hr.expense` | hr.expense.tree | hr.expense.tree |
| 41 | 2858 | tree | `hr.expense` | hr.expense.tree | hr.expense.tree |
| 42 | 2898 | tree | `hr.expense` | hr.expense.tree.inherit.sale.expense | hr.expense.tree |
| 43 | 2859 | form | `hr.expense` | hr.expense.view.form | — |
| 44 | 2860 | form | `hr.expense` | hr.expense.view.form | hr.expense.view.form |
| 45 | 7922 | form | `hr.expense` | hr.expense.view.form.inherit.documents.hr.expense | hr.expense.view.form |
| 46 | 2866 | search | `hr.expense` | hr.expense.view.search | — |
