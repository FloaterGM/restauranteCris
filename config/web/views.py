from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos, Empleado

def Home(request):
    return render(request, 'index.html')

def vistaEmployees(request):

    verEmpleados = Empleado.objects.all()

    dataEmployees = {
        'empleados': verEmpleados
    }

    return render(request, 'verEmpleados.html', dataEmployees)

def vistaMenu(request):

    verPlatos = Platos.objects.all()
    print(verPlatos)

    dataMenu = {
        'platos': verPlatos
    }

    return render(request, 'verMenu.html', dataMenu)
    
def vistaPlatos(request):

    formulario = FormularioPlatos()

    dataPlatos = {
        'formulario' : formulario,
        'banderaPlatos' : False
    }

    if request.method == 'POST':
        datosPlatos = FormularioPlatos(request.POST)
        if datosPlatos.is_valid():
            datosPlates = datosPlatos.cleaned_data
            newPlato = Platos(
                nombre=datosPlates["nombrePlato"],
                descripcion=datosPlates["descripcionPlato"],
                foto=datosPlates["fotoPlato"],
                precio=datosPlates["precioPlato"],
                tipo=datosPlates["tipoPlato"]
            )

            try:
                newPlato.save()
                dataPlatos["banderaPlatos"]=True
                print("EXITO GUARDANDO LOS DATOS")
            
            except Exception as error:
                dataPlatos["banderaPlatos"]=False
                print("error",error)
            

        

    return render(request, 'platos.html', dataPlatos)

def vistaEmpleados(request):

    formulario = FormularioEmpleados

    dataEmpleados = {
        'formularioEmpleados' : formulario,
        'banderaEmpleados' : False,
    }

    if request.method == 'POST':
        datosEmpleados = FormularioEmpleados(request.POST)
        if datosEmpleados.is_valid():
            datosEmployees = datosEmpleados.cleaned_data
            newEmpleado = Empleado(
                foto = datosEmployees["fotoEmpleado"],
                nombre = datosEmployees["nombreEmpleado"],
                numero = datosEmployees["numeroContacto"],
                salario = datosEmployees["salario"],
                cargo = datosEmployees["cargoEmpleado"]
            )

            try:
                newEmpleado.save()
                dataEmpleados["banderaEmpleados"]=True
                print("EXITO GUARDANDO LOS DATOS")
            
            except Exception as error:
                dataEmpleados["banderaEmpleados"]=False
                print("error",error)

           
 

    return render(request, 'empleados.html', dataEmpleados)