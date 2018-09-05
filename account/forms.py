#coding:utf8

from django import forms

class RegistForm(forms.Form):
	username = forms.CharField(required=True,max_length=10,min_length=6,error_messages={'min_length':u'hello zunzun.'}) # 没有这些参数:null=True,blank=True
	password = forms.CharField(max_length=10,error_messages={'required':u'密码不能少'})
	password_repeat = forms.CharField(max_length=10)

	def clean_password(self):
		password = self.cleaned_data.get('password',None)
		if len(password) < 6:
			raise forms.ValidationError(u'password at least 6 length',code='min_length')
		return password


	def clean(self):
		super(RegistForm,self).clean()
		# super.clean()
		cleaned_data = self.cleaned_data
		password = cleaned_data.get('password',None)
		password_repeat = cleaned_data.get('password_repeat',None)
		if password != password_repeat:
			self.add_error('password',u'password not equal')
			# raise forms.ValidationError
		# return cleaned_data
