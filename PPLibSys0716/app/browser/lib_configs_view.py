from five import grok
from plone.directives import dexterity, form
from PPLibSys0716.app.content.lib_configs import ILibConfigs

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ILibConfigs)
    grok.require('zope2.View')
    grok.template('lib_configs_view')
    grok.name('view')

