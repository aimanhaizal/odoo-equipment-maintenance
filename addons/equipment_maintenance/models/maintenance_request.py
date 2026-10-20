from odoo import api, fields, models


class MaintenanceRequest(models.Model):
    _name = "maintenance.request.portfolio"
    _description = "Portfolio Maintenance Request"
    _order = "priority desc, deadline, id desc"

    name = fields.Char(
        string="Request Title",
        required=True,
    )
    equipment_id = fields.Many2one(
        comodel_name="maintenance.equipment.portfolio",
        string="Equipment",
        required=True,
        ondelete="restrict",
    )
    description = fields.Text(
        string="Description",
    )
    technician_id = fields.Many2one(
        comodel_name="res.users",
        string="Assigned Technician",
    )
    priority = fields.Selection(
        selection=[
            ("0", "Low"),
            ("1", "Normal"),
            ("2", "High"),
            ("3", "Critical"),
        ],
        default="1",
        required=True,
    )
    deadline = fields.Date(
        string="Target Date",
    )
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("in_progress", "In Progress"),
            ("repaired", "Repaired"),
            ("cancelled", "Cancelled"),
        ],
        default="new",
        required=True,
        copy=False,
    )
    notes = fields.Text(
        string="Resolution Notes",
    )

    def action_start(self):
        self.write({"state": "in_progress"})

    def action_repaired(self):
        self.write({"state": "repaired"})

    def action_cancel(self):
        self.write({"state": "cancelled"})

    def action_reset(self):
        self.write({"state": "new"})
