from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from baselogic.models import UserMailLog
from content.models import UserReview
from content.forms import ReviewForm


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
        review = ReviewForm(request.POST)

        if review.is_valid():
            print('True')
            review.save(commit=False)
            review.save()

        messages.add_message(request, messages.INFO, f'Ваш отзыв отправлен\n{request.POST}')
        return redirect('/')

