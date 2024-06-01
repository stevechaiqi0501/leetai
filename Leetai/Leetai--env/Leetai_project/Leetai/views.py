from django.shortcuts import render
from django.views.generic import TemplateView

# class クラス名（親クラス）
class HomepageView(TemplateView):
    # HTMLを指定する属性
    template_name = 'home.html'


