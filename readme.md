## Youtube Forwarder
Kodi/XBMC plugin

![](/icon.png)

Allows plugins and remote applications designed to play videos with the standard Youtube plugin (by TheCollective) to work with a different plugin of choice. It does this by sharing the same plugin ID (plugin.video.youtube) and using a large version number so it takes precedence and is not overwritten. Play requests are then forwarded to the plugin specified in settings, by default this is Bromix's Youtube plugin but any Youtube-capable plugin can be specified if its path structure is known.

There is no need to overwrite the existing Youtube plugin as this plugin's higher version number ensures it takes precedence. Installing from the ZIP file will place it in the folder "plugin.video.youtube.forwarder". Delete this folder to uninstall and the original Youtube plugin will become available again. Uninstalling through the interface also works but is usually not possible due to dependencies.

This plugin is not an ideal solution, it prevents the normal Youtube plugin from being accessed and on slower hardware like the Raspberry Pi, the extra hop to get to the destination plugin takes a few extra seconds. A better approach would be to use a background service to intercept plugin requests and redirect them to the user's plugin of choice. Kodi services however do not currently have this capability.  