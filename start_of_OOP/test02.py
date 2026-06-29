import time
import msvcrt
import os

distancia = float(input("DISTÂNCIA A SER PERCORRIDA:(KM) "))
combustivel = float(input("COMBUSTÍVEL DISPONÍVEL:(L) "))
tempo_desejado = int(input("TEMPO DESEJADO DE CONCLUSÃO:(SEG) "))

consumo = [0, 5.5, 4.7, 9.4, 8.1, 10.2, 9.6, 14.7, 13.6, 12.5]
distancia = distancia * 1000 
cont = 0                                     
tempo = 0                                   
tempo_parado = 0                                                                     
tempo_acima25 = 0   
velocidade = 0
velocidade_somada = 0                                              
distancia_percorida = 0                      
consumo_atual = 0
combustivel_restante = combustivel               
cambio = 0                                  

# --- NOVA MATRIZ PARA O HISTÓRICO ---
historico_viagem = [] 

def consumo_medio(distancia_percorrida_m, combustivel_original, combustivel_atual):
    litros_gastos = combustivel_original - combustivel_atual
    if litros_gastos == 0:
        return 0
    return (distancia_percorrida_m / 1000) / litros_gastos

def classificar_velocidade(velocidade):
    if velocidade == 0:
        return "Parado"
    elif 0 < velocidade <= 3:
        return "Lento"
    elif 3 < velocidade <= 6:
        return "Moderado"
    else:
        return "Rápido"

def formatar_tempo(tempo_segundos):
    horas = tempo_segundos // 3600 
    minutos = (tempo_segundos % 3600) // 60 
    segundos = tempo_segundos % 60
    # O :02d garante que mostre 02:05:09 em vez de 2:5:9
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

while True:
    tempo += 1                                     
    tempo_restante = tempo_desejado - tempo
    
    print("TECLAS [0] a [9] VARIAM A VELOCIDADE | APERTE Q PARA SAIR")
    
    if msvcrt.kbhit():
        tecla = msvcrt.getch()
        if tecla.isdigit():
            valor = int(tecla)
            if 0 <= valor <= 9:
                cambio = valor
        elif tecla in [b'q', b'Q']:
            print("Sair selecionado")
            break

    if cambio == 0:                                                                 
        tempo_parado += 1
        velocidade = 0
        consumo_atual = 0
    else:
        consumo_atual = consumo[cambio]           
        velocidade = cambio                      
        velocidade_somada += velocidade          
        cont += 1                                 
        combustivel_restante -= (velocidade / 1000) / consumo_atual 

    distancia_percorida += velocidade                                            
    distancia_faltante_metros = distancia - distancia_percorida   
    velocidadeKMH = velocidade * 3.6                                              
    
    if velocidadeKMH > 25:
        tempo_acima25 += 1

    # --- SALVANDO OS DADOS NA MATRIZ ---
    # Cada linha da matriz terá 4 colunas: [Tempo, Velocidade, Distância, Combustível]
    dados_segundo_atual = [tempo, velocidade, distancia_percorida, combustivel_restante]
    historico_viagem.append(dados_segundo_atual)

    # EXIBIÇÃO DAS INFORMAÇÕES
    print("===========================================")
    print("           COMPUTADOR DE BORDO")
    print("===========================================\n")

    if cambio == 0:
        print("---Veículo PARADO---")
        print(f"TEMPO: {formatar_tempo(tempo)}")
        
    if combustivel_restante <= 0:
        print("---SEM COMBUSTÍVEL---")
        break
    if distancia_faltante_metros <= 0:
        print("===VOCÊ CHEGOU AO SEU DESTINO===")
        break
    if tempo > tempo_desejado:
        print("===TEMPO DESEJADO ULTRAPASSADO===")
        
    if cambio > 0:    
        print("==================VELOCIDADE==================")
        print(f"Classificação da velocidade: {classificar_velocidade(velocidade)}")
        print(f"Velocidade atual: {velocidade} M/S ({velocidadeKMH:.1f} Km/h)")
        print(f"Velocidade média rodando:(M/S) {velocidade_somada / cont:.2f}")
        if tempo_restante > 0:
            print(f"Velocidade para o tempo estimado:(M/S) {distancia_faltante_metros / tempo_restante:.2f}")

        print("==================DISTÂNCIA==================")
        print(f"Distância total a percorrer:(KM) {distancia / 1000}")  
        print(f"Distância percorrida: {distancia_percorida:.1f} M ({distancia_percorida / 1000:.2f} KM)")
        print(f"Distância restante: {distancia_faltante_metros:.1f} M ({distancia_faltante_metros / 1000:.2f} KM)")

        print("==================TEMPO==================")
        print(f"Tempo em movimento: {formatar_tempo(cont)} | Tempo parado: {formatar_tempo(tempo_parado)}")
        print(f"Tempo total viajado: {formatar_tempo(tempo)}")
        print(f"Tempo acima de 25 KM/H: {formatar_tempo(tempo_acima25)}")

        print("==================COMBUSTÍVEL==================")
        print(f"Total de combustível no tanque:(L) {combustivel_restante:.2f}")
        print(f"Consumo Médio:(KM/L) {consumo_medio(distancia_percorida, combustivel, combustivel_restante):.2f}")
        print(f"Consumo atual:(KM/L) {consumo_atual:.2f}")

    time.sleep(1)
    os.system('cls')

# --- RELATÓRIO PÓS-VIAGEM (USANDO A MATRIZ) ---
print("\n===========================================")
print("          RELATÓRIO FINAL DA VIAGEM")
print("===========================================")
print(f"Total de segundos registrados na matriz: {len(historico_viagem)}")

# Exemplo de leitura da matriz: mostrando os dados do primeiro e do último segundo
if len(historico_viagem) > 0:
    primeiro_segundo = historico_viagem[0]
    ultimo_segundo = historico_viagem[-1]
    print(f"No 1º segundo: Velocidade = {primeiro_segundo[1]} m/s, Combustível = {primeiro_segundo[3]:.2f} L")
    print(f"No último segundo: Distância percorrida = {ultimo_segundo[2]:.2f} m")

print(historico_viagem)