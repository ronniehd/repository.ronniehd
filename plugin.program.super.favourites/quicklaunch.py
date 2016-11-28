#
#       Copyright (C) 2014-
#       Sean Poyser (seanpoyser@gmail.com)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#


def run():
    import xbmcgui
    if xbmcgui.Window(10000).getProperty('Super_Favourites_Chooser') == 'true':
        return

    import xbmc
    import chooser
    
    if not chooser.GetFave('SF_QL', includePlay=True):
        return False
    
    path = xbmc.getInfoLabel('Skin.String(SF_QL.Path)')

    if len(path) == 0 or path == 'noop':
        return

    toTest = path.replace(',return', '').lower()

    if toTest.startswith('activatewindow') and ',' in toTest: #i.e. NOT like ActivateWindow(filemanager)
        if not toTest.startswith('activatewindow(10003'): #Filemanager
            xbmc.executebuiltin(path)
            return

    #remove any spurious SF stuff, e.g.
    #ActivateWindow("weather?sf_options=desc%3DShow%2520Weather%26_options_sf",return) needs to be
    #ActivateWindow(weather)
    path = path.split('?')[0]
    path = path.replace('"',      '')
    path = path.replace('&quot;', '')
    if not path.endswith(')'):
        path += ')'

    import player
    player.playCommand(path)
    

if __name__ == '__main__':
    run()
