from odoo import models, fields, api

class printingpressOrder(models.Model):
    _name = "printingpress.order"
    _description = "This table contains all customers records"
    _rec_name="customer_id"
    
    customer_id = fields.Many2one('printingpress.customer', string="Customer", required=True)
    isworking = fields.Boolean(string='IsWorking')
    iscomplete = fields.Boolean(string='IsComplete')
    # product_id = fields.Many2one('printingpress.orderline', string="Product Orders", required=True)
    
    orderline_ids = fields.One2many('printingpress.orderline', 'orderl_id', string='')
    
    


    