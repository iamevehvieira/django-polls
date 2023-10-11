from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('sobre/', views.sobre, name = 'sobre'),
    path('pergunta/<int:question_id>', views.exibe_questao, name='exibe_questao'),
    path('perguntas', views.ultimas_perguntas, name='ultimas_perguntas'),
    path('perguntas/list', views.ultimas_perguntas, name='polls_list'),
    path('pergunta/add', views.QuestionCreateView.as_view(), name="poll_add"),
    path('pergunta/<int:pk>/edit', views.QuestionUpdateView.as_view(), name="poll_edit"),
    path('pergunta/<int:pk>/delete', views.QuestionDeleteView.as_view(), name="poll_delete"),
    path('pergunta/<int:pk>/show', views.QuestionDetailView.as_view(), name="poll_show"),
    path('pergunta/all', views.QuestionListView.as_view(), name="polls_all"),
    path('about-us', views.SobreTemplateView.as_view(), name="about_page"),
    path('pergunta/<int:pk>/alternativa/add', views.ChoiceCreateView.as_view(), name="choice_add"),
    path('alternativa/<int:pk>/edit', views.ChoiceUpdateView.as_view(), name="choice_edit"),
    path('alternativa/<int:pk>/delete', views.ChoiceDeleteView.as_view(), name="choice_delete"),
] 