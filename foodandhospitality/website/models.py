from django.db import models
from django.contrib.auth.models import User, auth
from django.forms import ModelForm

# Create your models here.


class uprofile(models.Model):
    meta = models.ForeignKey(User, on_delete=models.CASCADE)
    profileimg = models.ImageField(upload_to='profileimgs/')
    phone_no = models.BigIntegerField()
    address = models.TextField(max_length=300)


class uprofileform(ModelForm):
    class Meta:
        model = uprofile
        fields = ['profileimg', 'phone_no', 'address']
