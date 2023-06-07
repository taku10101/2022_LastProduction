
from django.views.generic import ListView,CreateView,TemplateView
from django.views.generic.list import ListView
from django.contrib import admin


from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views import View


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#AddAccountForm 
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render, redirect
from .forms import PostForm1
from .forms import PostForm2
from .forms import PostForm3
from .forms import PostForm4

from .models import Account
from .models import PostTable1
from .models import PostTable2
from .models import PostTable3
from .models import PostTable4

from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.shortcuts import render
from django.views.generic import TemplateView 
from .forms import AccountForm 
from django.contrib.auth.decorators import login_required



#ユーザー登録処理

class  AccountRegistration(TemplateView):
    template_name = "register.html"

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["AccountCreate"] = False
        return render(request,"register.html",context=self.params)

    #Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        #フォーム入力の有効検証
        if self.params["account_form"].is_valid() :
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"register.html",context=self.params)
    
    

def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('myapp:top'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません。ログインページに戻ってください")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています。ログインページに戻ってください")
    # GET
    else:
        return render(request, 'login.html')


#ログアウト
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('myapp:Login'))


#ホーム
@login_required
def top(request):
    params = {"UserID":request.user}
    return render(request, "top.html",context=params)


#投稿場所選択
class View_post(LoginRequiredMixin,TemplateView):
    template_name = "post.html"


    
#投稿
class View_post1(LoginRequiredMixin,CreateView):
    template_name = "post1.html"
    model = PostTable1
    fields = ("post_img","post_txt")
    success_url="/result1/"
    
    def form_valid(self, form):
        """投稿ユーザーをリクエストユーザーと紐付け"""
        form.instance.user = self.request.user
        return super().form_valid(form)
    #受け取り
    
    
class View_post2(LoginRequiredMixin,CreateView):
    template_name = "post1.html"
    model = PostTable2
    fields = ("post_img","post_txt")
    success_url="/result2/"
    
    def form_valid(self, form):
        """投稿ユーザーをリクエストユーザーと紐付け"""
        form.instance.user = self.request.user
        return super().form_valid(form)
    #受け取り    
    
    
class View_post3(LoginRequiredMixin,CreateView):
    template_name = "post1.html"
    model = PostTable3
    fields = ("post_img","post_txt")
    success_url="/result3/"
    
    def form_valid(self, form):
        """投稿ユーザーをリクエストユーザーと紐付け"""
        form.instance.user = self.request.user
        return super().form_valid(form)
    #受け取り    
    
    
class View_post4(LoginRequiredMixin,CreateView):
    template_name = "post1.html"
    model = PostTable4
    fields = ("post_img","post_txt")
    success_url="/result4/"

    def form_valid(self, form):
        """投稿ユーザーをリクエストユーザーと紐付け"""
        form.instance.user = self.request.user
        return super().form_valid(form)
    #受け取り    
    
    
    
def View_chapter1(request):
    template_name ="chapter1.html"
    ctx={}
    all_qs= PostTable1.objects.all()
    ctx["object_list"]=all_qs
    return render(request,template_name,ctx)

def View_chapter2(request):
    template_name ="chapter2.html"
    ctx={}
    all_qs= PostTable2.objects.all()
    ctx["object_list"]=all_qs
    return render(request,template_name,ctx)

def View_chapter3(request):
    template_name ="chapter3.html"
    ctx={}
    all_qs= PostTable3.objects.all()
    ctx["object_list"]=all_qs
    return render(request,template_name,ctx)

def View_chapter4(request):
    template_name ="chapter4.html"
    ctx={}
    all_qs= PostTable4.objects.all()
    ctx["object_list"]=all_qs
    return render(request,template_name,ctx)

    
    #profile





class View_profile(LoginRequiredMixin,TemplateView):
    template_name = "profile.html"


class View_result1(LoginRequiredMixin,TemplateView):
    template_name = "result1.html"


class View_result2(LoginRequiredMixin,TemplateView):
    template_name = "result2.html"

class View_result3(LoginRequiredMixin,TemplateView):
    template_name = "result3.html"


class View_result4(LoginRequiredMixin,TemplateView):
    template_name = "result4.html"



class LikeBase1( View):
    model=PostTable1

    def get(self, request, *args, **kwargs):
#記事の特定
        pk = self.kwargs['pk']
        related_post1 = PostTable1.objects.get(pk=pk)
    
    #いいねテーブル内にすでにユーザーが存在する場合   
        if self.request.user in related_post1.like1.all(): 
            #テーブルからユーザーを削除 
            obj = related_post1.like1.remove(self.request.user)
        #いいねテーブル内にすでにユーザーが存在しない場合
        else:
            #テーブルにユーザーを追加                           
            obj = related_post1.like1.add(self.request.user)  
            return obj
        
class LikeBase2( View):
    def get(self, request, *args, **kwargs):
#記事の特定
        pk = self.kwargs['pk']
        related_post2 = PostTable2.objects.get(pk=pk)
    
    #いいねテーブル内にすでにユーザーが存在する場合   
        if self.request.user in related_post2.like2.all(): 
            #テーブルからユーザーを削除 
            obj = related_post2.like2.remove(self.request.user)
        #いいねテーブル内にすでにユーザーが存在しない場合
        else:
            #テーブルにユーザーを追加                           
            obj = related_post2.like2.add(self.request.user)  
            return obj


class LikeBase3(View):
    def get(self, request, *args, **kwargs):
#記事の特定
        pk = self.kwargs['pk']  
        related_post3 = PostTable3.objects.get(pk=pk)
    
    #いいねテーブル内にすでにユーザーが存在する場合   
        if self.request.user in related_post3.like3.all(): 
            #テーブルからユーザーを削除 
            obj = related_post3.like3.remove(self.request.user)
        #いいねテーブル内にすでにユーザーが存在しない場合
        else:
            #テーブルにユーザーを追加                           
            obj = related_post3.like3.add(self.request.user)  
            return obj

class LikeBase4(View):
    def get(self, request, *args, **kwargs):
#記事の特定
        pk = self.kwargs['pk']
        related_post4 = PostTable4.objects.get(pk=pk)
    
    #いいねテーブル内にすでにユーザーが存在する場合   
        if self.request.user in related_post4.like4.all(): 
            #テーブルからユーザーを削除 
            obj = related_post4.like4.remove(self.request.user)
        #いいねテーブル内にすでにユーザーが存在しない場合
        else:
            #テーブルにユーザーを追加                           
            obj = related_post4.like4.add(self.request.user)  
            return obj
        
        
        
        
class Like1(LikeBase1):
    
   def get(self, request, *args, **kwargs):
    #LikeBaseでリターンしたobj情報を継承
        super().get(request, *args, **kwargs)
        return redirect('myapp:like_result1')

class Like2(LikeBase2):
   def get(self, request, *args, **kwargs):
    #LikeBaseでリターンしたobj情報を継承
        super().get(request, *args, **kwargs)
        return redirect('myapp:like_result2')
    

class Like3(LikeBase3):
   def get(self, request, *args, **kwargs):
    #LikeBaseでリターンしたobj情報を継承
        super().get(request, *args, **kwargs)
        return redirect('myapp:like_result3')
    

class Like4(LikeBase4):
   def get(self, request, *args, **kwargs):
    #LikeBaseでリターンしたobj情報を継承
        super().get(request, *args, **kwargs)
        return redirect('myapp:like_result4')
    
    
    
    
class likeresult1(TemplateView):
    template_name= "like_result1.html"
        
class likeresult2(TemplateView):
    template_name= "like_result2.html"   
    
    
class likeresult3(TemplateView):
    template_name= "like_result3.html"
    
class likeresult4(TemplateView):
    template_name= "like_result4.html"
    
    
from .forms import SearchForm



def search(request):
    searchForm = SearchForm(request.GET)
    # searchForm変数に正常なデータがあれば
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword'] # keyword変数にフォームのキーワードを代入
        articles1 = PostTable1.objects.filter(post_txt=keyword) 
        articles2= PostTable2.objects.filter(post_txt=keyword) 
        articles3 = PostTable3.objects.filter(post_txt=keyword) 
        articles4= PostTable4.objects.filter(post_txt=keyword) 
    # それ以外の場合
    else:
        searchForm = SearchForm()   
        articles1 = PostTable1.objects.all()
        articles2 = PostTable2.objects.all()
        articles3 = PostTable3.objects.all()
        articles4 = PostTable4.objects.all()

    context = {
    'articles1': articles1,'articles2': articles2,'articles3': articles3,'articles4': articles4,
    'searchForm': searchForm}
    return render(request, 'search.html', context)



