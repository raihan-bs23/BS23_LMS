from django.urls import path
from .views import RegistrationView
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='pages/login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('sign_up/', RegistrationView.as_view(), name='user_registration'),
    path('demo/', views.Demo, name='demo'),
    path('profile/<user>', views.UserProfile, name='user_profile'),
    path('edit_profile/<user_id>/<username>/', views.EditUserProfile, name='edit_user_profile'),
    path('add_user_info/<user_id>/<user>/', views.AddUserAdditionalInfo, name='add_user_info'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
