print("==Validação de Informações==")

nome = str(input("Qual seu nome?")) #variável que recebe o nome
while len(nome) <= 3:   #condição para determinar se o nome tem mais de 3 caracteres
    nome = input("Seu nome deve ter mais que 3 caracteres: ")

idade = int(input("Qual sua idade?")) #variável que recebe a idade
while (idade < 1) or (idade > 150):     #condição para determinar se a idade é maior que 0 e menor que 150
    idade = int(input("Informe uma idade válida entre 1 e 150 anos: "))

salario = float(input("Qual seu salário?")) #variável que recebe o salário
while (salario <= 0):   #condição para determinar se o salário é maior que 0
    salario = float(input("Informe um valor acima de 0: "))

sexo = str(input("Qual seu sexo?(M-masculino/F-feminino)")) #variavel que recebe o sexo da pessoa
while (sexo!= 'f') and (sexo!='m'):     #condição para determinar se o sexo é Masculino ou Feminino
    sexo = str(input("Você deve informar apenas M-masculino ou F-meninino: "))

ec = input("Qual seu Estado Civil atual?(s/c/v/d)") #variável que recebe o Estado Civil da pessoa

while (ec!='s')and(ec!='c')and(ec!='v')and(ec!='d'):    #condição para determinar se o Estado Civil é valido
      print("Informe apenas uma das opções acima!")
      ec = input("Deve ser s, c, v ou d: ")
