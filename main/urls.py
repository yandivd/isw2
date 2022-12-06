from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('historiasc/listar/', views.hclistar, name='listar_hc'),
    path('historiasc/create/', views.crearHC, name='crear_hc'),
    path('historiasc/view/<id>/', views.ver_hc, name='ver_hc'),
    path('historiasc/edit/<id>/', views.editar_hc, name='editar_hc'),
    path('historiasc/delete/<id>',views.matarPaciente, name='matarP'),
    # path('paciente/create/', views.crearPaciente, name='crear_paciente'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)