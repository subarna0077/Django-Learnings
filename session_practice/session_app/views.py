from django.http import HttpResponse
from django.shortcuts import redirect

def set_session(request):
    # Set session data
    request.session['favorite_color'] = 'blue'
    request.session['visits'] = request.session.get('visits', 0) + 1
    return HttpResponse("Session data set! Visit count: {}".format(request.session['visits']))

def get_session(request):
    # Get session data
    favorite_color = request.session.get('favorite_color', 'Not set')
    visits = request.session.get('visits', 0)
    return HttpResponse(f"Favorite Color: {favorite_color}, Visits: {visits}")

def clear_session(request):
    # Clear session data
    request.session.flush()
    return HttpResponse("Session cleared!")
