import random

class AkinatorGame:
    def __init__(self):
        self.characters = {
            "Homem de Ferro": "super-herói",
            "Sherlock Holmes": "detetive",
            "Mario": "encanador",
           "Batman": "super-herói",
          "Superman": "super-herói",
          "Flash": "super-herói",
          "Aquaman": "super-herói",
          "Supergirl": "super-herói",
          "Wonder Woman": "super-herói",
          "Green Lantern": "super-herói",
          "Green Arrow": "super-herói",
          "Flash": "super-herói",
          "Green Arrow": "super-herói",
          "Everaldo de souza pinho": "família"
            # Adicione mais personagens e suas características aqui
        }

    def start_game(self):
        print("Bem-vindo ao Jogo de Adivinhação!")
        print("Pense em um personagem e eu vou tentar adivinhar.")

        while True:
            question = self.get_random_question()
            print(f"\n{question}")

            response = input("Digite 's' se sim, 'n' se não, ou 'q' para sair: ").lower()

            if response == 'q':
                print("Obrigado por jogar! Até a próxima.")
                break
            elif response == 's' or response == 'n':
                self.filter_characters(question, response)
            else:
                print("Resposta inválida. Tente novamente.")

    def get_random_question(self):
        questions = [
            "Seu personagem é um super-herói?",
            "Seu personagem é um detetive?",
            "Seu personagem é um encanador?",
           "Seu personagem é da sua família?"
          
            # Adicione mais perguntas aqui
        ]
        return random.choice(questions)

    def filter_characters(self, question, response):
        filtered_characters = {
            character: category for character, category in self.characters.items() if self.evaluate_question(character, question, response)
        }

        if filtered_characters:
            self.characters = filtered_characters
        else:
            print("Não consegui adivinhar. Pode ser que eu precise de mais informações.")

    def evaluate_question(self, character, question, response):
        category = self.characters[character]

        if "sim" in response and category.lower() in question.lower():
            return True
        elif "não" in response and category.lower() not in question.lower():
            return True

        return False

# Iniciar o jogo
game = AkinatorGame()
game.start_game()
