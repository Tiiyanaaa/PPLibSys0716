from five import grok
from plone.directives import dexterity, form
from PPLibSys0716.app.content.publishers import IPublishers

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IPublishers)
    grok.require('zope2.View')
    grok.template('publishers_view')
    grok.name('view')

