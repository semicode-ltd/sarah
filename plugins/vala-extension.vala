/*
 * pulg.vala
 * 
 * Copyright 2016 Semicode Inc <aye7@archost>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */
using Sarah;

public class Hello : Object, IExtension
{
    //PlugApp.API plugins;
    public Object object { get; construct set; }
    //public abstract Window window { get; construct set; }

    public void activate (string [] args)
    {
		stdout.printf ("Really >");
		foreach(var s in args )
			stdout.printf("%s ",s);   
    }

    public void deactivate ()
    {

    }
}

[ModuleInit]
public void peas_register_types (GLib.TypeModule module)
{
    var objmodule = module as Peas.ObjectModule;
    objmodule.register_extension_type (typeof (IExtension),
                                       typeof (Hello));
}
