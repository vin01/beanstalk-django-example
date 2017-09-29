# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import textwrap

from django.http import HttpResponse
from django.views.generic.base import View


class HealthPageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
.
        ''')
        return HttpResponse(response_text)
