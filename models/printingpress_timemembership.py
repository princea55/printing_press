from odoo import models, fields, api

class printingpressTimemembership(models.Model):
    _name="printintgpress.timemembership"
    _description = "custopmer membership based on time"

    name = fields.Selection([
        ('1', '1 Year'),
        ('2', '2 Year'),
        ('5', '5 Year'),
        ('10', '10 Year')
        
    ], string='Memmbership Year', required=True)

    