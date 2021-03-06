from __future__ import unicode_literals
from frappe import _
import frappe
import datetime as dt

def get_data():

    return [
        {
            "label": _("Patients"),
            "icon": "icon-star",
            "items": [
                {
                    "type": "doctype",
                    "name": "Midwife Appointment",
                    "label": _("Appointment"),
                    "description": _("Appointment"),
                },
                {
                    "type": "doctype",
                    "name": "Patient Record",
                    "label": _("Patient Record"),
                    "description": _("Patient Record"),
                },
                {
                    "type": "doctype",
                    "name": "Free Prescription",
                    "label": _("Free Prescriptions"),
                    "description": _("Free Prescriptions"),
                },
                {
                    "type": "doctype",
                    "name": "Sales Invoice",
                    "label": _("Invoices"),
                    "description": _("Invoices"),
                },
                ]
            },
        {
            "label": _("Folders"),
            "icon": "icon-star",
            "items": [
                {
                    "type": "doctype",
                    "name": "Pregnancy",
                    "label": _("Pregnancy"),
                    "description": _("Pregnancy"),

                },
                {
                    "type": "doctype",
                    "name": "Prenatal Interview",
                    "label": _("Prenatal Interview"),
                    "description": _("Prenatal Interview"),

                },
                {

                    "type": "doctype",
                    "name": "Perineum Rehabilitation",
                    "label": _("Perineum Rehabilitation"),
                    "description": _("Perineum Rehabilitation"),

                },
                {
                    "type": "doctype",
                    "name": "Gynecology",
                    "label": _("Gynecology"),
                    "description": _("Gynecology"),

                },
            ]
        },
        {
            "label": _("Consultations"),
            "icon": "icon-star",
            "items": [
                {
                    "type": "doctype",
                    "name": "Pregnancy Consultation",
                    "label": _("Pregnancy Consultation"),
                    "description": _("Pregnancy Consultation"),
                },
                {
                    "type": "doctype",
                    "name": "Birth Preparation Consultation",
                    "label": _("Birth Preparation Consultation"),
                    "description": _("Birth Preparation Consultation"),
                },
                {
                    "type": "doctype",
                    "name": "Early Postnatal Consultation",
                    "label": _("Early Postnatal Consultation"),
                    "description": _("Early Postnatal Consultation"),
                },
                {
                    "type": "doctype",
                    "name": "Postnatal Consultation",
                    "label": _("Postnatal Consultation"),
                    "description": _("Postnatal Consultation"),
                },
                {
                    "type": "doctype",
                    "name": "Perineum Rehabilitation Consultation",
                    "label": _("Perineum Rehabilitation Consultation"),
                    "description": _("Perineum Rehabilitation Consultation"),
                },
                {
                    "type": "doctype",
                    "name": "Gynecological Consultation",
                    "label": _("Gynecological Consultation"),
                    "description": _("Gynecological Consultation"),
                },
                {
                    "type": "doctype",
                    "name": "Free Consultation",
                    "label": _("Free Consultation"),
                    "description": _("Free Consultation"),
                },

                ]
        },
        {
            "label": _("Setup"),
            "icon": "icon-star",
            "items": [
                {
                    "type": "doctype",
                    "name": "Professional Information Card",
                    "label": _("Professional Information Card"),
                    "description": _("Professional Information Card"),
                },
                {
                    "type": "doctype",
                    "name": "Codification",
                    "label": _("Codifications"),
                    "description": _("Codifications"),
                },
                {
                    "type": "doctype",
                    "name": "Drug",
                    "label": _("Drugs"),
                    "description": _("Drugs"),
                },
                {
                    "type": "doctype",
                    "name": "Lab Exam Type",
                    "label": _("Lab Exam Types"),
                    "description": _("Lab Exam Types"),
                },
                ]
            },

    ]
