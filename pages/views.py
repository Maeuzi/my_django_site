from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("<h1>Hi its sweta nancy, this is my first  website </h1>")