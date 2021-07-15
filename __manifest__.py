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
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}