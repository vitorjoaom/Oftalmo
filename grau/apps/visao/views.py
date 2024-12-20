from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    dados = {
        1:{
            "nome": "Jhonny Santos",
            "telefone": "88005578",
            "endereço": "av. Maria Lacerda Montenegro, 515",
            "grau": "2.75",
        },
        2:{
            "nome":"Carlos Junior Filho",
            "telefone":"36669606",
            "endereço":"av. itapetinga, 4808",
            "grau":"4.15",
        },

    }
    return render(request, "index.html", {"contatos":dados})

def home(request):
    return HttpResponse("Página Home")