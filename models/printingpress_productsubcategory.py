from odoo import models, fields, api

class printingpressProductsubcategory(models.Model):
    _name = "printingpress.productsubcategory"
    _description = "This table contains all product Subcategory records"
    
    name = fields.Char(string = "Product Subcategory Name", size=20, help="Name of the Subcategory category", required=True)
    products_ids = fields.One2many('printingpress.product', 'product_subcategory_id', string="Products")