## Youtube Forwarder
Kodi/XBMC plugin

![](/icon.png)

**Forward Youtube play requests to a different plugin.**

Takes the place of the [standard Youtube plugin (by TheCollective)](https://github.com/HenrikDK/youtube-xbmc-plugin) so that playback requests from plugins and remote apps (eg [Reddit TV](https://github.com/AddonScriptorDE/plugin.video.reddit_tv) & [Yatse Android Remote](http://yatse.leetzone.org/redmine)) can be forwarded to a different plugin of choice. It does this by sharing the same plugin ID (*plugin.video.youtube*) and using a large version number so it takes precedence and is not overwritten. By default, play requests are forwarded to [Bromix's Youtube plugin](https://github.com/bromix/plugin.video.bromix.youtube) but any Youtube-capable plugin can be specified if its path structure is known.

There is no need to overwrite the existing Youtube plugin as this plugin's higher version number ensures it takes precedence. Installing from the ZIP file will place it in the addons folder *plugin.video.youtube.forwarder*. Delete this folder to uninstall and the original Youtube plugin will become available again. Uninstalling through the interface also works but is usually not possible due to dependencies.

This plugin is not an ideal solution, it prevents the normal Youtube plugin from being accessed and on slower hardware like the Raspberry Pi, the extra hop to get to the destination plugin takes a few extra seconds. A better approach would be to use a background service that intercepts plugin requests and redirects them to the user's plugin of choice. Kodi services however do not currently have this capability.  