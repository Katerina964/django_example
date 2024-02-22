from django.http import HttpResponse
from example_app.models import Choice


def index(request):
   
    (Choice(choice_text="What's new?", votes=1)).save()
    return HttpResponse("Hello, world WITH LOVE")
