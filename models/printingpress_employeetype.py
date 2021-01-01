from odoo import models, fields, api

class printingpressEmployeetype(models.Model):
    _name = "printingpress.employeetype"
    _description = "This table contains all employee type records"
    
    name = fields.Char(string = "Type Name", size=50, help="Name of the employee type", required=True)
    employee_ids = fields.One2many('printingpress.employee', 'employee_category', string="Employee_ids")
    