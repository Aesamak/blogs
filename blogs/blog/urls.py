from django.urls import path
from .views import blog_list,create_post,blog_detail,edit_post,delete_post

urlpatterns = [
    path("", blog_list, name="blog_list"),
    path("create/", create_post, name="create_post"),
    path("blog/<int:blog_id>/", blog_detail, name="blog_detail"),
    path("blogs/<int:blog_id>/edit/", edit_post, name="edit_post"),
    path("blogs/<int:blog_id>/delete/", delete_post, name="delete_post"), 
]
