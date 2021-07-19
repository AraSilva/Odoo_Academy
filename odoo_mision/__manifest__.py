{
    'name': 'Mision Espacial',
    'summary': """Aplicacion de Mision Espacial""",
    'description': "Aplicacion de Mision Espacial de Odoo",
    'author': 'Ara',
    'category': 'Training',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/mision_menuitems.xml',
        'views/nave_views.xml',
        'security/mision_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/mision_demo.xml'
    ],
}