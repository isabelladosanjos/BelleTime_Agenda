# database.py 
import mysql.connector
from mysql.connector import Error

# --- 1. CONFIGURAÇÃO DA CONEXÃO ---
CONFIG = {
    'host': '192.168.15.10',  # <--- CONFIRA SE O IP DA VM É ESSE MESMO (ip a)
    'user': 'isabella',
    'password': '745181',
    'database': 'belletime_agendadb'
}

def conectar_banco():
    try:
        conexao = mysql.connector.connect(**CONFIG)
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# --- 2. CRUD DE CLIENTES ---

def adicionar_cliente(nome, telefone, anotacoes):
    conexao = conectar_banco()
    if conexao is None: return False
    cursor = conexao.cursor()
    sql = "INSERT INTO clientes (nome, telefone, anotacoes) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql, (nome, telefone, anotacoes))
        conexao.commit()
        return True
    except Error as e:
        print(f"Erro ao adicionar cliente: {e}")
        return False
    finally:
        cursor.close()
        conexao.close()

def listar_clientes():
    conexao = conectar_banco()
    if conexao is None: return []
    cursor = conexao.cursor(dictionary=True) 
    try:
        cursor.execute("SELECT * FROM clientes ORDER BY id ASC")
        return cursor.fetchall()
    except Error: return []
    finally:
        cursor.close()
        conexao.close()

def buscar_cliente_por_id(id_cliente):
    conexao = conectar_banco()
    if conexao is None: return None
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id_cliente,))
        return cursor.fetchone()
    except Error: return None
    finally:
        cursor.close()
        conexao.close()

def atualizar_cliente(id_cliente, nome, telefone, anotacoes):
    conexao = conectar_banco()
    if conexao is None: return False
    cursor = conexao.cursor()
    sql = "UPDATE clientes SET nome = %s, telefone = %s, anotacoes = %s WHERE id = %s"
    try:
        cursor.execute(sql, (nome, telefone, anotacoes, id_cliente))
        conexao.commit()
        return True
    except Error: return False
    finally:
        cursor.close()
        conexao.close()

def excluir_cliente(id_cliente):
    conexao = conectar_banco()
    if conexao is None: return False
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
        conexao.commit()
        return True
    except Error: return False
    finally:
        cursor.close()
        conexao.close()

# --- 3. AGENDAMENTOS E DROPDOWNS ---

def listar_clientes_dropdown():
    conexao = conectar_banco()
    if conexao is None: return []
    cursor = conexao.cursor(dictionary=True) 
    try:
        cursor.execute("SELECT id, nome FROM clientes ORDER BY nome")
        return cursor.fetchall()
    except Error: return []
    finally:
        cursor.close()
        conexao.close()

def listar_servicos_dropdown():
    conexao = conectar_banco()
    if conexao is None: return []
    cursor = conexao.cursor(dictionary=True) 
    try:
        cursor.execute("SELECT id, nome, preco FROM servicos ORDER BY nome")
        return cursor.fetchall()
    except Error: return []
    finally:
        cursor.close()
        conexao.close()

def adicionar_agendamento(cliente_id, servico_id, data_hora):
    conexao = conectar_banco()
    if conexao is None: return False
    cursor = conexao.cursor()
    sql = "INSERT INTO agendamentos (cliente_id, servico_id, data_hora, status) VALUES (%s, %s, %s, 'Agendado')"
    try:
        cursor.execute(sql, (cliente_id, servico_id, data_hora))
        conexao.commit()
        return True
    except Error: return False
    finally:
        cursor.close()
        conexao.close()

def excluir_agendamento(id_agendamento):
    conexao = conectar_banco()
    if conexao is None: return False
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM agendamentos WHERE id = %s", (id_agendamento,))
        conexao.commit()
        return True
    except Error: return False
    finally:
        cursor.close()
        conexao.close()

# --- 4. RELATÓRIOS ---

def contar_total_clientes():
    conexao = conectar_banco()
    if conexao is None: return 0
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT COUNT(id) as total FROM clientes")
        res = cursor.fetchone()
        return res[0] if res else 0
    except Error: return 0
    finally:
        cursor.close()
        conexao.close()

def listar_agendamentos_hoje():
    conexao = conectar_banco()
    if conexao is None: return []
    cursor = conexao.cursor(dictionary=True)
    sql = """
        SELECT c.nome as nome_cliente, s.nome as nome_servico, a.data_hora
        FROM agendamentos a
        JOIN clientes c ON a.cliente_id = c.id
        JOIN servicos s ON a.servico_id = s.id
        WHERE DATE(a.data_hora) = CURDATE()
        ORDER BY a.data_hora
    """
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Error: return []
    finally:
        cursor.close()
        conexao.close()

def calcular_faturamento_mensal():
    conexao = conectar_banco()
    if conexao is None: return 0.0
    cursor = conexao.cursor()
    sql = """
        SELECT SUM(s.preco) FROM agendamentos a
        JOIN servicos s ON a.servico_id = s.id
        WHERE MONTH(a.data_hora) = MONTH(CURDATE()) 
        AND YEAR(a.data_hora) = YEAR(CURDATE())
    """
    try:
        cursor.execute(sql)
        res = cursor.fetchone()
        return float(res[0]) if res and res[0] else 0.0
    except Error: return 0.0
    finally:
        cursor.close()
        conexao.close()

def listar_agendamentos_mes_tabela():
    conexao = conectar_banco()
    if conexao is None: return []
    cursor = conexao.cursor(dictionary=True)
    sql = """
        SELECT a.id, a.data_hora, c.nome as cliente, s.nome as servico, s.preco
        FROM agendamentos a
        JOIN clientes c ON a.cliente_id = c.id
        JOIN servicos s ON a.servico_id = s.id
        WHERE MONTH(a.data_hora) = MONTH(CURDATE()) 
        AND YEAR(a.data_hora) = YEAR(CURDATE())
        ORDER BY a.data_hora DESC
    """
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Error: return []
    finally:
        cursor.close()
        conexao.close()

# --- 5. NOVO: CRUD DE SERVIÇOS (GERENCIAR CARDÁPIO) ---

def listar_servicos_crud():
    conexao = conectar_banco()
    if conexao is None: return []
    cursor = conexao.cursor(dictionary=True) 
    try:
        cursor.execute("SELECT * FROM servicos ORDER BY nome")
        return cursor.fetchall()
    except Error: return []
    finally:
        cursor.close()
        conexao.close()

def buscar_servico_por_id(id_servico):
    conexao = conectar_banco()
    if conexao is None: return None
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM servicos WHERE id = %s", (id_servico,))
        return cursor.fetchone()
    except Error: return None
    finally:
        cursor.close()
        conexao.close()

def adicionar_servico(nome, duracao, preco):
    conexao = conectar_banco()
    if conexao is None: return False
    cursor = conexao.cursor()
    sql = "INSERT INTO servicos (nome, duracao_minutos, preco) VALUES (%s, %s, %s)"
    try:
        cursor.execute(sql, (nome, duracao, preco))
        conexao.commit()
        return True
    except Error as e:
        print(f"Erro ao adicionar serviço: {e}")
        return False
    finally:
        cursor.close()
        conexao.close()

def atualizar_servico(id_servico, nome, duracao, preco):
    conexao = conectar_banco()
    if conexao is None: return False
    cursor = conexao.cursor()
    sql = "UPDATE servicos SET nome = %s, duracao_minutos = %s, preco = %s WHERE id = %s"
    try:
        cursor.execute(sql, (nome, duracao, preco, id_servico))
        conexao.commit()
        return True
    except Error: return False
    finally:
        cursor.close()
        conexao.close()

def excluir_servico(id_servico):
    conexao = conectar_banco()
    if conexao is None: return False
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM servicos WHERE id = %s", (id_servico,))
        conexao.commit()
        return True
    except Error as e:
        print(f"Erro ao excluir serviço: {e}")
        return False
    finally:
        cursor.close()
        conexao.close()
    
def verificar_login(usuario, senha):
    """Verifica se o usuário e senha existem no banco."""
    conexao = conectar_banco()
    if conexao is None: return False

    cursor = conexao.cursor()
    sql = "SELECT * FROM usuarios WHERE login = %s AND senha = %s"

    try:
        cursor.execute(sql, (usuario, senha))
        resultado = cursor.fetchone()
        return True if resultado else False # Retorna True se achou alguém
    except Error as e:
        print(f"Erro no login: {e}")
        return False
    finally:
        cursor.close()
        conexao.close()

def verificar_horario_ocupado(data_hora):
    """Verifica se já existe agendamento neste horário (ignorando segundos)."""
    conexao = conectar_banco()
    if conexao is None: return False
    
    cursor = conexao.cursor()
    
    sql = """
        SELECT COUNT(*) FROM agendamentos 
        WHERE DATE_FORMAT(data_hora, '%Y-%m-%d %H:%i') = DATE_FORMAT(%s, '%Y-%m-%d %H:%i')
    """
    
    try:
        cursor.execute(sql, (data_hora,))
        resultado = cursor.fetchone()
        quantidade = resultado[0]
        return quantidade > 0 # Se for maior que 0, está ocupado
    except Error as e:
        print(f"Erro ao verificar horário: {e}")
        return False
    finally:
        cursor.close()
        conexao.close()