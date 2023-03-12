from django.urls import path
from pokemon.views import signup, login_view, home, logout_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
	path('logout/', logout_view, name='logout'),
]
