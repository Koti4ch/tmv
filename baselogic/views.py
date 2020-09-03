from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.core.mail import send_mail, BadHeaderError
from baselogic.models import UserMailLog
from django.contrib import messages
# Create your views here.


class FormHendler(View):
    def post(self, request):
        subject = 'Сообщение от {}'.format(request.POST.get('cf-name', ''))
        message = request.POST.get('cf-message', '')
        from_email = request.POST.get('cf-email', '')
        if subject and message and from_email:
            try:
                maillog = UserMailLog()
                maillog.sendername = subject
                maillog.sendermail = from_email
                maillog.mailtext = message
                maillog.save()

                send_mail(subject, message, from_email, ['dkt324@yandex.ru'])
            except BadHeaderError:
                messages.add_message(request, messages.INFO, 'Invalid header found.')
                return redirect('/')
            messages.add_message(request, messages.INFO, 'Сообщение отправлено.')
        return HttpResponseRedirect('/')



class SendReviewView(View):
    def post(self, request):
        print(request)
