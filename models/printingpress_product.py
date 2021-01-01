from odoo import models, fields, api

class printingpressProduct(models.Model):
    _name = "printingpress.product"
    _description = "This table contains all products records"
    
    
    name = fields.Char(string = "Product Name", required=True)
    isbn = fields.Char(string = "ISBN No.", required=True)
    publisher_name = fields.Char(string = "Publisher Name")
    no_of_page = fields.Char(string="Number Of Page")
    price_per_book = fields.Integer(string="Price Per Book", required=True)
    product_detail = fields.Text(string="Product Description")
    image = fields.Binary(string='Photo')
    image = fields.Binary(string='photo', attachment=False, store=True)
    # customer_id = fields.Many2one('printingpress.customer', ondelete="cascade", string="Customer", required=True)
    product_category_id = fields.Many2one('printingpress.productcategory', string="Product Category", required=True)
    product_subcategory_id = fields.Many2one('printingpress.productsubcategory', string="Product Subcategory")
    product_language_id = fields.Many2many('printingpress.language','products_language', column1="product_id", column2="language_id", string="Language", required=True)
    # order_ids = fields.One2many('printingpress.order', 'product_id', string="Orders")
    printingbook_ids = fields.One2many('printingpress.printingbook', 'product_id', string="Printin Book")
    
    

    