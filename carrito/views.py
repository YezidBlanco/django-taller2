from django.shortcuts import render
from django.http import HttpResponse
from carrito.models import Customer

# Create your views here.

def index(request):
    clientes = Customer.objects.all()
    context = {
        "numero_clientes": len(clientes),
        "clientes": clientes,
    }
    return render(request, "carrito/index.html", context)

def carrito_yezid(request):
    html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Carrito</title>
            </head>
            <body>
                <header>
                    <h1>Carrito</h1>
                </header>

                <section class="contenedor">
                    <!-- <h2>Contenedor</h2> -->
                    <section class="principal">
                        <!-- <h2>Principal</h2> -->
                        <h5>Nombre: Yezid Blanco Maldonado</h5>
                    </section>
                    <aside>
                        <!-- <h3>El Aside</h3> -->
                        <h3>Visitas</h3>
                        <a href="https://www.contadorvisitasgratis.com" title="http contador de visitas com"><img src="https://counter10.wheredoyoucomefrom.ovh/private/contadorvisitasgratis.php?c=4ywulrbfean8ql13qsdztybtn4645bcg" border="0" title="http contador de visitas com" alt="http contador de visitas com"></a>
                    </aside>

                </section>
            <footer>
                <h4>2024</h4>
            </footer>
            </body>
            </html>
    """
    return HttpResponse(html)