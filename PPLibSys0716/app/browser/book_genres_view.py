from five import grok
from plone.directives import dexterity, form
from PPLibSys0716.app.content.book_genres import IBookGenres

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IBookGenres)
    grok.require('zope2.View')
    grok.template('book_genres_view')
    grok.name('view')

