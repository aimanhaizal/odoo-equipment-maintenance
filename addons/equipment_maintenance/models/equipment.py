
from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _name = "maintenance.equipment.portfolio"
    _description = "Portfolio Equipment"
    _order = "name"

    _sql_constraints = [
        (
            "serial_number_unique",
            "UNIQUE(serial_number)",
            "Serial number must be unique.",
        ),
    ]

    name = fields.Char(
        string="Equipment Name",
        required=True,
    )
    serial_number = fields.Char(
        string="Serial Number",
        copy=False,
    )
    location = fields.Char(
        string="Location",
    )
    purchase_date = fields.Date(
        string="Purchase Date",
    )
    active = fields.Boolean(
        default=True,
    )
    notes = fields.Text(
        string="Notes",
    )
