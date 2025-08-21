# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    facebook_url = fields.Char(string='Facebook: ')
    linkedin_url = fields.Char(string='LinkedIn: ')
    x_url = fields.Char(string='TwitterX: ')
    complete_profile = fields.Boolean(compute='_compute_complete_profile',
                                        string='Perfil Completo',
                                        store=True)

    @api.depends('facebook_url', 'linkedin_url', 'x_url')
    def _compute_complete_profile(self):
        for partner in self:
            partner.complete_profile = all([bool(partner.facebook_url),  bool(partner.linkedin_url), bool(partner.x_url)])
