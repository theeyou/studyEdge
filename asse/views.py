from django.shortcuts import render
from django.http import HttpResponse


def index(request):
 #   return HttpResponse("Hello, world. You're at the poll index.")	
# Create your views here.
	return render(request, 'asse/index.html')
	
def result(request):
	s=request.GET.get('q')
	wordlist=[
	"maverick",
    "ranger",
    "rocket",
    "chicago",
    "bear",
    "wizard",
    "seattle",
    "atlanta",
    "miami",
    "austin",
    "boston",
    "pittsburgh",
    "heat",
    "saint",
    "hawk",
    "king"
	]
	slist=s.split(' ')
	nlist=s.split(' ')
	for i in range(0, len(nlist)):
		for va in wordlist:
			slist[i]=slist[i].replace(va,len(va)*'*')
	for i in range(0, len(nlist)):
		if slist[i]==len(nlist[i])*'*':
			nlist[i]=slist[i]
	ret=''
	for i in range(0, len(nlist)):
		ret=ret+nlist[i]+' '
	return  HttpResponse(ret)	