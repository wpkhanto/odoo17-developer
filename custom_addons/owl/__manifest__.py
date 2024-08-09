# -*- coding: utf-8 -*-
{
    'name': "OWL Tutorial",
    'version': '1.0',
    'summary': 'OWL Tutorial',
    'sequence': -1,
    'description': """OWL Tutorial""",
    'category': 'OWL',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'asset': {
        'web.assets_backend': [],
    },
}