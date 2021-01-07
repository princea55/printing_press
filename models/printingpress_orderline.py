from odoo import models, fields, api
from odoo.exceptions import ValidationError

class printingpressOrderline(models.Model):
    _name = "printingpress.orderline"
    _description = "This table contains all orderline records"
    _sql_constraints = [
        ('quentity_check', 'check (quentity >= 10)', "Quentity must be greater or eqaul 10!"),
    ]
    # _rec_name="product_id"
    # @api.depends('quentity','unit_price')
    # def _compute_total_price(self):
    #     for i in self:
    #         print(i.unit_price,i.quentity)
    #         i.total_price = i.unit_price * i.quentity

    
    @api.onchange('quentity')
    def _onchange_quentity(self):
        print("onchange call")
        for i in self:
            print(i.unit_price, i.quentity)
            i.total_price = i.unit_price * i.quentity

    product_id = fields.Many2one(
        'printingpress.product', string="Product", required=True)
    quentity = fields.Integer(string="Quentity", group_operator="sum",
                              default=1, readonly=False, track_visibility='onchange')
    unit_price = fields.Integer(
        related="product_id.price_per_book", string="Unit Price")
    total_price = fields.Float(
        string="Total price", digits=(5, 2), readonly=True, store=True)
    orderl_id = fields.Many2one('printingpress.order', string="Order")

    @api.constrains('total_price')
    def _check_amount(self):
        for line in self:
            print("line Price",line.total_price)
            if line.total_price <=0:
                raise ValidationError('The amount of a cash transaction cannot be 0.')