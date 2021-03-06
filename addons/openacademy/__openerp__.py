# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-2015 Aselcis Consulting, S.L. (https://www.aselcis.com). All Rights Reserved
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    'name': 'Open Academy',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Miguel Paraíso',
    'category': 'Test',
    'description': """
    Módulo Open Academy para gestionar cursos
    - cursos
    - sesiones
    - registro de asistentes
    """,
    'data': [
             'views/openacademy_view.xml', # Todos los demas archivos de datos excepto datos demo y tests
             'views/partner.xml',
             ],
    'demo': [
             # Archivos XML o YAML que contienen datos demo
             ],
    'tests': [
              # Archivos XML o YAML que contienen tests
              ],
    'instalable': True,
    'auto_install': False,
    # 'certificate' : 'certificate',
}


