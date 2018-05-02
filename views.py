from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import string, random

def homePageView(request):
    Strings = ["Bad Doggie", "Tick tock is bad", "I dont eat all time, but Doggie calls me pig, GRR", "Doggie is LOVE","Doggie sometimes talk bad, :P ", "Tick tock sometimes is real ticking bomb, dont know when he will explode", "Doggie is very good", "Best Doggie", "Doggie Teaches <3", "Bestest :P <3"];
    #random_string = {"RandomString" : (random.choice(Strings))}
    #print(random_string)
    return HttpResponse(random.choice(Strings))
