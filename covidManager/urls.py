from django.contrib import auth
from django.urls import path, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [ path('create/', csrf_exempt(views.create), name='create'),
                path('update/', csrf_exempt(views.update), name='update'),
                path('updateloc/', csrf_exempt(views.updateloc), name='updateloc'),
                path('addfriend/', csrf_exempt(views.addfriend), name='addfriend'),
                path('friendloc/', csrf_exempt(views.friendloc), name='friendloc'),
                path('notify/', csrf_exempt(views.notify), name='notify'),
                path('accept/', csrf_exempt(views.accept), name='accept-friend'),
                path('reject/', csrf_exempt(views.reject), name='reject-friend')
               ] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)