from django.contrib import admin
from django.urls import path
from . import views

from.views import IndexView, SessaoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('sessoes/', SessaoView.as_view(), name='sessoes'),
]