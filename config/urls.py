from django.contrib import admin
from django.urls import path
from cinema.views import IndexView, SessaoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('sessoes/', SessaoView.as_view(), name='sessoes'),
]