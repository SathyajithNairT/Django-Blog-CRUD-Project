from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about-me/', views.about_me, name = 'about'),
    path('add-posts/', views.add_post, name = 'add'),
    path('continue-reading/<int:blog_id>/', views.continue_reading, name = 'continue_reading'),
    path('edit/<int:blog_id>/', views.edit, name = 'edit'),
    path('delete/<int:blog_id>/', views.delete, name = 'delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
  