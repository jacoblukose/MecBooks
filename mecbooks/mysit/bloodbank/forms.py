from django import forms

class pass_change(forms.Form):
    oldpassword=forms.CharField(
        widget=forms.PasswordInput)
    newpassword1=forms.CharField(
        widget=forms.PasswordInput)
    newpassword2=forms.CharField(
        widget=forms.PasswordInput)


class Lform(forms.Form):       #sampleclasss
    # print "inside ContactFor Class"
    firstname=forms.CharField(max_length=100)
    password = forms.CharField(
        widget=forms.PasswordInput)

#     #sex=forms.CharField(max_length=20)
#     #bloodgroup=forms.CharField(max_length=5)
#     #weight=forms.IntegerField()

class CForm(forms.Form):
    
    # print "inside cform Class"
    firstname = forms.CharField(max_length=100)
    lastname= forms.CharField(max_length=100)
    # age=forms.IntegerField()
    # email=forms.EmailField()
    # # password = forms.CharField(widget=forms.PasswordInput)
    pass1 = forms.CharField(
        widget=forms.PasswordInput)
    pass2 = forms.CharField(
        widget=forms.PasswordInput)
        # help_text=_("Enter the same password as above, for verification.")

    # class Meta:
    #     model = User
    #     fields = ("username",)

    def clean_password2(self):
        print "inside func"
        pass1= self.cleaned_data.get("pass1")
        pass2 = self.cleaned_data.get("pass2")
        if pass1 and pass2 and pass1 != pass2:
            return 0
            #raise forms.ValidationError(
            #    code='password_mismatch'
            #)
        return pass2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["pass1"])
        if commit:
            user.save()
        return user

class search_addbook_form(forms.Form):

    bookname = forms.CharField(max_length=100)

class categoryform(forms.Form):
    
    #categoryname=forms.CharField(max_length=100)
    choices = forms.MultipleChoiceField(
        # choices = LIST_OF_VALID_CHOICES, # this is optional
        widget  = forms.CheckboxSelectMultiple,
    ) 

class search_addcat_form(forms.Form):
    catname=forms.CharField(max_length=100)

class searchbookform(forms.Form):
    yoyi=forms.CharField(max_length=100)
    queryname=forms.CharField(max_length=100)


class fileupload(forms.Form):
    file=forms.FileField()