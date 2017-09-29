from inventory.models import Item
from django import forms


class ItemForm1(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class ItemForm2(forms.ModelForm):
    title = forms.CharField(max_length=128)
    description = forms.Textarea()
    amount = forms.IntegerField()

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Item
        fields = '__all__'


class ItemForm3(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ItemForm3, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter the Item name.'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter description'})
        self.fields['amount'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter amount'})

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Item
        fields = ['title', 'description', 'amount']
