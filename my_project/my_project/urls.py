from django.contrib import admin
from django.urls import path, include
from accounts.views import signup
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset/', auth_views.PasswordResetView.as_view(
                            template_name='password_reset.html',
                            email_template_name='password_reset_email.html',
                            subject_template_name='password_reset_subject.txt'),
                            name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(
                            template_name='password_reset_done.html'), 
                            name='password_reset_done'),
    path('reset/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(
                            template_name='password_reset_confirm.html'), 
                            name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(
                            template_name='password_reset_complete.html'),
                            name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('', include('boards.urls')),

    # Change password
    path('settings/password/', auth_views.PasswordChangeView.as_view(
                            template_name='password_change.html'
                            ),
                            name='password_change'),
    path('settings/passowrd/done', auth_views.PasswordChangeDoneView.as_view(
                            template_name='password_change_done.html'
                            ),
                            name='password_change_done'),
    # path('change-password/', auth_views.PasswordChangeView.as_view(
    #                         template_name='change-password.html',
    #                         success_url = '/'),
    #                     name='change_password'),
]