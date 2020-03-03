print ("=====Financiamento====")

f = float(input("Qual o valor para o financiamento? ")) #Variável para o valor de financiamento do produto
taxa = float(input("Qual a taxa aplicada sobre o financiamento em reais? ")) #Variável para a taxa de financiamento aplicada sobre o produto
p = int(input("Qual o parcelamento desejado? (24,36,48 ou 60)")) #Variável para o parcelamento escolhido
juros = 0.002 #Valor da taxa de juros ao mês

while (p!=24) and (p!=36) and (p!=48) and (p!=60): #Definição da condição para que o parcelamento seja apenas um dentre os informados
    print("Informe o parcelamento novamente!")
    p = int(input("Qual o parcelamento desejado? (24,36,48 ou 60)"))

financiamento = f+(juros*p)+taxa #Variável que recebe o calculo do Financiamento Total

vp = f/p  #Equação para determinar o valor de cada parcela
pcj = (vp*0.002) + vp  #Equação para definir o valor das parcelas com o juros aplicado ao mês
print("O valor de pagamento das parcelas é de: {:.2f} R$" .format(pcj))
print("O valor total do financiamento é de: {:.2f} R$" .format(financiamento))



