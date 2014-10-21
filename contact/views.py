from django.shortcuts import render_to_response
from contact.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                '13466582010@126.com',
                ['zhouyuyong@readnovel.com', 'liyanbo@readnovel.com'],
            )
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
            )
    return render_to_response(
        'contact_form.html',
        RequestContext(request, {'form': form})
        )


def thanks(request):
    return HttpResponse("Thanks for your contacting us")
