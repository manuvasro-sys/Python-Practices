# Python-Practices
# Codédex Currency Practice
co = int(input('What do you have left in pesos? ')) 
pe = int(input('What do you have left in soles? '))
br = int(input('What do you have left in reais? '))
total_usd = (co * 0.00029) + (pe * 0.30) + (br * 0.19)
print(total_usd)
