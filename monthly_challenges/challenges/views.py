from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

challenges_dict = {
    "january": "Eat no meat for entire month",
    "february": "Learn Django for 1 hour every day",
    "march": "Read a book every week",
    "april": "Go for a walk every morning",
    "may": "Practice meditation daily",
    "june": "Write a journal entry every night",
    "july": "Drink 2 liters of water every day",
    "august": "Try a new recipe each week",
    "september": "Limit social media to 30 minutes a day",
    "october": "Do 20 push-ups every day",
    "november": "Learn a new programming concept weekly",
    "december": None,
}

# Create your views here.

def index(request):
    months = list(challenges_dict.keys())
    return render(request, "challenges/index.html" , {
        "months": months
    })

def monthly_challenges_by_number(request, month):
    months = list(challenges_dict.keys())

    if(month > len(months)):
        return HttpResponse('Months not found')
    forward_month = months[month-1]

    redirect_path = reverse("month-challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)



def monthly_challenges(request, month):
   challenge_text = challenges_dict.get(month)

   if challenge_text is None:
        response_data = render_to_string("404.html")
        return HttpResponse(response_data, status=404)

   try:
        response_data = render(request,"challenges/challenge.html", {'text': challenge_text, "month": month})
        return response_data
   except:
       raise Http404()
