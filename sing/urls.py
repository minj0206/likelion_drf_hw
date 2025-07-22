from .views import *
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'sing'

urlpatterns=[
    path('', views.singer_list_create),
    path('<int:sing_id>', views.sing_detail_update_delete),
    path('<int:sing_id>/comment', views.comment_read_create),
    path('tags/<str:tags_name>', views.find_tag),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)