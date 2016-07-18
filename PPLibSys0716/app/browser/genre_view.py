from five import grok
from plone.directives import dexterity, form
from PPLibSys0716.app.content.genre import IGenre

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IGenre)
    grok.require('zope2.View')
    grok.template('genre_view')
    grok.name('view')

