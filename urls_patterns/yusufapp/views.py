from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	# print(dir(request))
	return HttpResponse('Hello world')

def about(request):
	return HttpResponse ('<h1>test rejim</h1>')


def yusuf(request):
	return HttpResponse('<h2>Yusufdev</h2>')
