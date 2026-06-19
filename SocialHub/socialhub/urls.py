from social.views import home, register, create_post, delete_post, like_post
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
urlpatterns = [
    # Admin page
    path('admin/', admin.site.urls),

    # Home page
    path('', home, name='home'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),

    # Register page
    path('register/', register, name='register'),
    path('create_post/', create_post, name='create_post'),
    # Login page
    path('like/<int:post_id>/', like_post, name='like_post'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),

    # Logout page
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    
]