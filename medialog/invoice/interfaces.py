# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer



from z3c.form import interfaces
from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.invoice')


class IMedialogInvoiceLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""



class IInvoiceSettings(form.Schema):
    """Adds settings to medialog.controlpanel
    """

    form.fieldset(
        'invoice',
        label=_(u'Invoice settings'),
        fields=[
             'paid_to',
             'sum',
             'bodytext',
             'kontonr'
        ],
     )

    paid_to = schema.Text (
    	title=_(u"Paid to", default=u"Paid to"),
    )

    sum = schema.TextLine (
    	title=_(u"Sum", default=u"Sum"),
    )
    bodytext = schema.Text (
    	title=_(u"Bodytext", default=u"Bodytext"),
    )

    kontonr = schema.Text (
    	title=_(u"Account nr.", default=u"Kontonr."),
    )

alsoProvides(IInvoiceSettings, IMedialogControlpanelSettingsProvider)