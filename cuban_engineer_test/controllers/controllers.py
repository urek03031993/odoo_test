# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class SocialMediaController(http.Controller):

    @http.route('/customers', type='http', auth="public", website=True)
    def customers_list(self, search='', **kwargs):
        domain = []
        if search:
            domain += ['|', '|', '|',
                        ('name', 'ilike', search),
                        ('facebook_url', 'ilike', search),
                        ('linkedin_url', 'ilike', search),
                        ('x_url', 'ilike', search)]

        partners = request.env['res.partner'].sudo().search(domain)
        return request.render('cuban_engineer_test.customers', {
            'partners': partners,
            'search': search,
        })

