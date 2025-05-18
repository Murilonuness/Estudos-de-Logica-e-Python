from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.dateparse import parse_datetime

def index(request):
    minutes, seconds = get_remaining_time(request)
    return render(request, 'timerapp/index.html', {
        'minutes': str(minutes).zfill(2),
        'seconds': str(seconds).zfill(2),
    })

def start_timer(request):
    segundos_restantes = request.session.get('seconds', 0)
    request.session['end_time'] = str(timezone.now() + timezone.timedelta(seconds=segundos_restantes))
    request.session['last_updated'] = str(timezone.now())  # <-- ESSA LINHA É IMPORTANTE
    request.session['running'] = True
    return redirect('index')

def pause_timer(request):
    request.session['running'] = False
    return redirect('index')

def edit_timer(request):
    if request.method == 'POST':
        valor = request.POST.get('minutos')
        if valor and valor.isdigit():
            minutos = int(valor)
        else:
            minutos = 0
        request.session['seconds'] = minutos * 60
        request.session['running'] = False
    return redirect('index')

def get_remaining_time(request):
    if 'seconds' not in request.session:
        request.session['seconds'] = 0
        request.session['running'] = False
        request.session['last_updated'] = str(timezone.now())

    if request.session.get('running'):
        last = parse_datetime(request.session['last_updated'])
        now = timezone.now()
        elapsed = int((now - last).total_seconds())
        remaining = max(0, request.session['seconds'] - elapsed)
        request.session['seconds'] = remaining
        request.session['last_updated'] = str(now)
    else:
        remaining = request.session['seconds']

    minutes = remaining // 60
    seconds = remaining % 60
    return minutes, seconds

def fullscreen_view(request):
    minutes, seconds = get_remaining_time(request)
    return render(request, 'timerapp/fullscreen.html', {
        'minutes': str(minutes).zfill(2),
        'seconds': str(seconds).zfill(2),
    })

