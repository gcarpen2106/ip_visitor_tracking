# ip_visitor_tracking/__manifest__.py

{
    'name': 'ip_visitor_tracking',
    'version': '1.0',
    'author': 'Gonzalo Carretero',
    'category': 'Website',
    'summary': 'Seguimiento de Visitantes mediante Geolocalización IP',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/visitor_views.xml',
    ],
    'icon': '/ip_visitor_tracking/static/description/icon58.png',
    'installable': True,
    'application': True,
}