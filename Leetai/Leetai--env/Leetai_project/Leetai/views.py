from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from Leetai.models import Question,Answer
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy
# class クラス名（親クラス）
class HomepageView(ListView):
    # HTMLを指定する属性
    template_name = 'home.html'
    model = Question
    context_object_name = "Question_lists"
    
class QuestionDetailView (DetailView):
    model = Question
    template_name = 'question_detail.html'
    context_object_name = 'question'
    
class QuestionCreateView(CreateView):
    template_name = "question_form.html"
    model = Question
    fields = "__all__"
    success_url = reverse_lazy("home")
    
class QuestionUpdateView(UpdateView):
    template_name = "question_form.html"
    model = Question
    fields = "__all__"
    success_url = reverse_lazy("home")
    