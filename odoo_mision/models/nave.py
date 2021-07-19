# -*- coding:utf-8 -*-

from odoo import models, fields, api


class Nave(models.Model):
    _name = 'mision.nave'
    _description = 'Mision Info'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    capacity = fields.Integer(string='Capacity', default=3)

    active = fields.Boolean(string='Active', default=True)
