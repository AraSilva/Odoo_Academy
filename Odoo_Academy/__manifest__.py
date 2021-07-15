{
    'name': 'Odoo Academy',
    'summary': 'Academy app to manage Training',
    'description': "Academy Module to manage Training",
    'author': 'Odoo',
    'category': 'Training',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/course_views.xml',
        'views/academy_menuitems.xml',
        'security/academy_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}