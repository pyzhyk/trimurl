from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from urlshortener.views import redirect_url_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('newurl/', views.newurl, name="newurl"),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
    path('mylinks/', views.mylinks, name="mylinks"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
