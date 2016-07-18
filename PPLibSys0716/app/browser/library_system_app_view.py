from five import grok
from plone.directives import dexterity, form
from PPLibSys0716.app.content.library_system_app import ILibrarySystemApp

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(ILibrarySystemApp)
    grok.require('zope2.View')
    grok.template('library_system_app_view')
    grok.name('view')

