from odoo import models, fields, api
from odoo.exceptions import ValidationError
from openerp import api
from openerp.models import TransientModel

class printingpressEmployee(models.Model):
    _name = "printingpress.employee"
    _description = "This table contains all customers records"
    _inherit = 'mail.thread'
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Employee name already exists !')
    ]
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
    

    @api.constrains('experience')
    def _check_amount(self):
        for line in self:
            if line.experience <= 0:
                raise ValidationError('Employee experience must be 0 or greater!')

    # @api.onchange('country')
    # def set_values_to(self):
    #     if self.country:
    #         ids = self.env['res.country.state'].search(
    #             [('country_id', '=', self.country.id)])
    #         return {
    #             'domain': {'state': [('id', 'in', ids.ids)], }
    #         }

    
    