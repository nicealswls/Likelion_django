from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(reqeust):
    sentence = reqeust.GET['sentence']

    wordList = sentence.split()

    return render(reqeust, "result.html", {'fulltext':sentence, 'count':len(wordList), "wordList":wordList})              
