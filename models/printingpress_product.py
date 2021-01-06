from odoo import models, fields, api


class printingpressProduct(models.Model):
    _name = "printingpress.product"
    _description = "This table contains all products records"

    def _get_total_no_of_product(self):
        for record in self:
            record.count_products = self.env['printingpress.product'].search_count(
                [('product_category_id', '=', 2)])
        # print(self.env.ref('product_category_id')[0])

    def get_product_category(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Product Categories',
            'view_mode': 'tree',
            'res_model': 'printingpress.product',
            'domain': [('product_category_id', '=', 2)],
            'context': "{'create': False}"
        }

    name = fields.Char(string="Product Name", required=True)
    isbn = fields.Char(string="ISBN No.", required=True)
    publisher_name = fields.Char(string="Publisher Name")
    no_of_page = fields.Char(string="Number Of Page")
    price_per_book = fields.Integer(string="Price Per Book", required=True)
    product_detail = fields.Text(string="Product Description")
    # image = fields.Binary(string='Photo')
    count_products = fields.Integer(
        string='Count Product', compute="_get_total_no_of_product", store=False)
    image = fields.Binary(string='photo', attachment=False, store=True)
    # customer_id = fields.Many2one('printingpress.customer', ondelete="cascade", string="Customer", required=True)
    product_category_id = fields.Many2one(
        'printingpress.productcategory', string="Product Category", required=True)
    product_subcategory_id = fields.Many2one(
        'printingpress.productsubcategory', string="Product Subcategory")
    product_language_id = fields.Many2many('printingpress.language', 'products_language',
                                           column1="product_id", column2="language_id", string="Language", required=True)
    # order_ids = fields.One2many('printingpress.order', 'product_id', string="Orders")
    printingbook_ids = fields.One2many(
        'printingpress.printingbook', 'product_id', string="Printin Book")
