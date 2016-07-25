from django.shortcuts import render, get_object_or_404
from polls.models import Question
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Question

# Create your views here.


def index(request):
	latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
	context = {'latest_quesion_list': latest_question_list}
	return render(request, 'poll/index.html', context)

def detail(request, question_id):
	question == get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
	p = get_obejct_or_404(Question, pk = question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {'question': p, 'error_message': "not selected.",})
	else:
		seleced_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})
