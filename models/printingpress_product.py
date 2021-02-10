from odoo import models, fields, api
from odoo.exceptions import UserError

class printingpressProduct(models.Model):
    _name = "printingpress.product"
    _description = "This table contains all products records"

    def _get_total_no_of_product(self):
        print("=====================>>>>>>>>>>call _get_total_no_of_product")
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
    currency_id = fields.Many2one(
        'res.currency', string='Currency')
    price_per_book = fields.Monetary(string="Price Per Book", required=True)
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
    

    def get_operation(self):
        print("======================blank recordset=========",self.env['printingpress.product'])
        print("self.env Environment object", self.env,type(self.env))
        print("self.env.context", self.env.context, type(self.env.context))
        print("params",self.env.context.get('params'))
        record = self.env['printingpress.product'].search([('product_category_id','=',2)],limit=2)
        multi_record = self.env['printingpress.product'].search([])
        print(multi_record.get_metadata())
        for i in multi_record:
            if i.exists():
                print("==============================single record================", i.name)
            else:
                print("**************record does not exixts***************")
        for i in self.env['printingpress.product'].search_read([('product_category_id', '=', 2)]):
            print(i['name'])

        print("==================count in serach ===================",self.env['printingpress.product'].search([('product_category_id','=',2)],count=True))
        print("==========list of record=========",record)
        print("==========browse===========",self.env['printingpress.product'].browse([2,4]))
    @api.model
    def create(self, vals):
        print("=====================================creaate method call")
        print("====================VALUE====================",vals)
        vals['name'] = vals['name'].lower()
        vals['isbn'] = "00"+vals['isbn'] 
        # print(type(vals['product_subcategory_id']))
        vals.update({'product_language_id':[(0,0,{"name":"French"})]})

        # vals.update({'product_language_id':[(4,2)]})
        rec = super(printingpressProduct, self).create(vals)
        
        print('=====================rec create method===================',rec)
        print('=====================vals create method===================',vals)
        return rec

    def get_filtered(self):
        record_set = self.env['printingpress.product'].search([])
        
        row = record_set.filtered(lambda r: r.price_per_book < 1000)
        for i in row:
            print("*******************",i.name)

    def sorted_function(self):
        record_set = self.env['printingpress.product'].search([])
        print("===================sorted method==============",record_set.sorted('id', reverse=True))


    def mapped_method(self):
        record_set = self.env['printingpress.product'].search([])
        print("===========mapped-email============",record_set.mapped('name'))

    # @api.model
    # def search_count(self, args):
    #     """ search_count(args) -> int

    #     Returns the number of records in the current model matching :ref:`the
    #     provided domain <reference/orm/domains>`.
    #     """
    #     print("===================search_count callled=============")
    #     res = super(printingpressProduct,self).search_count(args, count=True)
    #     print(res)
    #     return res 

    # @api.model
    # def search(self, args, offset=0, limit=None, order=None, count=False):
    #     print("==========================search method called")
    #     res = super(printingpressProduct,self).search(args=[('product_category_id','=',2)], offset=3, limit=5, order="name asc", count=False)
    #     print(res)
    #     print(type(res))
    #     return res

    # @api.model
    # def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
    #     print("======================search_read method called===========")
    #     rec = super(printingpressProduct,self).search_read(domain=None, fields=None, offset=0, limit=None, order=None)
    #     for i in rec:
    #         print(i)
    #         print("\n")
    #     return rec
    
    def write(self, vals):
        print("=======================write method called=============",vals)
        # print(self.env['printingpress.product'].search_read([('id', '=', )]))
        # print(self.env['printingpress.product'].browse([self.env.context['params']['id']]))
        # current_record = 
        # print(current_record.product_category_id)
        vals.update({'product_language_id':[(1,4,{"name":"chinese"})]})
        res = super(printingpressProduct, self).write(vals)
        # vals.update({'product_language_id':[(1,0,{"product_language_id":"French"})]})
        
      
        print(type(res))
        print("***********************write rec **************",res)
        return res
    
    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        print("============Read_group method called===========")
        rec = super(printingpressProduct,self).read_group(domain=[('price_per_book','>',1000)], fields=['name','price_per_book'], groupby=['product_category_id'], offset=0, limit=1, orderby=False, lazy=True)
        print(type(rec))
        for i in rec:
            print(i)
            print("\n")
        return rec

    def name_get(self):
        print("================name_get called===============")
        result = []
        for rec in self:
            name = str(rec.name) + " - " + str(rec.publisher_name)
            result.append((rec.id, name))
        return result

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        print("**********************name_serach Called***************")
        if args is None:
            args = []
        args = args+['|',('name',operator,name),('publisher_name',operator,name)]
        print("**************************************",args)
        print("===========================domainjoin================================")
        rec = super(printingpressProduct, self).search(args=args, offset=0, limit=limit, order=None, count=False).name_get()
        print(rec)
        return rec

    
    def copy(self, default=None):
        print("*****************copy method Called*************")
        # print(self.ensure_one())
        # self.ensure_one()
        default =  dict()
        default.update({'name':"Prince", 'image':""})
        print(default)     
        print(type(default))   
        res = super(printingpressProduct, self).copy(default=default)
        print("**********************end copy method",res)
        # Re-evaluating the domain
        # res._onchange_model_and_list()
        return res
    

    def unlink(self):
        print("*****************unlink method called***********",self)
        for i in self:
            if int(i.price_per_book) > 5000:
                raise UserError("You can not delete this record")
        
        rec = super(printingpressProduct, self).unlink()
        print("********unlink return statement", rec)
        return rec

    