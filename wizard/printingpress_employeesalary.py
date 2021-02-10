from odoo import models, fields, api

class employeesalary(models.TransientModel):
    _name = 'printingpress.employeesalary'
    _description = 'employee salary update'

    salary = fields.Integer(string="salary")

    def update_employee_salary(self):
        print("update salary called")
        self.env['printingpress.employee'].browse(self._context.get("active_ids")).update({'salary':self.salary})
        print("update successfully")
        return True