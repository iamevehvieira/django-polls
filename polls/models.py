from django.db import models
from django.core.exceptions import ValidationError

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
    
    def save(self, user, *args, **kwargs):
        question_user = QuestionUser.objects.filter(user=user, question=self.question).count()
        if question_user > 0:
            raise ValidationError('Não é permitido votar mais de uma vez')
        
        question_user = QuestionUser.objects.create(user=user, question=self.question)
        question_user.save()

        super().save(*args, **kwargs)
    
# Model para criar relacionamento N:N - mantém o voto anônimo, mas registra que votou
class QuestionUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)