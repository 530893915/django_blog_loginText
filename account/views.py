from django.shortcuts import render

from django.shortcuts import render,reverse
from .models import UserModel
from django.http import HttpResponse,HttpResponseRedirect
import uuid
# Create your views here.
def index(request):
    def index(request):
        sessionid = request.COOKIES.get("mysessionid", None)
        username = request.session.get(sessionid, None)
        if username:
            html = u'这是主界面,您的用户名是: %s' % username
            return HttpResponse(html)
        else:
            return HttpResponseRedirect(reverse('login'))

def login(request):
    pass

def regist(request):
    pass