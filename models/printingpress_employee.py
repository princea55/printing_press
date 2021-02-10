from odoo import models, fields, api
from odoo.exceptions import ValidationError
# from openerp import api
# from openerp.models import TransientModel

class printingpressEmployee(models.Model):
    _name = "printingpress.employee"
    _description = "This table contains all customers records"
    # _inherit = 'mail.thread'
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Employee name already exists !')
    ]
    _order = "salary asc"
    
    name = fields.Char(string="Employee Name", required=True, track_visibilty='always')
    email = fields.Char(string="Employee Email", required=True)
    contact = fields.Char(string="Employee Contact", required=True, track_visibilty='onchange')
    image = fields.Binary(string='photo', attachment=False, store=True)
    employee_category = fields.Many2one('printingpress.employeetype', string='Employee Category')
    salary = fields.Integer(string="Employee Salary", required=True)
    experience = fields.Integer(string='Experience(In year)', size=3, required=True)
    country = fields.Many2one('res.country', string='Country')
    state = fields.Many2one('res.country.state', string='State')
    address = fields.Text(string="Address")
    city = fields.Char(string='City')
    
    
    def wiz_open(self):
        # not working
        # print(self.env['ir.actions.act_window']._for_xml_id('printingpress_employee.action_update_employee_salary'))
        return {
            'type':'ir.actions.act_window',
            'res_model':'printingpress.employeesalary',
            'view_mode':'form',
            'target':'new',
        }


    @api.constrains('experience')
    def _check_amount(self):
        for line in self:
            if line.experience <= 0:
                raise ValidationError('Employee experience must be 0 or greater!')

    # @api.onchange('country')
    # def set_values_to(self):from openerp import api
# from openerp.models import TransientModel
    # @api.model
    # def fields_view_get(self, view_id=None, view_type='tree', toolbar=False, submenu=False):
    #     print("***************Field View Get Method Called************")
    #     """ Set the correct label for `unit_amount`, depending on company UoM """
    #     print(self)
    #     result = super(printingpressEmployee, self).fields_view_get(view_id=view_id, view_type='tree', toolbar=toolbar, submenu=submenu)
    #     # result['arch'] = self._apply_timesheet_label(result['arch'])
    #     print(result)
    #     result['fields']['name']['sortable']=False
    #     result['fields']['name']['string']="Employees"
    #     return result

    
    