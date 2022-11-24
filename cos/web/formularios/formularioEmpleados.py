from django import forms


class FormularioEmpleados(forms.Form):

    #CREANDO ATRIBUTO PARA ACRGAR EL SELECTOR
    OPCIONES=(
        (1,'Cocinero'),
        (2,'Ayudante'),
        (3,'Mesero'),
        (4,'Administrador')
    )

    #DENTRO DE LA CLASE CADA ATRIBUTO SERÁ UN INPUT

    fotoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=200
    )

    nombreEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=16
    )

    numeroContacto=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        required=False,
        max_length=10
    )

    salario=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        required=True,
        max_length=7
    )
    
    cargoEmpleado=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        required=True,
        choices=OPCIONES
    )