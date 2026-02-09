from django.urls import path
from .views import post_list,post_detail,post_create,post_delete,post_update
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', post_list, name='list'),
    path('detail/<int:id>/', post_detail, name='detail'),
    path('create/', post_create, name='create'),
    path('delete/<int:id>/', post_delete, name='delete'),
    path('update/<int:id>/',post_update, name='update')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)