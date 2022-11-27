from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('historiasc/listar/', views.hclistar, name='listar_hc'),
    path('historiasc/create/', views.crearHC, name='crear_hc'),
    path('historiasc/view/<int:pk>/', views.verHC, name='ver_hc'),
    # path('paciente/create/', views.crearPaciente, name='crear_paciente'),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)