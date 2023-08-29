from django.views.generic.edit import CreateView, UpdateView

from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from polls.models import Question, Choice

from django.http import HttpResponse

# Create your views here.

def index (request):
    context = {'titulo': 'Página Principal'}
    return render(request, 'home.html', context)

def sobre (request):
    return HttpResponse('Olá, este é um app de enquete')

def exibe_questao(request, question_id):
    question = Question.objects.get(id=question_id)

    if question is not None:
        #questao.question_text
        return HttpResponse(f'{question.question_text}')
    
    return HttpResponse('Não existe questão a exibir')

def ultimas_perguntas(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    #return render(request, 'polls/perguntas.html', context)
    return render(request, 'perguntas_recentes.html', context)
    
class QuestionCreateView(CreateView):
    model = Question
    template_name = 'polls/question_form.html'
    fields = ('question_text', 'pub_date', )
    success_url = reverse_lazy('polls_list')
def get_context_data(self, **kwargs):
    context = super(QuestionCreateView, self).get_context_data(**kwargs)
    context['form_title'] = 'Criando uma pergunta'
    return context

class QuestionUpdateView(UpdateView):
    model = Question
    template_name = 'polls/question_form.html'
    fields = ('question_text', 'pub_date', )
    success_url = reverse_lazy('polls_list')
def get_context_data(self, **kwargs):
    context = super(QuestionUpdateView, self).get_context_data(**kwargs)
    context['form_title'] = 'Editando a pergunta'
    return context