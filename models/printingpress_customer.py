from odoo import models, fields, api, _


class printingpressCustomer(models.Model):
    _name = "printingpress.customer"
    _description = "This table contains all customers records"
    _inherit = 'mail.thread'
    _parent_store = True
    #  _parent_name= "parent_id"
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Name name already exists !"),
        ('email_uniq', 'unique (email)', "Email name already exists !"),
    ]
    name = fields.Char(string="Customer Name", size=20,
                       help="Name of the customer", required=True)
    email = fields.Char(string="Customer Email",
                        required=True, track_visibility="always")
    contact = fields.Char(string="Customer Contact No.", size=10)
    city = fields.Char(string='Customer City')
    image = fields.Binary(string='photo', attachment=False, store=True)
    zip_code = fields.Char(string='Zip', size=6, track_visibility="onchange")
    street = fields.Char(string="Street2..")
    street2 = fields.Char(string="Street2...")
    country = fields.Many2one('res.country', string='Country')
    state = fields.Many2one('res.country.state', string='State')
    parent_id = fields.Many2one(
        'printingpress.customer', 'Parent Menu', index=True, ondelete="cascade")
    child_ids = fields.One2many(
        'printingpress.customer', 'parent_id', string='Child Menus')
    parent_path = fields.Char(index=True)
    # product_ids = fields.One2many('printingpress.product', 'customer_id', string="Product")
    order_ids = fields.One2many(
        'printingpress.order', 'customer_id', string="Order")
    ref_key = fields.Reference([
        ('printintgpress.timemembership', 'Year Based'),
        ('printintgpress.permanentlymembership', 'Permannent Based')

    ], string="Reference Key")
    name_seq = fields.Char(string="Order reference", required=True,
                           copy=False, readonly=True, index=True, default='New')
    color = fields.Integer(string="color", default=0)
    
    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('printingpress.customer') or _('New')

        result = super(printingpressCustomer, self).create(vals)
        return result
