from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta: # Holds info about what fields should be there in the particular form. Provides info about this class(RegisterForm). Meta - Data about data
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
