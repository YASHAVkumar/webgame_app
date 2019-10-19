from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.conf.urls.static import static
import random
# Create your views here.

def index(request):
    return render(request, 'home.html')
def score(request):
    val = request.GET.get('Player')

    exit = 0
    win1 = '_'
    comp = '_'
    equal='_'
    y='NONE'
    print("PLAYER VALUE ", val)
    x = random.randrange(1, 4)

    if x == 1:
        print("COMPUTER VALUE Stone")
        y="STONE"
    elif x == 2:
        print("COMPUTER VALUE Paper")
        y="PAPER"
    else:
        print("COMPUTER VALUE Scissor")
        Y="SCISSOR"
    if val == "STONE" and x == 1:
        print("Draw")
        equal="DRAW"
    elif val == "STONE" and x == 2:
        print("Computer won")
        comp = "COMPUTER WON"
    elif val == "STONE" and x == 3:
        print("Player won")
        win1 = "YOU WON"
    elif val == "PAPER" and x == 2:
        print("Draw")
        equal="DRAW"
    elif val == "PAPER" and x == 3:
        print("computer won")
        comp = "COMPUTER WON"
    elif val == "PAPER" and x == 1:
        print("player won")
        win1 = "YOU WON"
    elif val == "SCISSOR" and x == 3:
        print("Draw")
        equal="DRAW"
    elif val == "SCISSOR" and x == 1:
        print("computer won")
        comp = "COMPUTER WON"
    elif val == "SCISSOR" and x == 2:
        print("player won")
        win1 = "YOU WON"

    print("PLAYER WINS ", win1)
    print("COMPUTER WINS ", comp)
    return render(request, 'score.html', {'win1':win1,'val':val, 'comp':comp,'y':y,'equal':equal})

