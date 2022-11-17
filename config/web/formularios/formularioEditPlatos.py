from django import forms

class formularioEditPlatos(forms.Form):

    precioPlato=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3', 'placeholder': 'Precio del plato'}),
        required=True,
    )