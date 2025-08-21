from odoo.tests.common import TransactionCase


class TestResPartner(TransactionCase):

    def setUp(self):
        super(TestResPartner, self).setUp()
        self.Partner = self.env['res.partner']

    def test_complete_profile(self):
        partner = self.Partner.create({
            'name': 'Partner1Complete',
            'facebook_url': 'https://facebook.com/test',
            'linkedin_url': 'https://linkedin.com/test',
            'x_url': 'https://x.com/test',
        })

        self.assertTrue(partner.complete_profile)

    def test_incomplete_profile(self):
        partner = self.Partner.create({
            'name': 'Partner2Incomplete',
            'facebook_url': 'https://facebook.com/test',
        })

        self.assertFalse(partner.complete_profile)

    def test_search_functionality(self):
        partner = self.Partner.create({
            'name': 'Partner3Search',
            'facebook_url': 'https://facebook.com/test',
            'linkedin_url': 'https://linkedin.com/test',
            'x_url': 'https://x.com/test',
        })

        partners_by_name = self.Partner.search([('name', 'ilike', 'Search')])
        self.assertIn(partner, partners_by_name)

        partners_by_facebook = self.Partner.search([('facebook_url', 'ilike', 'facebook')])
        self.assertIn(partner, partners_by_facebook)

        partners_by_linkedin = self.Partner.search([('linkedin_url', 'ilike', 'linkedin')])
        self.assertIn(partner, partners_by_linkedin)

        partners_by_twitterx = self.Partner.search([('x_url', 'ilike', 'x')])
        self.assertIn(partner, partners_by_twitterx)