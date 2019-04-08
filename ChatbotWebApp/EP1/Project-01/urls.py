from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

# when using class based views always remember to use .as_view() with the view
urlpatterns = [
    path('', views.RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(template_name='Project01/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='Project01/logout.html'), name="logout"),
    path('login/home/', views.HomeView.as_view(), name="home"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profile/edit/', views.ProfileEditView.as_view(), name="profile_edit"),
    path('profile/password/', views.PasswordChange.as_view(), name="password_reset"),
    path('my_ajax_view/', views.AjaxTest.as_view(), name="ajax-test"),
    path('helpdesk/', views.HelpDeskView.as_view(), name="helpdesk"),
    path('helpdesk/ticket/', views.TicketView.as_view(), name="ticket_submitted"),

]
