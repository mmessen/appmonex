from .models import Equities
from .models import Nis_pos
from django.shortcuts import render, redirect
import sqlite3
from django.contrib.auth.decorators import login_required

@login_required
def index(request): ## muestra el listado de acciones
    equities = Equities.objects.all()
    context = {'equities':equities}
    return render(request, 'app/index.html', context)

@login_required
def niscaly(request):
    posicion = Nis_pos.objects.all()
    context = {'posicion':posicion}
    return render(request, 'app/niscaly.html', context)

@login_required
def posiciones(request):
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    cur.execute('SELECT equity_id, SUM(Cantidad * precio_compra) FROM app_nis_pos GROUP BY equity_id;')
    pos = cur.fetchall()
    cur.execute('SELECT equity_id, SUM(Cantidad * precio_compra) FROM app_nis_pos;')
    total = cur.fetchall()
    con.close()
    context = {'pos':pos,'total':total}
    return render(request, 'app/niscaly_pos.html', context)