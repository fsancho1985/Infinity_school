from Cliente import Cliente
from Endereco import Endereco
from Carrinho import Carrinho
from Produto import Produto

#e1 = Endereco("41111-600", "Rua K", "300", "Itapuã", "Salvador", "Bahia", "Brasil")
#c1 = Cliente("Marlene", "mma_sss@email.com", "12345", e1)
#print(c1.endereco.cep)


p1 = Produto("Pasta", 3.0, "Pasta de dente Colgate")
p2 = Produto("Escova", 15.0, "Escova de dentes Oral-B")
p3 = Produto("Sabonete", 4.0, "Sabonete de rosas Phebo")

produtosCadastrados = [p1, p2, p3]

carrinho = Carrinho(produtosCadastrados)
print(carrinho.produtos)
print(carrinho.valorTotal())