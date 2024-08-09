# -*- coding: utf-8 -*-
from odoo import api, fields, models

class  OwlList(models.Model):
    _name = 'owl.todo.list'
    _description = 'OWL Todo List App'

    name = fields.Char(string='Task Name')
    completed = fields.Boolean()
    color = fields.Char()