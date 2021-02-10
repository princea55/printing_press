from odoo import models, fields, api

class printingpressCrm(models.Model):
    _inherit = "crm.lead"
    _description = "adding fields to crm.lead"

    website_name = fields.Char(String="Website Name")