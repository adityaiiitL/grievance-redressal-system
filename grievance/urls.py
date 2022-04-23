
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('student/', include('student.urls')),
    path('faculty/', include('faculty.urls')),
    path('', views.index, name='index'),
    path('home',views.home, name='home'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),

    # path('accounts/', include('allauth.urls'))

] + static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
