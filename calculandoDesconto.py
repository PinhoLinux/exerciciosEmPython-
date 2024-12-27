valorProduto = float(input('Digite o valor do produto: R$ '))
desconto = valorProduto * 0.05
valorDesconto = valorProduto - desconto
print(f'O produto que era R${valorProduto} com desconto de 5% ficará R${valorDesconto:.2f}')