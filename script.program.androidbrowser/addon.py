import xbmc
import xbmcgui
import os

def launcher():
		xbmc.executebuiltin('XBMC.StartAndroidActivity(,"android.intent.action.VIEW",,"https://google.com")')
launcher()
