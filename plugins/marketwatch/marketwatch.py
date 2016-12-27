#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  marketwatch.py
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
import webbrowser
import gi
gi.require_version('Peas', '1.0')
gi.require_version('Sarah', '1.0')
from gi.repository import GObject, Peas, Sarah


class MarketWatchPlugin(GObject.Object, Sarah.IExtension):
    __gtype_name__ = 'MarketWatchPlugin'

    object = GObject.property(type=GObject.Object)

    def do_activate(self, args, argv):
        lookup_term = ''
        country = ''
        security_type = ''
        base_url ="http://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup=" 
        if 1 <= argv <= 3:
            if argv == 1:
                lookup_term = args[0].title()
                url = base_url + lookup_term
            elif argv == 2:
                lookup_term = args[0].title()
                country = args[1].title()
                url = base_url + lookup_term + "&Country=" + country
            elif argv == 3:
                lookup_term = args[0].title()
                country = args[1].title()
                security_type = args[2].title()
                url = base_url + lookup_term + "&Country=" + country + "&Type=" + security_type
            webbrowser.open(url)

        else:
            print("Usage: sarah marketwatch lookup_term [country] [security_type]")

    def do_deactivate(self):
       pass
