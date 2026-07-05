total_produtos = 0
soma_precos = 0.0
produtos_acima_100 = 0

produto_mais_caro = ""
maior_preco = 0.0

print("--- CADASTRO DE PRODUTOS ---")
print("(Digite 'sair' no nome do produto para encerrar)\n")

while True:
    nome = input("Nome do produto: ").strip()
    
    if nome.lower() == 'sair':
        break
    
    try:
        preco = float(input(f"Preço de '{nome}': R$ "))
    except ValueError:
        print("❌ Preço inválido! Por favor, insira um número. Tente cadastrar o produto novamente.\n")
        continue

    
    total_produtos += 1
    soma_precos += preco
    
    if preco > 100:
        produtos_acima_100 += 1
        
    if total_produtos == 1 or preco > maior_preco:
        maior_preco = preco
        produto_mais_caro = nome

