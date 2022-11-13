from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos, Empleados

def Home(request):
    return render(request, 'index.html')
    
def Platos(request):

    formulario = FormularioPlatos()

    dataPlatos = {
        'formulario' : formulario,
        'banderaPlatos' : False
    }

    if request.method == 'POST':
        datosPlatos = FormularioPlatos(request.POST)
        if datosPlatos.is_valid():
            datosPlates = datosPlatos.cleaned_data
            nuevoPlato = Platos(
                nombreplato = datosPlates['nombrePlato'],
                descripcionplato = datosPlates['descripcionPlato'],
                fotoplato = datosPlates['fotoPlato'],
                precioplato = datosPlates['precioPlato'],
                tipoplato = datosPlates['tipoPlato']
            )

            
            try:
                nuevoPlato.save()
                dataPlatos["banderaPlatos"]=True
                print("EXITO GUARDANDO LOS DATOS")
            
            except Exception as error:
                dataPlatos["banderaPlatos"]=False
                print("error",error)

    return render(request, 'platos.html', dataPlatos)

def Empleados(request):

    formulario = FormularioEmpleados

    dataEmpleados = {
        'formularioEmpleados' : formulario,
        'banderaEmpleados' : False
    }

    if request.method == 'POST':
        datosEmpleados = FormularioEmpleados(request.POST)
        if datosEmpleados.is_valid():
            datosEmployees = datosEmpleados.cleaned_data
            nuevoEmpleado = Empleados(
                identificacionempleado = datosEmployees["identificacionEmpleado"],
                nombreempleado = datosEmployees["nombreEmpleado"],
                numerocontacto = datosEmployees["numeroContacto"],
                salario = datosEmployees["salario"],
                cargoempleado = datosEmployees["cargoEmpleado"]
            )

            try:
                nuevoEmpleado.save()
                dataEmpleados["banderaEmpleados"]=True
                print("EXITO GUARDANDO LOS DATOS")
            
            except Exception as error:
                dataEmpleados["banderaEmpleados"]=False
                print("error",error)

         
 

    return render(request, 'empleados.html', dataEmpleados)