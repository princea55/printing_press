from odoo import models, fields, api, _

class printingpressOrder(models.Model):
    _name = "printingpress.order"
    _description = "This table contains all customers records"
    _rec_name="customer_id"
    
    @api.depends('total_price')
    def _total_order_price(self):
        for i in self:
            i.total_order_price += i.total_price
    def get_product(self):
        return {
            'name':_()
        }

    customer_id = fields.Many2one('printingpress.customer', string="Customer", required=True)
    isworking = fields.Boolean(string='IsWorking', default=False)
    iscomplete = fields.Boolean(string='IsComplete', default=False)
    date = fields.Date(string='Date')
    name_seq = fields.Char(string='Order reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    # product_id = fields.Many2one('printingpress.orderline', string="Product Orders", required=True)
    
    orderline_ids = fields.One2many('printingpress.orderline', 'orderl_id', string='orders')
    total_price = fields.Float(related='orderline_ids.total_price',  string="Total_price")
    total_order_price = fields.Integer(string="Total_order_price", compute="_total_order_price", store=True)
    state = fields.Selection([
        ('initial', 'Initial'),
        ('place_order', 'Place Order'),
        ('confirmed_order', 'Confirmed Order'),
        ('cancel_order', 'Cancel Order'),
    ], string='State', default="initial")
    

    def place_btn(self):
        self.state = "place_order"

    def confirmed_btn(self):
        self.state = "confirmed_order"

    def cancel_btn(self):
        self.state = "cancel_order"
    
    
    


    