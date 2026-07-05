import random

while True:
    print("\n" + "="*30)
    print("🎲 JOGO DE ADIVINHAÇÃO (MÁX: 7 CHANCES) 🎲")
    print("="*30)
    
    # Gera o número secreto e inicializa as variáveis do jogo
    numero_secreto = random.randint(1, 100)
    tentativas_restantes = 7
    historico = []
    ganhou = False

    while tentativas_restantes > 0:
        print(f"\nTentativas restantes: {tentativas_restantes}")
        if historico:
            print(f"Seus palpites anteriores: {historico}")
            
        # --- VALIDAÇÃO DE ENTRADA (Extra) ---
        try:
            palpite = int(input("Digite um número entre 1 e 100: "))
            if palpite < 1 or palpite > 100:
                print("⚠️ Fora do intervalo! Escolha um número de 1 a 100.")
                continue
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros.")
            continue

        # Adiciona o palpite ao histórico
        historico.append(palpite)
        tentativas_restantes -= 1

        # --- LÓGICA E COMPARAÇÕES ---
        if palpite == numero_secreto:
            ganhou = True
            break
        elif palpite > numero_secreto:
            print("📉 Muito alto!")
        else:
            print("📈 Muito baixo!")

    # --- FIM DA RODADA / RESULTADOS ---
    print("\n" + "-"*30)
    if ganhou:
        print(f"🎉 Parabéns! Você acertou em {7 - tentativas_restantes} tentativa(s)!")
        print(f"🏆 Histórico final de palpites: {historico}")
    else:
        print(f"💥 Que pena, suas chances acabaram! O número correto era: {numero_secreto}")
        print(f"📋 Seu histórico de tentativas: {historico}")
    print("-"*30)

    # --- PERGUNTAR SE DESEJA JOGAR NOVAMENTE ---
    jogar_de_novo = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
    if jogar_de_novo != 's':
        print("\nObrigado por jogar! Até a próxima. 👋")
        break