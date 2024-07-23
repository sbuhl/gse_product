# Copyright 2020 Tecnativa - Jairo Llopis
# Copyright 2021 Tecnativa - Víctor Martínez
# Copyright 2021 Tecnativa - Pedro M. Baeza
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
# -*- coding: utf-8 -*-
{
    'name': "gse_product",

    'summary': """
        Modifs du product""",

    'description': """
        
    """,

    "website": "https://github.com/OCA/e-commerce",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "maintainers": ["Yajo"],
    "license": "LGPL-3",

    'category': 'Customizations',
    'version': '17.0.0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['website_sale', 'delivery', 'stock', 'stock_delivery'],

    'data': [        
        'templates/product_template.xml',
        'views/ir_attachment.xml',
        'views/product_template.xml',
        'report/report.xml',
        'report/stock_picking_sbu.xml',
        # 'report/delivery_slip_sbu.xml',
    ],
    
}