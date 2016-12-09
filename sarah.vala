/*
 * Sarah.vala
 * 
 * Copyright 2016 aye7 <aye7@archost>
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
 
namespace Sarah
{
	
	/**********************************************
	 * 
	 *  Sarah Extension Plugins
	 * 
	 **********************************************/
	 public interface IExtension : Object {

		/* This will be set to the window */
		public abstract Object object { get; construct set; }

		/* The "constructor" */
		public abstract void activate(string [] args );

		/* The "destructor" */
		public abstract void deactivate();
	}
	
	/**********************************************
	 * 
	 *  Sarah Core Plugins
	 * 
	 **********************************************/ 
	
	public class Core : GLib.Object
	{
		public Sarah.IExtension extension;
		public Peas.Engine engine;
		public Peas.ExtensionSet extension_set;
		public Peas.PluginInfo plugin;

		public Core ()
		{
			this.engine = Peas.Engine.get_default ();
			this.engine.add_search_path ("./", null);
			//this.engine.enable_loader ("python");
			this.engine.enable_loader("python");
		}

		public string [] list (bool active = false) {
			unowned GLib.List<Peas.PluginInfo> plugin_list = this.engine.get_plugin_list ();
			//ArrayList <string>? plugins = new ArrayList <string> ();
			string [] plugins ={} ;
			foreach (Peas.PluginInfo plugin in plugin_list)
			{
				plugins += plugin.get_name(); 
				if(active)
					stdout.printf ("%#s \t %#s\n", plugin.get_module_name (), plugin.get_description () );
				
			}
			return plugins;
		}
		
		public void run (string[] args)
		{
		    extension_set = new Peas.ExtensionSet (engine, typeof(IExtension), "object", this);
		    //this.engine.load_plugin (this.plugin);
		    this.plugin = engine.get_plugin_info (args[1]) ;
		    this.engine.load_plugin (plugin);
		    extension       =  extension_set.get_extension(plugin) as IExtension;
		    var activatable = extension;
		    string []  arglist = args[2:args.length];
		    activatable.activate (arglist);
		}
	}


	/**********************************************
	 * 
	 * 	Sarah Appliction
	 * 
	 **********************************************/
    public class App
    {
        private Core manager;
        private string [] plugins;
        
        public App ()
        {
            manager = new Core();
            
        }

        public void init (string[] args)
        {
			if (args.length <= 1)
			{
				stdout.printf ("Help Me!\n");
			}else {
				if (args[1] == "list"){
					stdout.printf("Commands :\n");
					plugins = manager.list(true);
				} else {
					plugins = manager.list();
					if (args[1] in plugins){
						manager.run(args);
					}
				}
			}
        }
        
    }



}


