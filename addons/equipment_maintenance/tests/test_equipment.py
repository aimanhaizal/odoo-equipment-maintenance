from psycopg2 import IntegrityError

from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestEquipmentMaintenance(TransactionCase):

    def test_equipment_creation(self):
        equipment = self.env["maintenance.equipment.portfolio"].create({
            "name": "Test Pump",
            "serial_number": "TEST-PUMP-001",
            "location": "Test Lab",
        })

        self.assertEqual(equipment.name, "Test Pump")
        self.assertEqual(equipment.serial_number, "TEST-PUMP-001")
        self.assertTrue(equipment.active)

    def test_duplicate_serial_number_rejected(self):
        model = self.env["maintenance.equipment.portfolio"]

        model.create({
            "name": "Pump One",
            "serial_number": "DUPLICATE-001",
        })

        with self.assertRaises(IntegrityError):
            with self.cr.savepoint():
                model.create({
                    "name": "Pump Two",
                    "serial_number": "DUPLICATE-001",
                })