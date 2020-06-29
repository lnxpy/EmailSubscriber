from .models import Subscribers
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import AddEmailToSubscribersForm
from .tasks import add_email_to_subscribers, send_email_to_all


class HomePage(View):
    template_name = 'core/index.html'
    model = Subscribers
    form = AddEmailToSubscribersForm()

    def get(self, request):
        context = {
            'form': self.form,
            'subscribers': self.model.objects.all(),
        }
        #send_email_to_all.delay()
        return render(request, self.template_name, context=context)

    def post(self, request):
        email = request.POST['email']
        try:
            add_email_to_subscribers.delay(email)
            messages.info(self.request, 'Your email has been sent to us. It might not be seen in the subscribers table. If so, try to refresh the page.')
        except:
            messages.warning(self.request, 'Something went wrong! Please try again later.')
        return redirect('home')
