from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from product.models import *


class ProductForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["name"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_name",
			'id':"prod_name",
			'placeholder':"Product Name"
			})

		self.fields["short"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_short",
			'id':"prod_short",
			'placeholder':"Short Description",
			})
		self.fields["thumb_nail"].widget.attrs.update({
			'required':'',
			'class':"form-control form-choose",
			'type':"file", 
			'name':"prod_thumb",
			'id':"prod_thumb",
			})
		self.fields["sub_category"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_sub_cat",
			'id':"prod_sub_cat",
			'placeholder':"Choose Sub-Category",
			})
		self.fields["brand"].widget.attrs.update({
			'class':"form-control",
			'type':"text", 
			'name':"prod_brand",
			'id':"prod_brand",
			'placeholder':"Product Brand",
			})
		self.fields["description"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_desc",
			'id':"prod_desc",
			})
		self.fields["number"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_number",
			'id':"prod_number",
			'placeholder':"Product Number in Stock"
			})

	class Meta:
		model= Product
		fields=('name','short','sub_category','brand','number','description','thumb_nail')


class VariationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["size"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_size",
			'id':"prod_size",
			'placeholder':"Size of Product"
			})
		self.fields["price"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"number", 
			'name':"prod_price",
			'id':"prod_price",
			'placeholder':"Product Original Price"
			})
		self.fields["dis_price"].widget.attrs.update({
			'class':"form-control",
			'type':"number", 
			'name':"prod_discount",
			'id':"prod_discount",
			'placeholder':"Discount Price Of Product"
			})

	class Meta:
		model= Variation
		fields=('size','price','dis_price')		


class ProductInfoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["ingredients"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"prod_ingr",
			'id':"prod_ingr",
			'placeholder':"Product Ingredients",
			})
		self.fields["prod_date"].widget.attrs.update({
			'class':"form-control",
			'type':"date", 
			'name':"prod_date",
			'id':"prod_date",
			'placeholder':"Product Manufacturing Date",
			})
		self.fields["expiry_date"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"date", 
			'name':"prod_expiry",
			'id':"prod_expiry",
			'placeholder':"Product Expiry Date",
			})

	class Meta:
		model= ProductInformation
		fields=('ingredients','prod_date','expiry_date')		

