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
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = AddEmailToSubscribersForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            try:
                doer = add_email_to_subscribers.delay(email)
                messages.success(request, 'We recived your email. It might not exist in the subscribers table. If so, refresh the page.')
            except Exception as e:
                messages.warning(request, 'Something went wrong! Please try again later.')
        return redirect('home')
