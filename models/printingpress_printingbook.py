from odoo import models, fields, api


class printingpressprintingpress(models.Model):
    _name = "printingpress.printingbook"
    _description = "This table contains all customers records"
    _rec_name="product_id"
    product_id = fields.Many2one(
        'printingpress.product', string="Product", required=True)
    isworking = fields.Boolean(string='IsWorking')
    iscomplete = fields.Boolean(string='IsComplete')
