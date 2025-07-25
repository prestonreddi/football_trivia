from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    """
    Represents a trivia question.

    Attributes:
        text (str): The text content of the question.
        
    """
    # Question text
    text = models.CharField(max_length=255)
    # Display question.
    def __str__(self):
        return self.text


class Choice(models.Model):
    """
    Model for choices
    """
    # Related question.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Choice text.
    text = models.CharField(max_length=255)
    # Marks if correct.
    correct = models.BooleanField(default=False)
    # Display choice
    def __str__(self):
        return self.text

  
class Score(models.Model):
    """
    Model to store the quiz score for each user.
    """
    # User who took quiz
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Score value.
    score = models.IntegerField()
    # Time when score recorded.
    taken_on = models.DateTimeField(auto_now_add=True)