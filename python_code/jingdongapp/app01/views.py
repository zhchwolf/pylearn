from django.shortcuts import render

# Create your views here.
def handle_form(request):
    print(request)
    render(request, "index.html")
