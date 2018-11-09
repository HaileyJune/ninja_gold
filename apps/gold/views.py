from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if not 'gold' in request.session:
        request.session['activity'] = ''
        request.session['gold'] = 0


    return render(request, "gold/index.html")

def process_money(request):
    if request.POST['location'] != 'casino':
        if request.POST['location'] == 'farm':
            earned = random.randint(10, 20)
        elif request.POST['location'] == 'cave':
            earned = random.randint(5, 10)
        elif request.POST['location'] == 'home':
            earned = random.randint(2, 5)

        request.session['gold'] += earned
        string = (f"<p>You earned {earned} gold at the {request.POST['location']}.</p>")
        request.session['activity'] = ''.join((string, request.session['activity']))

    else:
        earned = random.randint(-50, 50)
        request.session['gold'] += earned
        if earned > 0:
            string = (f"<p>You made {earned} gold at the {request.POST['location']}.</p>")
            request.session['activity'] = ''.join((string, request.session['activity']))
        elif earned < 0:
            string = (f"<p style='color: red'>You lost {earned} gold at the {request.POST['location']}.</p>")
            request.session['activity'] = ''.join((string, request.session['activity']))
        else:
            string = (f"<p style='color: blue'>You didn't make or lose anything at the {request.POST['location']}.</p>")
            request.session['activity'] = ''.join((string, request.session['activity']))

    return redirect('/')