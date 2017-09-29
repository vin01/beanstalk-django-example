from django.conf.urls import url

import pdfmanager.views

urlpatterns = [
    url(r'^download_pdf$', pdfmanager.views.download_pdf, name='download_pdf'),
]

