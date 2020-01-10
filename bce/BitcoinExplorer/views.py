from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    latest_question_list = ["1", "2", "suka"]
    template = loader.get_template('BitcoinExplorer/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'BitcoinExplorer/be.html', {})

def blockExplorer(request):
	context = {}
	return render(request, 'BitcoinExplorer/be.html', context)