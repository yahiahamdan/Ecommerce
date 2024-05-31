from django import forms
product_quantity_choices = [(i, str(i)) for i in range(1, 21)]
class CartAddPrdouctForm(forms.Form):
    quantity=forms.TypedChoiceField(
        choices=product_quantity_choices,
        coerce=int
    )
    override=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
    