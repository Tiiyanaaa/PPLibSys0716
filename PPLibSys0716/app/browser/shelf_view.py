from five import grok
from plone.directives import dexterity, form
from PPLibSys0716.app.content.shelf import IShelf

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IShelf)
    grok.require('zope2.View')
    grok.template('shelf_view')
    grok.name('view')

