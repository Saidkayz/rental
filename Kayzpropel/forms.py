from django import forms
from Kayzpropel.models import Property, Member, Transactions


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'image', 'location', 'upload_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'email', 'username', 'password']

class MpesadataForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['amount', 'phone_number', 'transaction_date']