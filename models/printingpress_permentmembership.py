from odoo import models, fields, api

class printingpressPermanentlymembership(models.Model):
    _name="printintgpress.permanentlymembership"
    _description = "custopmer membership permanently"

    name = fields.Selection([
        ('bronze', 'Bronze Level'),
        ('silver', 'Silver Level'),
        ('gold', 'Gold Level'),
        ('platinum', 'Platinum Level')
        
    ], string='Memmbership Level', required=True)