# -*- coding: utf-8 -*-
{
    'name': "gse_product",

    'summary': """
        Modifs du product""",

    'description': """
        
    """,

    'author': "Sébastien Bühl",
    'website': "http://www.buhl.be",

    'category': 'Customizations',
    'version': '0.1.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['website_sale'],

    'data': [        
        'templates/product_template.xml',
        'views/ir_attachment.xml',
        'views/product_template.xml',
    ],
    
}