from django.db import models


class AutorManager(models.Manager):

    def Listar_All_Autor(self):
        return self.all()

    def Filtro_name(self, clave):
        # icontains busca concidencia dentro del string
        resultado = self.filter(nombre__icontains = clave)
        return resultado