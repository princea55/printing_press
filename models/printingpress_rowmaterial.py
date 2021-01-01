from odoo import models, fields, api

class printingpressRowmaterial(models.Model):
    _name = "printingpress.rowmaterial"
    _description = "This table contains all row material records"
    
    name = fields.Char(string = "Name", copy=False , required=True)
    quentity = fields.Char(string = "Quentity", required=True)
    material_type = fields.Selection([
        ("solid","solid"),
        ("liquid","liquid"),
    ], string="Material Type", copy=False)
    rowmaterial_id = fields.Many2many('printingpress.vendor', 'rowmaterial_vendor', column1="rowmaterial_id", column2="vendor_id", string="Vendor")

