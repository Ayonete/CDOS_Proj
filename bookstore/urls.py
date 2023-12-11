"""
This module defines URL routes fo rthe entire application. 
"""
# importing the django's in-built admin url
from django.contrib import admin
# importing path and include from django's in-built urls
from django.urls import path, include

# importing conf from settings.py
from django.conf import settings
# importing conf.urls from static
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# defining the list for urls
urlpatterns = [
    path('signup/', include('users.urls')),
    path('signin/', auth_views.LoginView.as_view(
        template_name='users/signin.html'), name='sign_in'),
    path('signout/', auth_views.LogoutView.as_view(
        template_name='users/signout.html'), name='sign_out'),
    # registering books application's urls in project
    path('', include('books.urls')),
    path('admin/', admin.site.urls),

]
# appending the urls with the static urls
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
