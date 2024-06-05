from django.urls import path
from . import views
# viewsから引き継ぐ設定を、都度やる
from .views import HomepageView,QuestionDetailView,QuestionCreateView,QuestionUpdateView

# pathは、関数べースの書き方と、クラスベースの書き方がある（"パス名"、クラス名．as_view())
urlpatterns =[
    path("",HomepageView.as_view(),name="home"),
    path('question/<int:pk>/',QuestionDetailView.as_view(),name="question_detail"),
    path('create-Question/',QuestionCreateView.as_view(),name="create_Question"),
    path('edit_question/<int:pk>/',QuestionUpdateView.as_view(),name="edit_question"),
    
]

#なんでquestion.id はエラーなんー