from django import forms

class bankform(forms.Form):
    fname=forms.CharField(max_length=30)
    psw=forms.CharField(max_length=20)

class bnkf(forms.Form):
    fname=forms.CharField(max_length=30)
    lname=forms.CharField(max_length=30)
    uname=forms.CharField(max_length=30)
    email=forms.EmailField()
    phn=forms.IntegerField()
    img=forms.FileField()
    psw=forms.CharField(max_length=20)
    cpsw=forms.CharField(max_length=20)

# class amount(forms.Form):
#     amountadd=forms.IntegerField()
#     psw1=forms.CharField(max_length=20)

class newsf(forms.Form):
    title=forms.CharField(max_length=20)
    content=forms.CharField(max_length=1000)

class adminf(forms.Form):
    password=forms.CharField(max_length=20)
    username=forms.CharField(max_length=20)

