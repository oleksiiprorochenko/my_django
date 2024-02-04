from django.urls import path

from . import views


urlpatterns = [
    path("main/", views.index, name="index"),
    path("child/", views.return_simple_html, name="child"),
    path("teams/", views.css_style, name="teams"),
    path("header/", views.header_footer, name="header"),
    path("signup/", views.SignUpView.as_view(), name="signup")
]