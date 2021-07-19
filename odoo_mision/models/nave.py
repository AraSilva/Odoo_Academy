# -*- coding:utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Nave(models.Model):

    _name = 'mision.nave'
    _description = 'Mision Info'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    capacity = fields.Integer(string='Capacity', default=3)

    dimension = fields.Text(string='Dimensiones')
    fuel = fields.Selection(string='Fuel Type',
                            selection=[('diesel', 'Diesel'),
                                       ('super', 'Super'),
                                       ('alcohol', 'Alcohol')],
                            copy=False)

    active = fields.Boolean(string='Active', default=True)

    type = fields.Selection(string='Ship Type',
                            selection=[('big', 'Big'),
                                       ('median', 'Median'),
                                       ('small', 'Small')],
                            copy=False)

    @api.onchange('capacity')
    def _check_capacity(self):
        for record in self:
            if record.capacity < 3:
                raise ValidationError('Capacity can not be lees than 3: %s' % record.capacity)
