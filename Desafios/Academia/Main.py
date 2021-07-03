from Atendentes import Atendentes
from Instrutores import Instrutores
from Clientes import Clientes

a1 = Atendentes("01", "Marcelo", "12/12/1980", 1200, "madrugada")
i1 = Instrutores("02", "Joel", "08/03/1990", 2000, "vespertino", "12345", "crossfit")
c1 = Clientes("00001", "José", "10/07/2003", "premium")
c1.plano = "platinum"
print(c1.plano)