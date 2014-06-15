# Twitter-monitoring: Monitor your Twitter statistics

A [Pandora FMS](http://pandorafms.com/) agent plugin written in Python to monitor statistics about a twitter account.


#Screenshots
![General vision of the plugin](https://dl.dropboxusercontent.com/u/374770/twitter_plugin_1.PNG "General vision of the plugin")

![Graph of the followers](https://dl.dropboxusercontent.com/u/374770/twitter_plugin_2.PNG "Graph of the followers")


#Quick start

##Prerequisites

This agent plugin assumes that you have a Pandora FMS server installed somewhere.
As this plugin is installed in an agent, we need to access Pandora FMS' server
IP to port 41121 TCP ([Tentacle protocol](http://www.openideas.info/wiki/index.php?title=Tentacle:Protocol#Tentacle_Protocol_Definition)).

For installing Pandora FMS's server, visit the [downloads section](http://pandorafms.com/Community/download/en) and install the appliance using [this instructions](http://wiki.pandorafms.com/index.php?title=Pandora:Documentation_en:Appliance_Install#Installation).


This agent plugin also assumes that you have installed an agent somewhere and it's already configured pointing to your Pandora FMS' server. [Download](http://pandorafms.com/Community/download/en) the agent, and [configure it properly](http://wiki.pandorafms.com/index.php?title=Pandora:Documentation_en:Operations#Common_Configuration_Parameters).


This agent plugin needs [Twython ](https://github.com/ryanmcgrath/twython).
### Install from PyPi

    pip install twython

or

    easy_install twython


##Installation of the plugin

Move the pandora_twitter_plugin.py file to your agent's folder, and add the following entry to the agent's configuration file:

    module_plugin python Path_to_your_agent_folder/twitter_pandora.py

Substitute 'Path_to_your_agent_folder' with a valid path.
