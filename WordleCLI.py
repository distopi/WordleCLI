import random
import sys

ARQUIVO_PALAVRAS = "words.txt"


def carregar_palavras(caminho: str) -> list[str]:
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return [linha.strip().lower() for linha in arquivo if linha.strip()]
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
        sys.exit(1)


def main():
    palavras = carregar_palavras(ARQUIVO_PALAVRAS)

    if not palavras:
        print("Erro: O arquivo de palavras está vazio.")
        return

    palavra_sorteada = random.choice(palavras)
    tamanho_palavra = len(palavra_sorteada)

    letras_descobertas = ["_"] * tamanho_palavra
    letras_tentadas = set()  # Usar 'set' é mais rápido para checar se algo já existe

    max_turnos = tamanho_palavra + 7
    turnos_gastos = 0

    print("=" * 40)
    print("Bem-vindo ao Jogo WordleCLI")
    print("=" * 40)

    # Loop principal do jogo
    while turnos_gastos < max_turnos:
        chances_restantes = max_turnos - turnos_gastos

        print(f"\nA palavra tem {tamanho_palavra} letras.")
        print(f"Você tem {chances_restantes} chance(s) restante(s).")

        print(f"Palavra: {' '.join(letras_descobertas)}")

        chute = input("Qual o seu palpite (uma letra)? ").strip().lower()

        if not chute.isalpha():
            print("⚠️ Por favor, digite apenas letras!")
            continue
        if len(chute) != 1:
            print("⚠️ Por favor, digite apenas UMA letra por vez!")
            continue
        if chute in letras_tentadas:
            print("⚠️ Você já tentou essa letra. Tente outra!")
            continue

        letras_tentadas.add(chute)
        turnos_gastos += 1

        if chute in palavra_sorteada:
            print("Você acertou uma letra!")

            for i, letra in enumerate(palavra_sorteada):
                if letra == chute:
                    letras_descobertas[i] = chute
        else:
            print("Letra incorreta!")

        if "_" not in letras_descobertas:
            print(f"\n PARABÉNS! Você descobriu a palavra secreta: '{palavra_sorteada.upper()}'! 🏆")
            break

    else:
        print(f"\n Que pena, suas chances acabaram! A palavra era: '{palavra_sorteada.upper()}'")


if __name__ == "__main__":
    main()
