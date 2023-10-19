from django.db import models




class bnkm(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    uname=models.CharField(max_length=30)
    email=models.EmailField()
    phn=models.IntegerField()
    img=models.FileField()
    psw=models.CharField(max_length=20)
    balance=models.IntegerField()
    acc_number=models.IntegerField()      
    def __str__(self):
        return self.uname

class addamount(models.Model):
    uid=models.IntegerField()
    amount2=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.uid

class widamount(models.Model):
    uid=models.IntegerField()
    amount1=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.uid



class newsm(models.Model):
    title=models.CharField(max_length=30)
    content=models.CharField(max_length=1000)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title


class wishlist(models.Model):
    uid=models.IntegerField()
    newsid=models.IntegerField() # prduct id in the news
    title=models.CharField(max_length=20)
    content=models.CharField(max_length=500)
    date=models.DateField()  #autonow will not be used bcz it is for wshlist
    def __str__(self):
        return self.title

