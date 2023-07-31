from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', views.index, name='index'),
    path('submit', views.submit, name='submit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('list', views.list, name='list'),
    path('sortdata', views.sortdata, name='sortdata'),
    path('searchdata', views.searchdata, name='searchdata'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    # register
    path('login/', views.login_view, name='login'),
    path('', views.register_view, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)