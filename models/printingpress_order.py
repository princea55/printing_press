from odoo import models, fields, api, _


class printingpressOrder(models.Model):
    _name = "printingpress.order"
    _description = "This table contains all customers records"
    _rec_name = "customer_id"

   


    @api.onchange('orderline_ids')
    def _total_order_price(self):
        for i in self:
            ttp = 0
            for j in i.orderline_ids:
                ttp += j.order_price
            i.update({
                'total':ttp,
            })

    customer_id = fields.Many2one(
        'printingpress.customer', string="Customer", required=True)
    isworking = fields.Boolean(string='IsWorking', default=False)
    iscomplete = fields.Boolean(string='IsComplete', default=False)
    date = fields.Date(string='Date')
    name_seq = fields.Char(string='Order reference', required=True,
                           copy=False, readonly=True, index=True, default=lambda self: _('New'))
    # product_id = fields.Many2one('printingpress.orderline', string="Product Orders", required=True)
    currency_id = fields.Many2one('res.currency', string='Currency')
    orderline_ids = fields.One2many('printingpress.orderline', 'orderl_id', string='orders')
    total_price = fields.Integer(related='orderline_ids.total_price',string="Total_price")
    total = fields.Integer(string="Total")
    order_sequence = fields.Char(string="Order reference", required=True,
                           copy=False, readonly=True, index=True, default=lambda self: _('New'))
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

    # @api.model
    # def default_get(self, fields_list):
    #     print("================default_get called============")
    #     print(fields_list)
    #     res = super(printingpressOrder, self).default_get(fields_list)

    #     print(res)

    #     if 'total_order_price' in fields_list:
    #         res['total_order_price'] = 100

    #     print("==============after super called===============")
    #     print(res)
    #     return res
    @api.model
    def create(self, vals):
        if vals.get('order_sequence', _('New')) == _('New'):
            vals['order_sequence'] = self.env['ir.sequence'].next_by_code('printingpress.order') or _('New')

        result = super(printingpressOrder, self).create(vals)
        return result