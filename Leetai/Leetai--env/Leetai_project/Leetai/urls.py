from django.urls import path
from . import views
# viewsから引き継ぐ設定を、都度やる
from .views import HomepageView,QuestionDetailView

# pathは、関数べースの書き方と、クラスベースの書き方がある（"パス名"、クラス名．as_view())
urlpatterns =[
    path("",HomepageView.as_view()),
    path('question/<int:pk>/',QuestionDetailView.as_view(),name="question_detail")
    
    
]

#なんでquestion.id はエラーなんー