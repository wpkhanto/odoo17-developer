{
    'name': 'My LINE Auth Module',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Login with LINE API',
    'description': """
Module to allow users to login using their LINE account.
    """,
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_users_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
}