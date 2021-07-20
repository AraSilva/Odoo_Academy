{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage Training""",
    'description': "Academy Module to manage Training",
    'author': 'Odoo',
    'category': 'Training',
    'version': '1.0',
    'depends': ['sale'],
    'data': [
        'views/course_views.xml',
        'views/academy_menuitems.xml',
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}