from odoo import models, fields, api

class printingpressOrderline(models.Model):
    _name = "printingpress.orderline"
    _description = "This table contains all orderline records"
    # _rec_name="product_id"
    
    product_id = fields.Many2one('printingpress.product', string="Product", required=True)
    quentity = fields.Integer(string="Quentity", group_operator="sum", default=1)
    unit_price = fields.Integer(related="product_id.price_per_book", string="Unit Price")
    total_price = fields.Float(string="Total_price", digits=(5,2), required=True)
    orderl_id = fields.Many2one('printingpress.order', string="Order")
    


    