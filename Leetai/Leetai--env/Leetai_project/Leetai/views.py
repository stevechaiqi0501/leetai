from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from Leetai.models import Question,Answer
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
# class クラス名（親クラス）
class HomepageCommonView(ListView):
    # HTMLを指定する属性
    template_name = 'home.html'
    model = Question
    context_object_name = "Question_lists"
    
class MyHomepageView(LoginRequiredMixin,ListView):
    template_name = 'myhome.html'
    model = Question
    context_object_name = "Question_lists"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['Question_lists']= context["Question_lists"].filter(user=self.request.user)
        return context
    
class QuestionDetailView (DetailView):
    model = Question
    field = "__all__"
    template_name = 'question_detail.html'
    context_object_name = 'question'
    
    
    
class QuestionCreateView(LoginRequiredMixin,CreateView):
    template_name = "question_form.html"
    model = Question
    fields = "__all__"
    success_url = reverse_lazy("home")
    
class QuestionUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "question_form.html"
    model = Question
    fields = "__all__"
    success_url = reverse_lazy("home")
    
class QuestionDeleteView(LoginRequiredMixin,DeleteView):
    model = Question
    fields = "__all__"
    success_url = reverse_lazy("home")
    context_object_name = "question"
    
class questionLoginview(LoginView):
    fields = "__all__"
    template_name = "login.html"
    
    def get_success_url(self):
        return reverse_lazy("home")
    