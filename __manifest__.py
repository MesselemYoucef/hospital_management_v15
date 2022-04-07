{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'DXB Coder Messelem',
    'sequence': -105,
    'summary': 'Hospital Management System',
    'description': """
This module contains all the required tools for a successful sale.
    """,
    'depends': [
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/patient_view.xml",
        "views/patient_view_female.xml",
        "views/patient_view_male.xml",
    ],
    'demo': [
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
