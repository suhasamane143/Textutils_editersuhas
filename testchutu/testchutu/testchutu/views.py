#i have created this file-suhas
#code for url, about, index
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    smallcaps = request.POST.get('smallcaps', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    newlineremover= request.POST.get('newlineremover','off')
    charcounter = request.POST.get('charcounter', 'off')
    if removepunc =="on":
        punctutations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctutations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctutations','analyzed_text':analyzed}
        djtext=analyzed
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed+char.upper()
        params={'purpose':'Changed to uppercase','analyzed_text':analyzed}
        djtext=analyzed
    if (smallcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Changed to lowercase', 'analyzed_text': analyzed}
        djtext=analyzed
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'removed newlines', 'analyzed_text': analyzed}
        djtext=analyzed
    if(charcounter == "on"):
        analyzed = "The no.of character are:"+str(len(djtext))
        params = {'purpose': 'charcounter', 'analyzed_text': analyzed}
        djtext=analyzed
    if(removepunc !="on" and newlineremover!="on" and fullcaps!="on" and smallcaps!="on" and extraspaceremover!="on" and charcounter!="on"):
        return HttpResponse("Please select the any operation and try again...")
    return render(request, 'analyze.html', params)




