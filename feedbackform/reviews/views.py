from django.shortcuts import render
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
# from .models import Review

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review_form.html", {
        "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect("/thank_you")   
        return render(request, "reviews/review_form.html", {"form":form})


# def review(request):
#     if(request.method == 'POST'):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#            form.save()
#            return HttpResponseRedirect("/thank_you")
#     else:
#         form = ReviewForm()  

    #This below return ensure tha there is always a return no matter the get or post request.
    
#     return render(request, "reviews/review_form.html", {"form":form})

class ThankYouView(TemplateView):
    template_name= "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This works'
        return context

    # def get(self, request):
    #     return render(request, "reviews/thank_you.html")

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=4)
        return data

     
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     singleReview = Review.objects.get(pk=review_id)
    #     context["review"] = singleReview
    #     return context
     