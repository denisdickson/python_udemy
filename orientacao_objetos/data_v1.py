class Data:  # Classe representa tipo de dado personalizado
   
    
    #def to_str(self):#todo metodo começa com self / self - obj que está sendo acessado
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


# Data() método construtor da classe, faz ponte entre a classe
d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2021
print(d1)

d2 = Data()
d2.dia = 19
d2.mes = 11
d2.ano = 2016
print(d2)
