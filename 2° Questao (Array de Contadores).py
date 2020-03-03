salarios = [[200,299],[300,399],[400,499],[500,599],[600,699],[700,799],[800,899],[900,999]] #Lista com os possiveis salarios
faixa = [0,0,0,0,0,0,0,0,0] #Lista de interligação com a de salários

print ("===Digite 0 para encerrar a contagem de vendas!===")
vendas = int(input("Informe o valor das vendas: ")) #Variável para receber os valor de venda dos produtos

while vendas != 0: #Condição para que o calculo do salário seja feito ate o 0 ser acionado
    salario = (vendas*0.09)+200 #Calculo para determinar o salário do funcionário
    if salario < 1000:
        for i in range(8): #Condição para que o indice seja um dos 8 da lista
            if salario > salarios[i][0] and salario < salarios[i][1]:
                faixa[i] += 1
    else:
        faixa[8] += 1
    vendas = int(input("Digite o valor das vendas:"))

for i in range(8): #Acionando o print para todos os resultados com indice entre os 8 lista
    print ("Funcionarios que receberam entre R$",salarios[i][0],"e R$",salarios[i]
[1],":",faixa[i],"vendedores.")
print ("Funcionarios que receberam salários maiores que R$1000:",faixa[8],"vendedores.")
