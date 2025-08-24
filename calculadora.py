import statistics
import math

def calcular_media(numeros):
    return statistics.mean(numeros)

def calcular_mediana(numeros):
    return statistics.median(numeros)

def calcular_moda(numeros):
    try:
        return statistics.mode(numeros)
    except statistics.StatisticsError:
        return "Não há moda (valores únicos ou múltiplas modas)"

def calcular_desvio_padrao(numeros):
    return statistics.stdev(numeros)

def calcular_fatorial(n):
    return math.factorial(n)

def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def salvar_relatorio(nome_arquivo, conteudo):
    with open(nome_arquivo, "w") as f:
        f.write(conteudo)

def menu():
    while True:
        print("\n--- Calculadora Estatística ---")
        print("1. Média")
        print("2. Mediana")
        print("3. Moda")
        print("4. Desvio Padrão")
        print("5. Fatorial")
        print("6. Fibonacci")
        print("7. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha in ["1", "2", "3", "4"]:
            numeros = list(map(float, input("Digite os números separados por espaço: ").split()))
            if escolha == "1":
                resultado = calcular_media(numeros)
                print(f"Média: {resultado}")
                salvar_relatorio("media.txt", f"Números: {numeros}\nMédia: {resultado}")
            elif escolha == "2":
                resultado = calcular_mediana(numeros)
                print(f"Mediana: {resultado}")
                salvar_relatorio("mediana.txt", f"Números: {numeros}\nMediana: {resultado}")
            elif escolha == "3":
                resultado = calcular_moda(numeros)
                print(f"Moda: {resultado}")
                salvar_relatorio("moda.txt", f"Números: {numeros}\nModa: {resultado}")
            elif escolha == "4":
                resultado = calcular_desvio_padrao(numeros)
                print(f"Desvio Padrão: {resultado}")
                salvar_relatorio("desvio_padrao.txt", f"Números: {numeros}\nDesvio Padrão: {resultado}")
        
        elif escolha == "5":
            n = int(input("Digite um número inteiro para fatorial: "))
            resultado = calcular_fatorial(n)
            print(f"Fatorial de {n}: {resultado}")
            salvar_relatorio("fatorial.txt", f"Fatorial de {n}: {resultado}")
        
        elif escolha == "6":
            n = int(input("Quantos números da sequência de Fibonacci deseja gerar? "))
            resultado = fibonacci(n)
            print(f"Fibonacci ({n} números): {resultado}")
            salvar_relatorio("fibonacci.txt", f"Fibonacci ({n} números): {resultado}")
        
        elif escolha == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
