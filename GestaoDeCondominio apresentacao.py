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
                    totalConsumo_1 = totalConsumo + totalConsumo
                    totalReservatorio = totalMoradores * totalConsumo_1 / totalMoradores 
                    reservatorio = totalReservatorio + (totalReservatorio * 0.2)
            print(" O Consumo das [TORRE 1 E 2] totaliza {:.2f} litros/dia, sendo nescessário um reservario de \{:.2f} litros ".format(totalReservatorio, reservatorio))
                    
            qres = input("GOSTARIA DE CONTINUAR? S / N:  ").upper()[0]
            if qres in 'S':
                main()
                                                
            else:
                exit()

        if adm == 2:
            for t in range(3, 5):
                    print("-------------- {}º TORRE --------------".format(t))
                    moradores = int(input("Informe total de moradores: "))
                    totalMoradores += moradores
                    consumo = float(input("Informe a media de consumo por apartamento: "))
                    totalConsumo += consumo
                    totalReservatorio = totalConsumo + totalConsumo
                    reservatorio = totalReservatorio + (totalReservatorio * 0.2)
            print(" O Consumo das [TORRE 3 E 4] totaliza {:.2f} litros/dia, sendo nescessário um reservario de \{:.2f} litros ".format(totalReservatorio, reservatorio))
            qres = input("GOSTARIA DE CONTINUAR? S / N:  ").upper()[0]
            if qres in 'S':
                main()
                
            else:
                exit()

        if adm == 3:
            for t in range(5, 7):
                if adm == 3:
                    print("-------------- {}º TORRE --------------".format(t))
                    moradores = int(input("Informe total de moradores: "))
                    totalMoradores += moradores
                    consumo = float(input("Informe a media de consumo por apartamento: "))
                    totalConsumo += consumo
                    totalReservatorio = totalConsumo + totalConsumo
                    reservatorio = totalReservatorio + (totalReservatorio * 0.2)
            print(" O Consumo das [TORRE 5 E 6] totaliza {:.2f} litros/dia, sendo nescessário um reservario de \{:.2f} litros ".format(totalReservatorio, reservatorio))
            qres = input("GOSTARIA DE CONTINUAR? S / N:  ").upper()[0]
            if qres in 'S':
                main()
            else:
                exit()

        if adm == 4:
            for t in range(7, 9):
                if adm == 4:
                    print("-------------- {}º TORRE --------------".format(t))
                    moradores = int(input("Informe total de moradores: "))
                    totalMoradores += moradores
                    consumo = float(input("Informe a media de consumo por apartamento: "))
                    totalConsumo += consumo
                    totalReservatorio = totalConsumo + totalConsumo
                    reservatorio = totalReservatorio + (totalReservatorio * 0.2)
            print(" O Consumo das [TORRE 7 E 8] totaliza {:.2f} litros/dia, sendo nescessário um reservario de \{:.2f} litros ".format(totalReservatorio, reservatorio))
            qres = input("GOSTARIA DE CONTINUAR? S / N:  ").upper()[0]
            if qres in 'Ss':
                main()
            else:
                exit()

        if adm < 1 or adm > 4:
            print("\033[31m OPÇÃO INCORRETA!")
            qres = input("GOSTARIA DE CONTINUAR? S / N:  ").upper()[0]
            if qres in 'S':
                main()
            else:
                exit()


main()
