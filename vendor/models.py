from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.utils.timezone import now
from main.models import *
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()





# Create your models here.

class Vendor(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=200, unique=True)
	image=models.ImageField(upload_to="vendor", storage=gd_storage)
	description = models.TextField()
	address = models.CharField(max_length=300)
	phone = PhoneNumberField(blank=True, null=True)
	email = models.EmailField()
	avg_ratings = models.IntegerField(default=0, blank=True, null=True)
	accept_terms = models.BooleanField(default=True)
	date = models.DateTimeField(auto_now_add=True)
	approve = models.BooleanField(default=False)

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" height="50" />'%(self.image.url))

	def get_absolute_url(self):
            return f'/vendor/{self.name}'		

	def __str__(self):
		return self.name

class VendorToken(models.Model):
	vendor= models.OneToOneField(Vendor,on_delete=models.CASCADE)
	token = models.CharField(max_length=150)

	def __str__(self):
		return self.vendor.name

class VendorPayment(models.Model):
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
	bank = models.CharField(max_length=50)
	acct_no = models.IntegerField()
	acct_name = models.CharField(max_length=50)

	def __str__(self):
		return self.vendor.name


RATING=(
    ("1",'1 Star'),
    ("2",'2 Stars'),
    ("3",'3 Stars'),
    ("4",'4 Stars'),
    ("5",'5 Stars'),
)

class VendorReview(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
	text=models.TextField()
	rating=models.IntegerField(choices=RATING,default=1)
	date=models.DateTimeField(default=now)

	def __str__(self):
		return self.user.username


class VendorWallet(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    last_withdrawal_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
    	return f'{self.vendor.name} Wallet'


class VendorPayout(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bank = models.ForeignKey(VendorPayment,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(default=now)  

    def __str__(self):
    	return self.vendor.name  
