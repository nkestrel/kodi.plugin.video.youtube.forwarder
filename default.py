'''
    Youtube Forwarder for XBMC
    Copyright (C) 2014 Kestrel

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import xbmcaddon
import xbmcgui
import xbmcplugin

def getParams(string):
    parsed = {};
    if string:
        params = string[1:].split("&")
        for param in params:
            pair = param.split("=")
            if len(pair) == 2:
                parsed[pair[0]] = pair[1]
    return parsed

if (__name__ == "__main__" ):
    pluginhandle = int(sys.argv[1])
    params = getParams(sys.argv[2])

    addon = xbmcaddon.Addon()
    if (addon.getSetting('destBromix') == 'true'):
        url = "plugin://plugin.video.bromix.youtube/play/?video_id="
    else:
        url = "plugin://" + addon.getSetting('destCustom') 

    if params:
        get = params.get
        if get("action") == "play_video":
            url = url + get("videoid")
            listitem = xbmcgui.ListItem(path=url)
            xbmcplugin.setResolvedUrl(pluginhandle, True, listitem)
    else:
        language = addon.getLocalizedString
        dialog = xbmcgui.Dialog()
        dialog.ok(addon.getAddonInfo('name'), language(33010) + ": " + url)
        del dialog