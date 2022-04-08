# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_time = fields.Datetime(string="Appointment Time")
    booking_date = fields.Date(string="Booking Date")

    