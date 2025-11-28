import csv

ARQUIVO = "viagens.csv"
RELATORIO = "relatorio.txt"




def ler_viagens():
    viagens = []
    try:
        with open(ARQUIVO, "r") as f:
            leitor = csv.DictReader(f)  
            for linha in leitor:
                try:
                    data = linha["data"]
                    distancia = float(linha["distancia"])
                    combustivel = float(linha["combustivel"])

                    viagens.append({
                        "data": data,
                        "distancia": distancia,
                        "combustivel": combustivel
                    })
                except Exception:
                    print("⚠ Ignorando linha inválida:", linha)
    except FileNotFoundError:
        print("Arquivo não encontrado!")

    return viagens





def adicionar_viagem():
    data = input("Data da viagem (dd/mm/aaaa): ")
    distancia = float(input("Distância percorrida (km): "))
    combustivel = float(input("Combustível consumido (litros): "))

    with open(ARQUIVO, "a", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow([data, distancia, combustivel])

    print("✔ Viagem registrada com sucesso!")





def estatisticas():
    viagens = ler_viagens()

    if not viagens:
        print("Nenhuma viagem registrada.")
        return

    total = len(viagens)
    distancia_total = sum(v["distancia"] for v in viagens)
    combustivel_total = sum(v["combustivel"] for v in viagens)

    media_km_l = distancia_total / combustivel_total if combustivel_total > 0 else 0

    print("\n=== ESTATÍSTICAS ===")
    print(f"Total de viagens: {total}")
    print(f"Distância total: {distancia_total:.2f} km")
    print(f"Combustível total: {combustivel_total:.2f} L")
    print(f"Média do veículo: {media_km_l:.2f} km/L")




def gerar_relatorio():
    viagens = ler_viagens()

    if not viagens:
        print("Nenhuma viagem registrada.")
        return

    total = len(viagens)
    distancia_total = sum(v["distancia"] for v in viagens)
    combustivel_total = sum(v["combustivel"] for v in viagens)
    media_km_l = distancia_total / combustivel_total if combustivel_total > 0 else 0

    viagem_longa = max(viagens, key=lambda x: x["distancia"])
    viagem_curta = min(viagens, key=lambda x: x["distancia"])

    with open(RELATORIO, "w") as f:
        f.write("RELATÓRIO DO SISTEMA\n")
        f.write("-------------------------\n")
        f.write(f"Total de viagens: {total}\n")
        f.write(f"Distância total: {distancia_total:.2f} km\n")
        f.write(f"Combustível total: {combustivel_total:.2f} L\n")
        f.write(f"Média do veículo: {media_km_l:.2f} km/L\n\n")
        f.write(f"Viagem mais longa: {viagem_longa['distancia']} km ({viagem_longa['data']})\n")
        f.write(f"Viagem mais curta: {viagem_curta['distancia']} km ({viagem_curta['data']})\n")

    print("✔ Relatório gerado com sucesso!")





def menu():
    while True:
        print("\n==== SISTEMA DE VIAGENS ====")
        print("1 - Exibir estatísticas")
        print("2 - Registrar nova viagem")
        print("3 - Gerar relatório")
        print("4 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            estatisticas()
        elif opc == "2":
            adicionar_viagem()
        elif opc == "3":
            gerar_relatorio()
        elif opc == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


menu()
