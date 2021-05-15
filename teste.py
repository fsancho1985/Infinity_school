print("="*20, "CÁLCULO DE CONSUMO DE ÁGUA RESIDENCIAL", "="*20)



print(""" 
RESERVATÓRIOS:

[ 1 ] TORRE 1 E TORRE 2
[ 2 ] TORRE 3 E TORRE 4
[ 3 ] TORRE 5 E TORRE 6
[ 4 ] TORRE 7 E TORRE 8
""")

def main():
        adm = int(input(" Escolha o reservatório para obter dados das unidades: "))
        totalMoradores = 0
        totalConsumo = 0
        if adm == 1:
            for t in range(1, 3):
                    print("-------------- {}º TORRE --------------".format(t))
                    moradores = int(input("Informe total de moradores: "))
                    totalMoradores += moradores
                    consumo = float(input("Informe a media de consumo por apartamento: "))
                    totalConsumo += consumo
                    #consumoDiario = totalMoradores * totalConsumo
                    reservatorio = totalConsumo + (totalConsumo * 0.2)
                    #consumoDiario + (consumoDiario * 20 / 100)
            print(" O Consumo das [TORRE 1 E 2] totaliza {:.2f} litros/dia, sendo nescessário um reservario de \
             {:.2f} litros ".format(consumoDiario, reservatorio))
            qres = str(input("GOSTARIA DE CONTINUAR? S / N:  ")).strip().upper()[0]
            if qres in 'S':
                main()
                adm = int(input(" Escolha o reservatório para obter dados das unidades: "))
            else:
                print("Opção inválida! Insira nova opção: ")
                while qres != 'S':
                    qres = str(input("GOSTARIA DE CONTINUAR? S / N:  ")).strip().upper()[0]
                main()
                exit()
