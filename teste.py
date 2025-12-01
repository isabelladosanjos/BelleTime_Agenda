(ESSE CÓDIGO FOI CRIADO NO INÍCIO DO PROJETO PARA TESTAR O BANCO DE DADOS)

import database

print("--- INICIANDO TESTE DE CONEXÃO ---")

# 1. Teste de ADICIONAR cliente
print("\n[TESTE 1: Adicionando novo cliente...]")
database.adicionar_cliente("Vitoria Teste", "(15) 99999-1111", "Cliente de teste do app")

# 2. Teste de LISTAR clientes
print("\n[TESTE 2: Listando todos os clientes...]")
clientes = database.listar_clientes()

if not clientes:
    print("Nenhum cliente encontrado ou erro na conexão.")
else:
    for cliente in clientes:
        print(f"ID: {cliente['id']}, Nome: {cliente['nome']}, Tel: {cliente['telefone']}")

print("\n--- TESTE FINALIZADO ---")
