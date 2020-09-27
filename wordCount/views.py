from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'hithere': 'This is me'})

def order(request):
    return HttpResponse('Order Placed')

def analysis(request):
    vowel_count = 0
    consonants_count = 0
    most_used_word = ""
    most_used_count = 0
    fullText = request.GET['fullText']

    listOfWords = fullText.split()
    word_Dictionary = {}
    vowelString = 'aeiouAEIOU'
    consonantString = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    symbol_count = 0
    for word in listOfWords:
        if word.lower() in word_Dictionary:
            #add to the count
            word_Dictionary[word.lower()] += 1
        else:
            word_Dictionary[word.lower()] = 1
    sorted(word_Dictionary.items(), key=operator.itemgetter(1), reverse=True)
    for word in word_Dictionary:
        if word_Dictionary[word.lower()] >= most_used_count:
            most_used_word = word.lower()
            most_used_count = word_Dictionary[word.lower()]

        for letter in word:
            if letter in vowelString:
                vowel_count += 1
            elif letter in consonantString:
                consonants_count += 1
            else:
                symbol_count += 1

    return render(request, 'analysis.html', {'fullText': fullText,
    'list': listOfWords, 'count': len(listOfWords),
    'Dictionary': word_Dictionary.items(), 'vowels': vowel_count, 'consonants':consonants_count,
    'most_used_word' : most_used_word, 'most_used_count': most_used_count, 'symbols': symbol_count})

def about(request):
    return render(request, 'about.html')
