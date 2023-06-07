from django.urls import path
from . import tests
from . import views
from .views import LikeBase1,LikeBase2,LikeBase3,LikeBase4
from .views import Like1,Like2,Like3,Like4
from .views import search
app_name = 'myapp'
urlpatterns = [
path('', tests.test, name='test'),


path('register/', views.AccountRegistration.as_view(), name='register'),
path('login/', views.Login,name='Login'),
path('logout/', views.Logout, name='Logout'),


path('top/', views.top, name='top'),

path('post/', views.View_post.as_view(), name='post'),
path('post1/', views.View_post1.as_view(), name='post1'),
path('post2/', views.View_post2.as_view(), name='post2'),
path('post3/', views.View_post3.as_view(), name='post3'),
path('post4/', views.View_post4.as_view(), name='post4'),


path('chapter1/', views.View_chapter1, name='chapter1'),
path('chapter2/', views.View_chapter2, name='chapter2'),
path('chapter3/', views.View_chapter3, name='chapter3'),
path('chapter4/', views.View_chapter4, name='chapter4'),


path('result1/',views.View_result1.as_view(),name="result1"),
path('result2/',views.View_result2.as_view(),name="result2"),
path('result3/',views.View_result3.as_view(),name="result3"),
path('result4/',views.View_result4.as_view(),name="result4"),


path('profile/', views.View_profile.as_view(), name='profile'),

path('like_result1/', views.likeresult1.as_view(), name='like_result1'),
path('like_result2/', views.likeresult2.as_view(), name='like_result2'),
path('like_result3/', views.likeresult3.as_view(), name='like_result3'),
path('like_result4/', views.likeresult4.as_view(), name='like_result4'),

path('like1/<int:pk>',Like1.as_view(), name='like1'),
path('like2/<int:pk>',Like2.as_view(), name='like2'),
path('like3/<int:pk>',Like3.as_view(), name='like3'),
path('like4/<int:pk>',Like4.as_view(), name='like4'),


path('search/',search, name='search'),
    

]