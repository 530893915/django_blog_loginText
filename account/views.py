from django.shortcuts import render

from django.shortcuts import render,reverse
from .models import UserModel
from django.http import HttpResponse,HttpResponseRedirect
import uuid
from .forms import RegistForm

# Create your views here.
def index(request):
    sessionid = request.COOKIES.get("mysessionid", None)
    username = request.session.get(sessionid, None)
    if username:
        html = u'这是主界面,您的用户名是: %s' % username
        return HttpResponse(html)
    else:
        return HttpResponseRedirect(reverse('login'))

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        userModel = UserModel.objects.filter(name=username, password=password).first()
        if userModel:
            # 代表登录成功
            # 1. 给客户端设置cookie
            response = HttpResponseRedirect(reverse('index'))
            sessionid = str(uuid.uuid4())
            response.set_cookie('mysessionid', sessionid)
            # 2. 设置session的值
            request.session[sessionid] = userModel.name
            # 3. 跳转到index页面
            return response
        else:
            return HttpResponse(u'用户名或密码错误')

def regist(request):
    if request.method == 'GET':
        form = RegistForm()
        return render(request, 'regist.html',{'form':form})
    else:
        # 这是post请求
        # 1. 根据用户提交的数据初始化一个表单
        form = RegistForm(request.POST)
        # 2. 验证提交的数据是否合法
        if form.is_valid():
            username = form.cleaned_data.get('username', None)
            password = form.cleaned_data.get('password', None)
            password_repeat = form.cleaned_data.get('password_repeat', None)
            if password == password_repeat:
                user = UserModel(name = username, password=password)
                user.save()
            return HttpResponse("注册成功！")
        else:
            return render(request, 'regist.html', {'errors': form.errors})