#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Hi.py
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
import sys
import urllib
import json
import requests

import gi
gi.require_version('Peas', '1.0')
gi.require_version('Sarah', '1.0')
from gi.repository import GObject, Peas, Sarah


class AdhanPlugin(GObject.Object, Sarah.IExtension):
    __gtype_name__ = 'AdhanPlugin'

    object = GObject.property(type=GObject.Object)

    def do_activate(self, args, argv):
            try:
                my_country = args[0].title()
                my_city =   args[1].title()
                adhan_times = requests.get("http://api.aladhan.com/timingsByCity?city="+my_city+"&country="+my_country+"&method=3").json()
                print (" Prayer time for "+my_city+", "+my_country+" :\n",\
                    " Fajr "+adhan_times['data']['timings']['Fajr']+"\n",\
                    " Dhuhr "+adhan_times['data']['timings']['Dhuhr']+"\n",\
                    " Asr "+adhan_times['data']['timings']['Asr']+"\n",\
                    " Maghrib "+adhan_times['data']['timings']['Maghrib']+"\n",\
                    " Isha "+adhan_times['data']['timings']['Isha']+"\n")
            except Exception as e:
                print("A error occured, please run sarah [city] [country]")


    def do_deactivate(self):
        pass
