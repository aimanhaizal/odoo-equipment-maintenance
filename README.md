# Odoo Equipment Maintenance Hub

A portfolio project demonstrating custom module development for Odoo 17.

## Features

- Equipment registry with unique serial-number validation
- Maintenance request tracking
- Equipment assignment to maintenance requests
- Priority levels and workflow states
- List, form, and Kanban views
- Access control configuration
- Demo data for equipment and maintenance requests
- Automated tests for equipment creation and duplicate serial-number validation

## Development Environment

The project uses Docker Compose with separate Odoo and PostgreSQL services.

- Odoo: 17
- PostgreSQL: 15
- Development URL: `http://localhost:8079`
- Development database: `equipment_dev`

The project has its own Docker services, database volume, and addon directory. It is designed to remain separate from any existing work Odoo environment.

## Testing

The module's automated tests have been run against a separate test database. The equipment creation and duplicate serial-number validation tests passed.

## Status

Core equipment and maintenance request functionality is implemented. Further improvements can include additional workflow tests, user documentation, and screenshots of the application.