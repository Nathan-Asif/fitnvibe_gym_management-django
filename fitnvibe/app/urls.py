from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("membership", views.membership, name="membership"),
    path("about-us", views.about_us, name="about_us"),
    path('contact-us', views.contact_form, name='contact_form')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)