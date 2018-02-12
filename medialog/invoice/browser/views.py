from pp.client.plone.browser.compatible import InitializeClass
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class InvoiceView(BrowserView):
    """ PDF view for invoice.    """

    template = ViewPageTemplateFile('invoice.pt')

    def __call__(self, *args, **kw):
        transformations = (
            'makeImagesLocal',
        )

        return self.template(self.context)

    @property
    def group_users(self):
        usergroup = api.user.get_users()
        userlist = []

        for member in usergroup:
            userlist.append(
                { 'id': member.getProperty('id'),
                  'etternavn': member.getProperty('etternavn'),
                  'fornavn': member.getProperty('fornavn'),
                  'postnr': member.getProperty('postnr'),
                  'poststed': member.getProperty('poststed'),
                  'honnor': member.getProperty('honn_rmedlem'),
                  'adresse': member.getProperty('adresse'),
                  'utenbys': member.getProperty('utenbys'),
                  })

        return userlist

InitializeClass(InvoiceView)