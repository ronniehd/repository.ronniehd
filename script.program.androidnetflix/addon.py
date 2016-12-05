import xbmc
import xbmcgui
import os

appname="Netflix"
packagename="com.netflix.mediaclient"

def launcher():
	packagepath = os.popen('pm path %s' % packagename).read()
	if packagepath:
		xbmc.executebuiltin('XBMC.StartAndroidActivity("%s")' % packagename)
	else:
		xbmcgui.Dialog().ok('App No Instalada', 'Esto es solo un atajo.  Por favor instale la app "%s" (%s) e intente de nuevo.' % (appname, packagename))
		xbmc.executebuiltin('XBMC.StartAndroidActivity("com.android.vending","android.intent.action.VIEW",,"market://details?id=%s")' % packagename)
launcher()
