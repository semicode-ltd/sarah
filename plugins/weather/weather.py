#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  weather.py
#
#  Copyright 2016 Semicode Inc <aye7@archost>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import os
import sys

import gi
gi.require_version('Peas', '1.0')
gi.require_version('Sarah', '1.0')
from gi.repository import GObject, Peas, Sarah


class WeatherPlugin(GObject.Object, Sarah.IExtension):
    __gtype_name__ = 'WeatherPlugin'

    object = GObject.property(type=GObject.Object)

    def do_activate(self, args, argv):
        os.system("curl wttr.in/"+' '.join(args))

    def do_deactivate(self):
       pass
