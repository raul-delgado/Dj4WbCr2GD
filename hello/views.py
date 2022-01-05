from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic
import logging


def owner(request):
    return HttpResponse("Hello, world. 8eb7be5a is the polls owner.")

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)



logger = logging.getLogger(__name__)

# Create your views here.

def helloworld(request):
    logging.error('Hello world DJ4E in the log...')
    print('Hello world DJ4E in a print statement...')
    response = HttpResponse("""<html><body><p>Hello world DJ4E in HTML</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>""")
    response.set_cookie('dj4e_cookie', '4badf6fc', max_age=1000)
    #response.set_cookie('dj4e_cookie', 42, max_age=1000)
    return HttpResponse(response)

# https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/',
#     domain=None, secure=None, httponly=False, samesite=None)
def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    resp = HttpResponse('In a view - the zap cookie value is '+str(oldval))
    if oldval :
        resp.set_cookie('zap', int(oldval)+1) # No expired date = until browser close
    else :
        resp.set_cookie('zap', 42) # No expired date = until browser close
    resp.set_cookie('sakaicar', 42, max_age=1000) # seconds until expire
    return resp

# https://www.youtube.com/watch?v=Ye8mB6VsUHw

def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    return resp
