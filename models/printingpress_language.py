from odoo import models, fields, api

class printingpressLanguage(models.Model):
    _name = "printingpress.language"
    _description = "This table contains all product language records"
    _sql_constraints = [
        ('lan_uniq', 'unique(name)', "Language name already exists !"),
    ]
    name = fields.Char(string = "Language", size=50, help="Name of the language category", required=True)
    # language_id = fields.Many2one('printingpress.product', string="Products")
    color = fields.Integer(string="color", default=0)