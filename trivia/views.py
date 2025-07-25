from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Choice, Score
from django.contrib.auth.models import User

# Create your views here.

"""
 Render the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'home.html' template
"""
def home(request):
    return render(request, 'home.html')


"""
Handles the trivia quiz logic: displays questions, processes answers, and records the score.

Args:
        request (HttpRequest): The HTTP request object.

Returns:
        HttpResponse: Renders the quiz page on GET requests, 
                      and renders the results page with the score on POST requests
"""
@login_required
def quiz(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                correct = Choice.objects.get(question=question, correct=True)
                if str(correct.id) == selected:
                    score += 1
        Score.objects.create(user=request.user, score=score)
        return render(request, 'result.html', 
                      {'score': score, 'total': len(questions)})
    return render(request, 'quiz.html', {'questions': questions})

"""
Display the logged-in user's score history.

Retrieves the user's past quiz scores, ordered by date.

Args:
request (HttpRequest): The HTTP request object.

Returns:
HttpResponse: The rendered 'profile.html' template showing the user's scores.
"""
@login_required
def profile(request):
    scores = Score.objects.filter(user=request.user).order_by('-taken_on')
    return render(request, 'profile.html', {'scores': scores})