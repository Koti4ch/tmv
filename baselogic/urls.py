from django.urls import path
from baselogic import views as handler


urlpatterns = [
    path('sendmail/', handler.FormHendler.as_view(), name='sendmail'),
]

