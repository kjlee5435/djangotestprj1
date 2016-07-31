from django.shortcuts import render, get_object_or_404
from polls.models import Question
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Question

# Create your views here.


def index(request):
    print("index in")
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    print("vote in")
    p = get_object_or_404(Question, pk=question_id)
    print("vote 0")
    
    try:
        print("vote 1")
        print(request.method)
        print("choice {0}".format(request.POST['choice']))
        print("vote 1-1")
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        print("vote 2")

    except(KeyError, Choice.DoesNotExist):
        print("vote3")
        return render(request, 'polls/detail.html', {'question': p, 'error_message': "not selected.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        print("selected")
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
