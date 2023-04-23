from asyncio import mixins

from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import generics, viewsets

from .models import Main
from .serializers import MainSerializer


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render(request, 'main/index.html', data)

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'main/contact.html'
    success_url = reverce_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')




def about(request):
    return render(request, 'main/index.html')


class DataMixin:
    pass


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

def logoutUser(request):
    logout(request)
    return redirect('login')


class Main:
    pass

class GenericViewSet:
    pass


class IsAuthenticatedOrReadOnly:
    pass

class IsAdminUser:
    pass


class MainAPIList(generics.ListCreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class MainAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer





class MainAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
    permission_classes = (IsAdminUser, )





#class MainViewSet(mixins.CreateModelMixin,
#                 mixins.RetrieveModelMixin,
#                 mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,
#                 mixins.ListModelMixin,
#                 GenericViewSet):
#   queryset = Main.objects.all()
#   serializer_class = MainSerializer






















