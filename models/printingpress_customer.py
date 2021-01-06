from odoo import models, fields, api

class printingpressCustomer(models.Model):
    _name = "printingpress.customer"
    _description = "This table contains all customers records"
    _sql_constraints = [
       
        ('name_uniq', 'unique (name)', "Name name already exists !"),
        ('email_uniq', 'unique (email)', "Email name already exists !"),
    ]
    name = fields.Char(string = "Customer Name", size=20, help="Name of the customer", required=True)
    email = fields.Char(string = "Customer Email", required=True)
    contact = fields.Char(string = "Customer Contact No.",size=10)
    city = fields.Char(string='Customer City')
    image = fields.Binary(string='photo', attachment=False, store=True)
    address = fields.Text(string = "Customer Address")
    # product_ids = fields.One2many('printingpress.product', 'customer_id', string="Product")
    order_ids = fields.One2many('printingpress.order', 'customer_id', string="Order")
    

    