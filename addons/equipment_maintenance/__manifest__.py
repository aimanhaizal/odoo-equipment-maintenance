
{
    "name": "Equipment Maintenance Hub",
    "version": "17.0.1.1.0",
    "category": "Operations/Maintenance",
    "summary": "Equipment registry and maintenance workflow",
    "description": """
        A portfolio project demonstrating custom Odoo 17 development.
        Includes equipment records and maintenance request tracking.
    """,
    "author": "Portfolio Project",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/equipment_views.xml",
        "views/maintenance_request_views.xml",
    ],
    "demo": [
        "demo/demo_data.xml",
    ],
    "application": True,
    "installable": True,
}
