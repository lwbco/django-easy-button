from django.conf.urls.defaults import *



urlpatterns = patterns("",
    url(r"^admin/$", "easy.signup_codes.views.admin_invite_user", name="admin_invite_user"),
)
