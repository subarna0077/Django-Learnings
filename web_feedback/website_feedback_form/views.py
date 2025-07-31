from django.shortcuts import render, redirect
from .forms import WebsiteForm
from .models import WebsiteFormModel


# Create your views here.

def feedback_form(request):
    if(request.method == 'POST'):
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')
    else:
        form = WebsiteForm()  

    return render(request, 'website_feedback_form/feedback_form.html', {'form': form})

 
def thank_you(request):
      return render(request,'website_feedback_form/thank_you.html')

def feedback_list(request):
    feedbacks = WebsiteFormModel.objects.all()
    return render(request, 'website_feedback_form/feedback_list.html', {'feedbacks': feedbacks})
    

