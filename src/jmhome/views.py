import pathlib
from django.shortcuts import render
from visits.models import PageVisits

def home_page_view(request,*args,**kwargs):
    qs= PageVisits.objects.all()
    page_qs = PageVisits.objects.filter(path=request.path)
    try:
        percent=(page_qs.count()*100.0)/qs.count()
    except:
        percent=0

    my_title = "Home page"
    my_context = {
        "page_title": my_title,
        "page_vist_count":page_qs.count(),
        "percent":percent,
        "total_visit_count":qs.count(),
    }
    PageVisits.objects.create(path=request.path)
    html_template = "home.html"
    return  render(request, html_template, my_context)


def about_page_view(request,*args,**kwargs):
    my_title = "About page"
    qs = PageVisits.objects.all()
    page_qs = PageVisits.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0
    my_context = {
        "page_title": my_title,
        "page_vist_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count(),
    }
    PageVisits.objects.create(path=request.path)
    html_template = "home.html"
    return render(request, html_template, my_context)
