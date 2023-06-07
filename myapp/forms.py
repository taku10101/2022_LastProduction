from django.contrib import admin
from .models import PostTable1
from .models import PostTable2
from .models import PostTable3
from .models import PostTable4

from django import forms
from django.urls import reverse_lazy
#
#UserTable　id, password
#PostTable post_img ,post_txt

#ProfileTable icon name(編集画面の追記予定)
#LikeTable like(判定　0,1)

from django.contrib.auth.models import User
from .models import Account

# フォームクラス作成

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm



# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','password')
        # フィールド名指定
        labels = {'username':"ユーザーID"}

        

class PostForm1(forms.ModelForm):
    class Meta:
        model = PostTable1
        fields = ("post_img","post_txt")
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostForm2(forms.ModelForm):
    class Meta:
        model = PostTable2
        fields = ("post_img","post_txt")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class PostForm3(forms.ModelForm):
    class Meta:
        model = PostTable3
        fields = ("post_img","post_txt")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class PostForm4(forms.ModelForm):
    class Meta:
        model = PostTable4
        fields = ("post_img","post_txt")
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
    
    
class SearchForm(forms.Form):
        keyword = forms.CharField(label='', max_length=50,)
        
