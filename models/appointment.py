# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'ref'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference", default="Odoo Mates", help="This is the reference")
    prescription = fields.Html(String="Prescription")
    priority = fields.Selection([
        ('0', 'very low'),
        ('1', 'low'),
        ('2', 'normal'),
        ('3', 'high')
    ], String="Priority", help="Give the priority to that appointment")

    state = fields.Selection([('draft', 'Draft'),
                              ('in_consultation', 'In Consultation'),
                              ('done', 'Done'),
                              ('canceled', 'Canceled'),
                              ],
                             String="Status", default="draft", required=True)

    gender = fields.Selection(String="Gender", related="patient_id.gender")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        for rec in self:
            rec.ref = rec.patient_id.ref

    def object_test(self):
        print("Button Pressed")
        message = "Click Successful"
        return {
            'effect': {
                'fadeout': 'slow',
                'message': message,
                'type': 'rainbow_man',
            }
        }

    @api.constrains("appointment_time")
    def check_date(self):
        for record in self:
            if record.appointment_time < fields.datetime.now():
                raise ValidationError(_("Choose a date/time for today and above in field Appointment Time"))
