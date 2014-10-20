from django.shortcuts import render_to_response
from django.http import Http404
import datetime

# Create your views here.


from django.http import HttpResponse


def hello(reques):
    return HttpResponse("Hello world")


def current_url_view(request):
    return HttpResponse("Welcome to the page at %s" % request.body)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    return render_to_response(
        'hours_ahead.html',
        {
            'hour_offset': offset,
            'next_time': dt
        }
    )


def display_meta(request):
    values = request.META.items()
    values = sorted(values)
    return render_to_response('meta.html', {'alist': values})


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def search_form(request):
    return render_to_response('search_form.html')


#def search(request):
#    if 'q' in request.GET:
#        message = 'You searched for : %r' % request.GET['q']
#    else:
#        message = 'You submitted an empty form.'
#    return HttpResponse(message)
