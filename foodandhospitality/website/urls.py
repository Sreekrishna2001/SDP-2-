from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.loginuser, name='loginuser'),
    path('profile', views.profile, name="profile"),
    path('register', views.Register, name="Register"),
    # path('aboutus',views.aboutus),
    # path('foodview', views.restsview),
    # path('aboutus', views.aboutus),
    path('logout', views.logoutuser),
    path('upload', views.upload),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
