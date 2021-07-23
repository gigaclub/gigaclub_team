from odoo import fields, models, api


class GCRequest(models.Model):
    _inherit = "gc.request"

    receiver_id = fields.Reference(selection_add=[("gc.team", "gc.team")])
    sender_id = fields.Reference(selection_add=[("gc.team", "gc.team")])
