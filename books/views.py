from django.shortcuts import render

def landing_page (request):
    print((request.COOKIES['sessionid']))
    # print(request.user.is_autenticated)

    return render (request,'landing_page.html')

