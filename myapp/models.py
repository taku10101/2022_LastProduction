from django.db import models
from django.utils import timezone
import uuid
from django.db import models
# ユーザー認証
from django.contrib.auth.models import User

# ユーザー認証



from django.db import models
# ユーザー認証
from django.contrib.auth.models import User

# ユーザーアカウントのモデルクラス
class Account(models.Model):
    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_image = models.ImageField(upload_to="images" )

    def __str__(self):
        return self.user
    
    
class PostTable1(models.Model):
    post_img = models.ImageField(upload_to='images')
    post_txt = models.TextField( blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #like追加
    like1 = models.ManyToManyField(User, related_name='related_post1', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_txt

    
class PostTable2(models.Model):
    post_img = models.ImageField(upload_to='images')
    post_txt = models.TextField( blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like2 = models.ManyToManyField(User, related_name='related_post2', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_txt
        
class PostTable3(models.Model):
    post_img = models.ImageField(upload_to='images')
    post_txt = models.TextField( blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like3 = models.ManyToManyField(User, related_name='related_post3', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_txt  
    
class PostTable4(models.Model):
    post_img = models.ImageField(upload_to='images')
    post_txt = models.TextField( blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like4 = models.ManyToManyField(User, related_name='related_post4', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_txt  

    





