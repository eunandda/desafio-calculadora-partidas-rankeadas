def calcular_saldo_nivel(vitorias, derrotas):
    saldo = vitorias - derrotas
    
    if vitorias < 10:
        nivel = "Ferro"
    elif 10 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:  
        nivel = "Imortal"
    
    
    return saldo, nivel

vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))

saldoVitorias, nivel = calcular_saldo_nivel(vitorias, derrotas)

print(f"O Herói tem de saldo {saldoVitorias} e está no nível {nivel}.")