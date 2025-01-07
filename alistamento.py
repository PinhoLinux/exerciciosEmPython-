anoNasc =  int(input("Digite o ano de nascimento: "))
idade = 2024 - anoNasc
if idade < 18:
    print(f"você nasceu em {anoNasc} e tem {idade} anos\n ainda faltam {18 - idade} anos para o alistamento")
elif idade == 18:
    print(f"Você nasceu em {anoNasc} e tem {idade} anos. Aliste-se imediatamente!")
elif idade > 18:
    print(f"você nasceu em {anoNasc} e tem {idade} anos. ja deveria ter se alistado a {idade - 18} anos")