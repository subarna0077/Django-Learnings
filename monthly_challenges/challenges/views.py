from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


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
    "december": "Reflect on your achievements this year",
}

# Create your views here.

def index(request):
    months = list(challenges_dict.keys())
    list_items = ""

    for month in months:
        month_path = reverse('month-challenge', args=[month]) 
        list_items += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenges_by_number(request, month):
    months = list(challenges_dict.keys())

    if(month > len(months)):
        return HttpResponse('Months not found')
    forward_month = months[month-1]

    redirect_path = reverse("month-challenge", args=[forward_month])
    return HttpResponseRedirect(redirect_path)



def monthly_challenges(request, month):
    challenge_text = challenges_dict.get(month)
    if challenge_text:
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    else:
        return HttpResponse("This month is not supported.", status=404)
