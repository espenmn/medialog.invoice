from pp.client.plone.browser.compatible import InitializeClass
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api

from medialog.invoice.interfaces import IInvoiceSettings


class InvoiceView(BrowserView):
    """ PDF view for invoice.    """

    template = ViewPageTemplateFile('invoice.pt')

    def __call__(self, *args, **kw):
        transformations = (
            'makeImagesLocal',
        )

        return self.template(self.context)

    @property
    def sum(self):
        return  api.portal.get_registry_record('sum', interface=IInvoiceSettings)

    @property
    def kontonr(self):
        return  api.portal.get_registry_record('kontonr', interface=IInvoiceSettings)

    @property
    def paid_to(self):
        return  api.portal.get_registry_record('paid_to', interface=IInvoiceSettings)

    @property
    def bodytext(self):
        return  api.portal.get_registry_record('bodytext', interface=IInvoiceSettings)

    @property
    def betalingsfrist(self):
        return  api.portal.get_registry_record('betalingsfrist', interface=IInvoiceSettings)

    @property
    def get_users(self):
        usergroup = api.user.get_users()
        userlist = []

        for member in usergroup:
            summ = self.sum
            if member.getProperty('utenbys'):
                summ = summ/2
            userlist.append(
                { 'id': member.getProperty('id'),
                  'etternavn': member.getProperty('etternavn'),
                  'fornavn': member.getProperty('fornavn'),
                  'postnr': member.getProperty('postnr'),
                  'poststed': member.getProperty('poststed'),
                  'honnor': member.getProperty('honn_rmedlem'),
                  'adresse': member.getProperty('adresse'),
                  'utenbys': member.getProperty('utenbys'),
                  'sum': summ,
                  })

        return userlist

InitializeClass(InvoiceView)
