from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from Leetai.models import Question,Answer
from django.views.generic.detail import DetailView
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