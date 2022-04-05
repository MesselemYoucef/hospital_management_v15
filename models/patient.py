# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Name")
    ref = fields.Char(string="Reference")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    weight = fields.Float(string="Weight")
    height = fields.Float(string="Height")
    active = fields.Boolean(string="Active", default=True)
    