
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add_course$', views.add_course, name="add_course"),
    url(r'^comment/(?P<id>\d+)$', views.comment, name="comment"),
    url(r'^add_comment/(?P<id>\d+)$', views.add_comment, name="add_comment"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove"),
    url(r'^confirm_remove/(?P<id>\d+)$', views.confirm_remove, name="confirm_remove"),
    url(r'^user_courses/$', views.user_courses, name="user_courses"),
    url(r'^add_user_to_course/$', views.add_user_to_course, name="add_user_to_course"),
]
