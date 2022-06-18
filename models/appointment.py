# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'ref'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference", default="Odoo Mates")
    prescription = fields.Html(String="Prescription")
    priority = fields.Selection([
        ('0', 'very low'),
        ('1', 'low'),
        ('2', 'normal'),
        ('3', 'high')
    ], String="Priority", help="Give the priority to that appointment")

    gender = fields.Selection(String="Gender", related="patient_id.gender")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        for rec in self:
            rec.ref = rec.patient_id.ref
    