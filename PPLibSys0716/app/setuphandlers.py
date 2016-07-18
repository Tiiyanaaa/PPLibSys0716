from collective.grok import gs
from PPLibSys0716.app import MessageFactory as _

@gs.importstep(
    name=u'PPLibSys0716.app', 
    title=_('PPLibSys0716.app import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('PPLibSys0716.app.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
