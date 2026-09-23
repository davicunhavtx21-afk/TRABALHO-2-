# Dados do Cenário 1: Processos curtos
cenario_1 = [
    {"nome": "P1", "cpu": 3, "prioridade": 1},
    {"nome": "P2", "cpu": 1, "prioridade": 1},
    {"nome": "P3", "cpu": 2, "prioridade": 1}
]
def executar_fcfs(processos):
    tempo_atual = 0
    soma_espera = 0
    soma_turnaround = 0
    quantidade = len(processos)
    
    print("--- Execução FCFS ---")
    
    for p in processos:
        inicio = tempo_atual
        fim = inicio + p["cpu"]
        
        turnaround = fim # Como chegam no 0, turnaround é o tempo final
        espera = turnaround - p["cpu"] # Fórmula: turnaround - tempo de CPU
        
        # Atualiza métricas
        soma_turnaround += turnaround
        soma_espera += espera
        tempo_atual = fim
        
        print(f"{p['nome']} de {inicio} a {fim}")
        print(f"  Espera: {espera} | Turnaround: {turnaround}")
        
    print(f"Espera média: {soma_espera / quantidade:.2f}")
    print(f"Turnaround médio: {soma_turnaround / quantidade:.2f}\n")

# Testando o cenário 1
executar_fcfs(cenario_1)
def executar_sjf(processos):
    # Ordena a lista de processos dando prioridade ao menor tempo de CPU
    processos_ordenados = sorted(processos, key=lambda p: p["cpu"])
    
    tempo_atual = 0
    soma_espera = 0
    soma_turnaround = 0
    quantidade = len(processos_ordenados)
    
    print("--- Execução SJF ---")
    
    for p in processos_ordenados:
        inicio = tempo_atual
        fim = inicio + p["cpu"]
        
        turnaround = fim 
        espera = turnaround - p["cpu"]
        
        soma_turnaround += turnaround
        soma_espera += espera
        tempo_atual = fim
        
        print(f"{p['nome']} de {inicio} a {fim}")
        print(f"  Espera: {espera} | Turnaround: {turnaround}")
        
    print(f"Espera média: {soma_espera / quantidade:.2f}")
    print(f"Turnaround médio: {soma_turnaround / quantidade:.2f}\n")


def executar_prioridade(processos):
    # Ordena a lista dando foco a quem tem o menor número de prioridade (1 vem antes de 2)
    processos_ordenados = sorted(processos, key=lambda p: p["prioridade"])
    
    tempo_atual = 0
    soma_espera = 0
    soma_turnaround = 0
    quantidade = len(processos_ordenados)
    
    print("--- Execução Prioridade ---")
    
    for p in processos_ordenados:
        inicio = tempo_atual
        fim = inicio + p["cpu"]
        
        turnaround = fim 
        espera = turnaround - p["cpu"]
        
        soma_turnaround += turnaround
        soma_espera += espera
        tempo_atual = fim
        
        print(f"{p['nome']} de {inicio} a {fim}")
        print(f"  Espera: {espera} | Turnaround: {turnaround}")
        
    print(f"Espera média: {soma_espera / quantidade:.2f}")
    print(f"Turnaround médio: {soma_turnaround / quantidade:.2f}\n")

# Para testar, chame as funções usando o mesmo cenário 1:
# executar_sjf(cenario_1)
# executar_prioridade(cenario_1)
def executar_round_robin(processos, quantum=2):
    # Cria uma cópia da lista e adiciona o controle de quanto tempo de CPU ainda falta
    fila = []
    resultados = {}
    
    for p in processos:
        fila.append({"nome": p["nome"], "cpu_restante": p["cpu"], "cpu_total": p["cpu"]})
        resultados[p["nome"]] = {"espera": 0, "turnaround": 0}
        
    tempo_atual = 0
    print(f"--- Execução Round Robin (Quantum {quantum}) ---")
    
    while fila:
        # Retira o primeiro processo da fila
        p_atual = fila.pop(0)
        
        # Define se ele vai usar todo o quantum ou apenas o tempo que falta
        if p_atual["cpu_restante"] > quantum:
            tempo_uso = quantum
        else:
            tempo_uso = p_atual["cpu_restante"]
            
        inicio = tempo_atual
        fim = inicio + tempo_uso
        tempo_atual = fim
        
        # Subtrai o tempo usado da CPU restante do processo
        p_atual["cpu_restante"] -= tempo_uso
        
        print(f"{p_atual['nome']} de {inicio} a {fim}")
        
        # Verifica se o processo terminou
        if p_atual["cpu_restante"] == 0:
            resultados[p_atual["nome"]]["turnaround"] = tempo_atual
            # Fórmula: Espera = Turnaround - Tempo de CPU
            resultados[p_atual["nome"]]["espera"] = tempo_atual - p_atual["cpu_total"]
        else:
            # Se não terminou, volta pro fim da fila
            fila.append(p_atual)
            
    # Calcula e exibe as médias
    soma_espera = sum(dados["espera"] for dados in resultados.values())
    soma_turnaround = sum(dados["turnaround"] for dados in resultados.values())
    quantidade = len(processos)
    
    for nome, dados in resultados.items():
        print(f"  {nome} -> Espera: {dados['espera']} | Turnaround: {dados['turnaround']}")
        
    print(f"Espera média: {soma_espera / quantidade:.2f}")
    print(f"Turnaround médio: {soma_turnaround / quantidade:.2f}\n")
    # Definindo os 3 cenários exigidos[cite: 1]
cenario_1 = [
    {"nome": "P1", "cpu": 3, "prioridade": 1},
    {"nome": "P2", "cpu": 1, "prioridade": 1},
    {"nome": "P3", "cpu": 2, "prioridade": 1}
]

cenario_2 = [
    {"nome": "P1", "cpu": 8, "prioridade": 1},
    {"nome": "P2", "cpu": 2, "prioridade": 1},
    {"nome": "P3", "cpu": 1, "prioridade": 1}
]

cenario_3 = [
    {"nome": "P1", "cpu": 4, "prioridade": 3},
    {"nome": "P2", "cpu": 2, "prioridade": 1},
    {"nome": "P3", "cpu": 3, "prioridade": 2}
]

# Exemplo de como rodar todos para o Cenário 1:
print("========== CENÁRIO 1 ==========")
executar_fcfs(cenario_1)
executar_sjf(cenario_1) # (Requer a função SJF que passei na mensagem anterior)
executar_prioridade(cenario_1) # (Requer a função Prioridade que passei na mensagem anterior)
executar_round_robin(cenario_1, quantum=2)
print("\n========== CENÁRIO 2 ==========")
executar_fcfs(cenario_2)
executar_sjf(cenario_2)
executar_prioridade(cenario_2)
executar_round_robin(cenario_2, quantum=2)

print("\n========== CENÁRIO 3 ==========")
executar_fcfs(cenario_3)
executar_sjf(cenario_3)
executar_prioridade(cenario_3)
executar_round_robin(cenario_3, quantum=2)