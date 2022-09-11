from odoo import api, fields, models, _
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="Reference", default="Odoo Mates")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender",
                              default="female")

    weight = fields.Float(string="Weight")
    height = fields.Float(string="Height")
    active = fields.Boolean(string="Active", default=True)
    date_of_birth = fields.Date(String="DOB")
    age = fields.Integer(string="Age", compute="_compute_age")

    @api.depends("date_of_birth")
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1


