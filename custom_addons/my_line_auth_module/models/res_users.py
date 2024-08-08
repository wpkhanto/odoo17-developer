from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    # Add any additional fields or methods related to LINE login