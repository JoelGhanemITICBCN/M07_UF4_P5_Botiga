"""
URL configuration for botiga_grupD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import  path
from  catalog import views
urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    #Paths per poder fer el crud mitjancant post dels productes i el cataleg
    path('Aproductes/', views.afegir_producte, name='Aproducte'),
    #Aquest path conte l id del producte per saber quin estem canviant
    path('Mproductes/<int:producte_id>/', views.actualitzar_producte, name='Mproducte'),
    #Aquest path conte l id del producte per saber quin estem Eliminant
    path('Eproductes/<int:producte_id>/', views.eliminar_producte, name='Eproducte'),
    #Aquest path conte l id del producte per especificar quin mostrem
    path('Gproductes/<int:producte_id>/', views.mostrar_producte, name='Gproducte'),
    #Aquest path no conte l'id aixi que es mostren tots
    path('Gproductes/',views.mostrar_producte, name='Gproducte'),
]