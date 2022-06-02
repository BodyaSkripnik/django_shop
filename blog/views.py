from itertools import product
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import RegisterUserForm,LoginUserForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from .models import Category,Product


def homepage(request):
    categorys = Category.objects.all()
    return render(request, 'blog/homepage.html',{'categorys':categorys})
def get_categorys(request,category_id):#принимаем category_id с urls.py
    print(category_id)
    products = Product.objects.filter(available = True,category = category_id)#фильтруем по активным и по category_id
    print(product)
    return render(request, 'blog/get_categorys.html',{'products':products})

    


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'blog/login.html'

    def get_success_url(self):
        return reverse_lazy('homepage')


def logout_user(request):
    logout(request)
    return redirect('login')