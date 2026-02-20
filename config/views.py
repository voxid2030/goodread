# from django.http import HttpResponse

# def landing_page(request):
#     return HttpResponse(f"Django is working: {request.META['HTTP_USER_AGENT']}")
from django.shortcuts import render
def landing_page (request):
    
    # print(request.user.is_autenticated)

    return render (request,'landing_page.html')