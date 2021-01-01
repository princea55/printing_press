from odoo import models, fields, api

class printingpressProductcategory(models.Model):
    _name = "printingpress.productcategory"
    _description = "This table contains all product category records"
    
    name = fields.Char(string = "Product Category Name", size=50, help="Name of the product category", required=True)
    products_ids = fields.One2many('printingpress.product', 'product_category_id', string="Products")
    