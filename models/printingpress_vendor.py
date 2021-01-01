from odoo import models, fields, api

class printingpressVendor(models.Model):
    _name = "printingpress.vendor"
    _description = "This table contains all suplier records"

    name = fields.Char(string = "Vendor Name", required=True)
    email = fields.Char(string = "Vendor Email", required=True)
    contact = fields.Char(string = "Vendor Contact No.", required=True, size=10)
    city = fields.Char(string = "Vendor City")
    address = fields.Text(string = "Vendor Address")
    vendor_type = fields.Selection([
        ('book_supplier', 'Book Supplier'),
        ('Row_material_supplier', 'Row Material Supplier'),
    ], string='Vendor type',required=True)
    # rowmaterial_ids = fields.One2many('printingpress.rowmaterial', 'rowmaterial_id', string="Row Material")

    