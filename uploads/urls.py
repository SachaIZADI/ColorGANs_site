from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from uploads.core import views

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import resolve, Resolver404

# try:
#     resolve(path)
# except Resolver404:
#     'not found'



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^uploads/home', views.home, name='home'),
    url(r'^home', views.home, name='home'),
    url(r'^uploads/simple', views.simple_upload, name='simple_upload'),
    url(r'^uploads/description/simple', views.simple_upload, name='simple_upload'),
    ################################ Sacha's stuffs #########################################

    url(r'^uploads/simple/sacha/predict$', views.simple_upload_sacha_predict, name='simple_upload_sacha'),
    url(r'^uploads/simple/sacha/return_image$', views.simple_upload_sacha_return_image, name='simple_upload_sacha_bis'),


    #####################################################################################
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^uploads/description/$', views.description, name='description'),
    url(r'^uploads/us/$', views.us, name='us'),
    url(r'^uploads/refs/$', views.refs, name='refs'),
    url(r'^uploads/how_it_works/$', views.how_it_works, name='how_it_works'),
    url(r'^admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
