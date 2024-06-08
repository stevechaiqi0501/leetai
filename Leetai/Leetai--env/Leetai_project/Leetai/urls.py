from django.urls import path
from . import views
# viewsから引き継ぐ設定を、都度やる
from .views import HomepageCommonView,QuestionDetailView,QuestionCreateView,QuestionUpdateView,QuestionDeleteView,questionLoginview,MyHomepageView


from django.contrib.auth.views import LogoutView
# pathは、関数べースの書き方と、クラスベースの書き方がある（"パス名"、クラス名．as_view())
urlpatterns =[
    path("",HomepageCommonView.as_view(),name="home"),
    path('question/<int:pk>/',QuestionDetailView.as_view(),name="question_detail"),
    path('create-Question/',QuestionCreateView.as_view(),name="create_Question"),
    path('edit_question/<int:pk>/',QuestionUpdateView.as_view(),name="edit_question"),
    path('delete_question/<int:pk>',QuestionDeleteView.as_view(),name="delete_question"),
    path('login/',questionLoginview.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page="login"),name="logout"),
    
    path('myhome',MyHomepageView.as_view(),name='myhome')
    
    
]

#負けんな