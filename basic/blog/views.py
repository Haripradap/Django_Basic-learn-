from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse("hello world, you are at blog index")

def detail(request, post_id):
    return HttpResponse(f"this is a details page of the blog page and id is {post_id}")

def old_url_redirect(request):
    return redirect(reverse('Blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new url")