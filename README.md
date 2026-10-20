# Odoo Equipment Maintenance Hub

A portfolio project demonstrating custom module development for Odoo 17, with an equipment registry and maintenance request workflow.

**GitHub repository:** https://github.com/aimanhaizal/odoo-equipment-maintenance

## Features

- Equipment registry with unique serial-number validation
- Maintenance request creation and tracking
- Equipment assignment to maintenance requests
- Priority levels and maintenance workflow states
- Kanban, list, and form views
- Access control configuration
- Demo XML data for equipment and maintenance requests
- Automated tests for equipment creation and duplicate serial-number validation

## Application Dashboard

The application runs in an isolated Docker Compose environment.

**Open the dashboard on the development machine:**

[http://localhost:8079](http://localhost:8079)

If you are accessing the development machine from another device on the same network, use:

[http://10.1.32.1:8079](http://10.1.32.1:8079)

The network address is specific to the current development environment. It will only work from another device if the host is reachable and network/firewall settings permit access.

## Run the Project Locally

### Prerequisites

- Docker Engine
- Docker Compose v2
- Git

### 1. Clone the repository

```bash
git clone https://github.com/aimanhaizal/odoo-equipment-maintenance.git
cd odoo-equipment-maintenance
```

### 2. Configure environment variables

Create a local `.env` file in the project root:

```bash
cat > .env <<'EOF'
POSTGRES_USER=odoo
POSTGRES_PASSWORD=dev_only_change_me
EOF
```

These are development credentials for a local portfolio environment only. Do not reuse them in production.

### 3. Start the services

```bash
docker compose up -d
```

Check the service status:

```bash
docker compose ps
```

View Odoo logs if needed:

```bash
docker compose logs -f web
```

### 4. Open Odoo

On the Docker host, open:

http://localhost:8079

Sign in with the Odoo account configured for your database. PostgreSQL credentials are separate from the Odoo login.

The Compose configuration targets the `equipment_dev` database. For a fresh installation, ensure that this database has been initialized before using the application.

### 5. Explore the module

After signing in, open **Equipment Hub** and explore:

- **Equipment** — view and manage registered equipment.
- **Maintenance Requests** — create requests, assign equipment, set priorities, and move requests through their workflow.

### 6. Stop the services

To stop the containers without deleting the database volumes:

```bash
docker compose stop
```

To start them again:

```bash
docker compose start
```

## Testing

Automated module tests have been run against a separate test database. The equipment creation and duplicate serial-number validation tests passed.

## Project Structure

```text
addons/
└── equipment_maintenance/
    ├── demo/
    ├── models/
    ├── security/
    ├── tests/
    └── views/
compose.yaml
README.md
```

## Technology Stack

- Odoo 17
- Python
- PostgreSQL 15
- Docker Compose
- XML views and demo data
- Git and GitHub

## Project Status

Core equipment registry and maintenance request functionality is implemented. Future improvements may include additional workflow tests, screenshots, and expanded documentation.

## License

This repository's code is released under the **MIT License**. See [`LICENSE`](LICENSE). The Kaggle dataset is a separate work; refer to its source page for applicable terms.