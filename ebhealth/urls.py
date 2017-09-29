from django.conf.urls import url

from ebhealth.views import HealthPageView

urlpatterns = [
    url(r'^health$', HealthPageView.as_view(), name='health'),
    url(r'^$', HealthPageView.as_view(), name='health'),
]
