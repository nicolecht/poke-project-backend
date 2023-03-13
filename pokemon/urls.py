from django.urls import path, include
from pokemon.views import signup, login_view, home, logout_view

urlpatterns = [
    # path('signup/', signup, name='signup'),
    # path('login/', login_view, name='login'),
    # path('home/', home, name='home'),
    # path('logout/', logout_view, name='logout'),

    # paths to djoser endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/users/', include('djoser.urls.authtoken')),
]