from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    re_path(r'^post/(?P<pk>[\d]+)/$',views.post_detail,name='post_detail'),
    re_path(r'^post/new/$',views.post_new,name='post_new'),
    re_path(r'^post/(?P<pk>[\d]+)/edit/$',views.post_edit,name='post_edit'),
    path('post/<pk>/remove',views.post_remove,name='post_remove'),
    path('drafts/',views.post_draft_list,name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),


]
