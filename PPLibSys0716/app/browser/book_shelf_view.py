from five import grok
from plone.directives import dexterity, form
from PPLibSys0716.app.content.book_shelf import IBookShelf

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IBookShelf)
    grok.require('zope2.View')
    grok.template('book_shelf_view')
    grok.name('view')

