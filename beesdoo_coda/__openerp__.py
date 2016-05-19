# -*- coding: utf-8 -*-
{
    'name': "Beescoop Coda Import module",

    'summary': """
		Import coda Wizard based on https://github.com/acsone/pycoda
     """,

    'description': """
    """,

    'author': "Beescoop - Cellule IT",
    'website': "https://github.com/beescoop/Obeesdoo",

    'category': 'Accounting & Finance',
    'version': '0.1',

    'depends': ['account'],

    'data': [
        'security/ir.model.access.csv',
        'views/partner.xml',
        'wizard/views/new_member_card.xml',
    ],
}
