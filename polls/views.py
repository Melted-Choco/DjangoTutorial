from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Question

# display the latest few questions
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

# displays a question text, with no results but with a form to vote
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

# displays results for a particular question
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# handles voting for a particular choice in a particular question
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
