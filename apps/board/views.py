from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

def index(request):
	# del request.session['g_point']
	# del request.session['h_point']
	# del request.session['r_point']
	# del request.session['s_point']
	# del request.session['record']
	if 'g_point' not in request.session:
		request.session['g_point'] =0

	if 'h_point' not in request.session:
		request.session['h_point'] =0

	if 'r_point' not in request.session:
		request.session['r_point'] =0

	if 's_point' not in request.session:
		request.session['s_point'] =0
	if 'record' not in request.session:
		request.session['record'] = list()

	return render(request, 'board/index.html')
def process_point(request):
	house = str(request.POST['house'])
	point = int(request.POST['point'])
	if point < 0:
		message = house + " looses the point... " +str(point) +" points are taken out of " + house +"."
		color = "red"
	else:
		message = house + " Scores! " +str(point) + " points to the " + house + "!"
		color = "green"

	if house == 'Gryffindor':
		request.session['g_point'] += point

	if house == 'Hufflepuff':
		request.session['h_point'] += point

	if house == 'Ravenclaw':
		request.session['r_point'] += point

	if house == 'Slytherin':
		request.session['s_point'] += point
	
	request.session['record'].insert(0,message)
	request.session['color'] = color
	m = max([request.session['g_point'], request.session['h_point'], request.session['r_point'], request.session['s_point']])
	
	if m == request.session['g_point']:
		request.session['winner'] = "Gryffindor"
	if m == request.session['h_point']:
		request.session['winner'] = "Hufflepuff"
	if m == request.session['r_point']:
		request.session['winner'] = "Ravenclaw"
	if m == request.session['s_point']:
		request.session['winner'] = "Slytherin"

	return HttpResponseRedirect('/')
