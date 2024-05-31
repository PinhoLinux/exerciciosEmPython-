def jogo_perguntas():
    print("Jogo do Quiz 🤔")
    # Perguntas, opções e respostas corretas
    perguntas = [
        "Qual é a principal fonte de energia utilizada no Brasil?",
        "Qual dessas fontes de energia não é renovável?",
        "Qual fonte de energia é obtida do sol?",
        "Qual fonte de energia usa o vento para gerar eletricidade?",
        "Qual é a principal desvantagem da energia nuclear?",
        "Qual dessas fontes de energia vem da queima de material orgânico?",
        "Qual país é conhecido por usar muita energia solar?",
        "Qual é a principal desvantagem da energia solar?",
        "Qual material é usado para fazer painéis solares? (Dica: é um elemento químico)",
        "Qual dessas fontes de energia vem do movimento da água?",
    ]

    opcoes = [
        ["\033[1;32ma) Hidrelétrica\033[0m", "\033[1;31mb) Nuclear\033[0m", "\033[1;33mc) Solar\033[0m", "\033[1;34md) Eólica\033[0m"],
        ["\033[1;33ma) Solar\033[0m", "\033[1;34mb) Eólica\033[0m", "\033[1;31mc) Nuclear\033[0m", "\033[1;32md) Biomassa\033[0m"],
        ["\033[1;34ma) Eólica\033[0m", "\033[1;32mb) Hidrelétrica\033[0m", "\033[1;33mc) Solar\033[0m", "\033[1;32md) Biomassa\033[0m"],
        ["\033[1;33ma) Solar\033[0m", "\033[1;34mb) Eólica\033[0m", "\033[1;31mc) Nuclear\033[0m", "\033[1;32md) Biomassa\033[0m"],
        ["\033[1;31ma) Alta emissão de CO2\033[0m", "\033[1;32mb) Custo elevado\033[0m", "\033[1;33mc) Resíduos radioativos\033[0m", "\033[1;34md) Depende do clima\033[0m"],
        ["\033[1;33ma) Solar\033[0m", "\033[1;34mb) Eólica\033[0m", "\033[1;32mc) Biomassa\033[0m", "\033[1;32md) Hidrelétrica\033[0m"],
        ["\033[1;34ma) Brasil\033[0m", "\033[1;32mb) Alemanha\033[0m", "\033[1;31mc) Estados Unidos\033[0m", "\033[1;32md) Japão\033[0m"],
        ["\033[1;32ma) Custo alto\033[0m", "\033[1;31mb) Intermitência\033[0m", "\033[1;33mc) Poluição\033[0m", "\033[1;34md) Consumo de água\033[0m"],
        ["\033[1;32ma) Cobre\033[0m", "\033[1;33mb) Silício\033[0m", "\033[1;34mc) Alumínio\033[0m", "\033[1;31md) Ferro\033[0m"],
        ["\033[1;32ma) Solar\033[0m", "\033[1;34mb) Eólica\033[0m", "\033[1;32mc) Hidrelétrica\033[0m", "\033[1;31md) Nuclear\033[0m"],
    ]

    respostas_certas = ["a", "c", "c", "b", "c", "c", "b", "b", "b", "c"]


    explicacoes = {
        "silício": "Silício é um elemento químico usado para fazer painéis solares porque é muito bom em converter luz solar em eletricidade.",
        "biomassa": "Biomassa é material orgânico, como madeira ou resíduos agrícolas, que pode ser queimado para produzir energia.",
        "intermitência": "Intermitência significa que algo não é constante. No caso da energia solar, a intermitência se refere ao fato de que não podemos gerar eletricidade solar à noite ou em dias nublados.",
        "resíduos radioativos": "Resíduos radioativos são materiais que sobram das usinas nucleares e que são perigosos para a saúde e o meio ambiente por muito tempo.",
    }

    pontuacao = 0

    # Loop através das perguntas
    for i in range(len(perguntas)):
        print(f"Pergunta {i + 1}: {perguntas[i]}")
        for opcao in opcoes[i]:
            print(opcao)
        
        resposta = input("Sua resposta (a/b/c/d): ").lower()
        
        if resposta == respostas_certas[i]:
            print("Correto!\n")
            pontuacao += 1
        else:
            print(f"Incorreto! A resposta correta é: {respostas_certas[i]}\n")
        
        # Adicionar explicação, se houver
        for termo, explicacao in explicacoes.items():
            if termo in perguntas[i].lower() or termo in opcoes[i][ord(respostas_certas[i]) - ord('a')].lower():
                print(f"Explicação: {explicacao}\n")

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")
    print("Esse é o nosso jogo, Grazi 🥳")

    # Perguntar quem está assistindo
    assistindo = input("Quem está assistindo? (anacleia, kayro, ambos): ").lower()

    if assistindo == "anacleia":
        print("Obrigado por assistir, Anacleia! 🫡🤝")
        nota_anacleia = input("Qual é a sua nota de 0 a 10? ")
        print(f"Anacleia, sua nota é: {nota_anacleia}")
    elif assistindo == "kayro":
        print("Obrigado por assistir, Kayro! 🫡🤝")
        nota_kayro = input("Qual é a sua nota de 0 a 10? ")
        print(f"Kayro, sua nota é: {nota_kayro}")
    elif assistindo == "ambos":
        print("Obrigado por assistir, Anacleia e Kayro! 🫡🤝")
        nota_anacleia = input("Anacleia, qual é a sua nota de 0 a 10? ")
        nota_kayro = input("Kayro, qual é a sua nota de 0 a 10? ")
        print(f"Nota de Anacleia: {nota_anacleia}")
        print(f"Nota de Kayro: {nota_kayro}")
        print(f"Vocês dois também são nota 10!")
    else:
        print("Resposta inválida.")

    # Perguntar a nota de Graziela
    nota_graziela = input("Graziela, qual é a sua nota de 0 a 10? ")
    print(f"Graziela, você é nota {nota_graziela}!")

    import time

def agradecimento():
    print("\n" * 30)  # Cria espaço para simular uma tela preta
    print("Gostaríamos de agradecer à equipe que produziu e pensou o jogo:")
    print("Emerson Pinho (Programador)")
    print("Isaac (Pensador)")
    print("Rafael Alves (Inovador)")
    print("Renato Alves (Criador da Lógica)")
    
    # Agradecimento à equipe
    print("\nGostaríamos de agradecer à equipe que produziu e pensou o jogo:")
    print("Emerson Pinho (Programador)")
    print("Isaac (Pensador)")
    print("Rafael pereira (Inovador)")
    print(" Renato Alves (Criador da Lógica)")
    # Agradecimento ao usuário
    print("\nObrigado por jogar o nosso jogo! 😊")

jogo_perguntas()