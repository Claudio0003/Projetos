renda_mensal = float(input('Entra a sua renda mensal: '))

# ( Porcentagem a ser removida / 100 ) * Renda_Mensal
obter_50_porcento = (50 / 100) * renda_mensal
obter_30_porcento = (30 / 100) * renda_mensal
obter_20_porcento = (20 / 100) * renda_mensal

print("=====================\nSeus numeros de 50% 30% 20%\n======================")

print('Necessidades: R${:,.2f}'.format(obter_50_porcento))
print('Gastos: R${:,.2f}'.format(obter_30_porcento))
print('Poupança: R${:,.2f}'.format(obter_20_porcento))

print("]n=========================================================================")