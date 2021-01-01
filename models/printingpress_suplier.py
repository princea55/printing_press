from odoo import models, fields, api

class printingpressSuplier(models.Model):
    _name = "printingpress.suplier"
    _description = "This table contains all suplier records"

    name = fields.Char(string = "Suplier Name", required=True)
    email = fields.Char(string = "Suplier Email")
    contact = fields.Char(string = "Suplier Contact No.")
    address = fields.Text(string = "Suplier Address")
    

    