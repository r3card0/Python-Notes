# extrae los indices donde el type del elemento es diferente (!=) a integer int
class Clean:
    def __init__(self,list:list) -> list:
        self.list = list

    def cleanList(self):
        for i in self.list:
            if type(i) != int:
                pos  = self.list.index(i)

        self.list.pop(pos)

        return self.list
      
      
# Ejemplo para aplicar la clase
# listaParaLimpiar = [1,2,'4','45']
# listaLimpia = Clean(listaParaLimpiar).cleanList()
