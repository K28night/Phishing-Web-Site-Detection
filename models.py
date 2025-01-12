from django.db import models
from django.contrib.auth.models import User


    
class registrationmodel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    confirmpassword=models.CharField(max_length=20,null=True)


class spammodel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category=models.CharField(max_length=20,null=True)
    domain=models.CharField(max_length=20,null=True)
    ip_address=models.CharField(max_length=20,null=True)
    server=models.CharField(max_length=20,null=True)
    malware=models.CharField(max_length=20,null=True)
    spamming=models.CharField(max_length=20,null=True)
    phishing=models.CharField(max_length=20,null=True)
    risk_score=models.CharField(max_length=20,null=True)
    suspicious=models.CharField(max_length=20,null=True)
    domain_rank=models.CharField(max_length=20,null=True)



class reportmodel(models.Model):
    sitename=models.CharField(max_length=20,null=True)
    reason=models.CharField(max_length=20,null=True)


class feedmodel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    email=models.CharField(null=True,max_length=200)  


    feed=models.CharField(max_length=20,null=True)