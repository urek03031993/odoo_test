# -*- coding: utf-8 -*-
{
    'name': "Customer Social Media",

    'summary': "Gestión de Redes Sociales en Odoo",

    'description': """ Gestión de redes sociales para cada uno de los partners en la plataforma""",

    'author': "<<David Velazquez Garcia - dave331993@gmail.com>>",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['contacts'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],

    'assets': {
        'web.assets_backend': [
            '/cuban_engineer_test/static/src/css/style.css',
        ],
    }
}

