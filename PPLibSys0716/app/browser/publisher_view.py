from five import grok
from plone.directives import dexterity, form
from PPLibSys0716.app.content.publisher import IPublisher

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IPublisher)
    grok.require('zope2.View')
    grok.template('publisher_view')
    grok.name('view')

