from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    author = models.ForeignKey(
       User, #chave estrangeira vinculada ao usuário
       editable=False, #não permite editar 
       on_delete=models.DO_NOTHING, #não exclui a pergunta se o autor for removido
       null=True, #permite autor NULL para não conflitar com registros já existentes
    )

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text