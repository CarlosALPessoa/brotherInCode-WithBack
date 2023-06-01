from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from .models import *
from .serializers import *

def lista_tutores(request):
    res = []
    tutores = Tutores.objects.all()
    for tutor in tutores:
        especializacoes = EspecializacaoTutor.objects.filter(id_tutor=tutor)
        avaliacoes = AvaliacaoTutor.objects.filter(id_tutor=tutor)
        res.append({
            'id_tutor': tutor.id_tutor,
            'nome': tutor.nome,
            'especializacoes': EspecializacaoTutorSerializer(especializacoes, many=True).data,
            'estrelas': [0]*int(sum([avaliacao.nota for avaliacao in avaliacoes])/len(avaliacoes)) if len(avaliacoes) > 0 else [0],
        })
    return render(request, 'brotherInCode/main2.html', {'tutores': res})


def perfil_tutor(request, id_tutor):
    tutor = Tutores.objects.get(id_tutor=id_tutor)
    especializacoes = EspecializacaoTutor.objects.filter(id_tutor=tutor)
    avaliacoes = AvaliacaoTutor.objects.filter(id_tutor=tutor)
    horarios = HorariosTutor.objects.filter(id_tutor=tutor)
    res = {
        'id_tutor': tutor.id_tutor,
        'nome': tutor.nome,
        'sobre': tutor.sobre,
        'especializacoes': EspecializacaoTutorSerializer(especializacoes, many=True).data,
        'estrelas': [0]*int(sum([avaliacao.nota for avaliacao in avaliacoes])/len(avaliacoes)) if len(avaliacoes) > 0 else [0],
        'horarios': HorariosTutorSerializer(horarios, many=True).data,
    }
    
    return render(request, 'brotherInCode/main.html', {'tutor': res})


def perfil_usuario(request):
    user = request.user.id
    try:
        usuario = Alunos.objects.get(id_user=user)
    except:
        usuario = Tutores.objects.get(id_user=user)

    res = {
        'id': usuario.pk,
        'id_user': usuario.id_user,
        'nome': usuario.nome,
        'username': usuario.id_user.username,
        'email': usuario.email,
    }
    
    aluno = Alunos()
    if type(usuario) == type(aluno):
        interesses = InteresseAluno.objects.filter(id_aluno=usuario)
        res['interesses'] = InteresseAlunoSerializer(interesses, many=True).data
    else:
        especializacoes = EspecializacaoTutor.objects.filter(id_tutor=usuario)
        res['sobre'] = usuario.sobre
        res['especializacoes'] = EspecializacaoTutorSerializer(especializacoes, many=True).data
    
    return render(request, 'brotherInCode/perfil.html', {'usuario': res})


def quemSomos(request):
    return render(request, 'brotherInCode/quem somos.html')

def tutorias(request):
    res = []
    tutorias = Tutoria.objects.filter(id_aluno=request.user.id) #+ Tutoria.objects.filter(id_tutor=request.user.id)
    for tutoria in tutorias:
        res.append({
            'id_tutoria': tutoria.id_tutoria,
            'tutor': tutoria.id_tutor,
            'data': tutoria.data,
            'horario': HorariosTutorSerializer(tutoria.id_horario_tutor).data,
            'area_do_conhecimento': tutoria.id_sub_area_conhecimento.nome,
            'link': tutoria.link,
        })
    
    return render(request, 'brotherInCode/tutorias.html', {'tutorias': res})

def quem_somos(request):
    return render(request, 'brotherInCode/quem somos.html')

def login(request):
    return render(request, 'brotherInCode/login.html')

def cadastro(request):
    return render(request, 'brotherInCode/joinUs.html')

class ContasViewSet(viewsets.ModelViewSet):
    queryset = Contas.objects.all()
    serializer_class = ContasSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]



class TutoresViewSet(viewsets.ModelViewSet):
    queryset = Tutores.objects.all()
    serializer_class = TutoresSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class AreaConhecimentoViewSet(viewsets.ModelViewSet):
    queryset = AreaConhecimento.objects.all()
    serializer_class = AreaConhecimentoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class SubareasConhecimentoViewSet(viewsets.ModelViewSet):
    queryset = SubareasConhecimento.objects.all()
    serializer_class = SubareasConhecimentoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class EspecializacaoTutorViewSet(viewsets.ModelViewSet):
    queryset = EspecializacaoTutor.objects.all()
    serializer_class = EspecializacaoTutorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class InteresseAlunoViewSet(viewsets.ModelViewSet):
    queryset = InteresseAluno.objects.all()
    serializer_class = InteresseAlunoSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class HorariosTutorViewSet(viewsets.ModelViewSet):
    queryset = HorariosTutor.objects.all()
    serializer_class = HorariosTutorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class AvaliacaoTutorViewSet(viewsets.ModelViewSet):
    queryset = AvaliacaoTutor.objects.all()
    serializer_class = AvaliacaoTutorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class TutoriaViewSet(viewsets.ModelViewSet):
    queryset = Tutoria.objects.all()
    serializer_class = TutoriaSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    
    def retrieve(self, request, pk=None):
        try:
            tutoria = Tutoria.objects.get(id=pk)
        except:
            return Response({'error': 'Tutoria não encontrada.'}, status=400)
        return Response(TutoriaSerializer(tutoria).data)
    
    
    @action(detail=False, methods=['get'])
    def minhas_tutorias(self, request, pk=None):
        try:
            aluno = Alunos.objects.get(id_user=request.user)
        except:
            return Response({'error': 'Usuário não é um aluno.'}, status=400)
        tutorias = Tutoria.objects.filter(id_aluno=aluno)
        return Response(TutoriaSerializer(tutorias, many=True).data)
