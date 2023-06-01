from rest_framework import routers

from .views import *

routerBrotherInCode = routers.DefaultRouter()
routerBrotherInCode.register(r'contas', ContasViewSet)
routerBrotherInCode.register(r'tutores', TutoresViewSet)
routerBrotherInCode.register(r'alunos', AlunosViewSet)
routerBrotherInCode.register(r'areaconhecimento', AreaConhecimentoViewSet)
routerBrotherInCode.register(r'subareasconhecimento', SubareasConhecimentoViewSet)
routerBrotherInCode.register(r'especializacaotutor', EspecializacaoTutorViewSet)
routerBrotherInCode.register(r'interessealuno', InteresseAlunoViewSet)
routerBrotherInCode.register(r'horariostutor', HorariosTutorViewSet)
routerBrotherInCode.register(r'avaliacaotutor', AvaliacaoTutorViewSet)
routerBrotherInCode.register(r'tutoria', TutoriaViewSet)

#By Carlos
from django.contrib import admin
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('Home/', home, name='main2'),
    path('PerfilTutor/', perfil_tutor, name= 'main'),
    path('QuemSomos/', quemSomos, name='quem somos'),
    path('Tutorias/', tutorias, name = 'tutorias'),
    path('Perfil/', perfil_usuario, name="perfil"),
    path('Login/', login, name= 'login'),
    path('JoinUs/', cadastro, name='joinUs')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
