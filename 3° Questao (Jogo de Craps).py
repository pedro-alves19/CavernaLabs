from random import randint  # Importando biblioteca para fazer a randonização dos numeros

nome = input("Qual seu nome jogador? ") #Variável para receber o nome do jogador

dado = {f'O jogador {nome}': randint(2,12)} #Variável que serve de dado para sortear os numeros

for k, v in dado.items(): #Função para captação do numero sorteado
    if (v == 7) or (v == 11): #Verificando se o numero é vencedor
        print(f'{k} tirou {v} no dado!')
        print(f'{nome} você é Natural você Ganhou Parabéns!')
    elif (v == 2) or (v == 3) or (v == 12): #Verificando se o numero é perdedor
        print(f'{k} tirou {v} no dado!')
        print(f'{nome} que pena, isso foi um Crap..você Perdeu!')
    else:  #Informando o numero do ponto do jogador
        print(f'{k} tirou {v} no dado!')
        print(f'{nome} este numero é seu Ponto agora!')
        jogo2 = str(input('Deseja jogar novamente? (S/N)')) #Variável para opção de jogar novamente
        if (jogo2 == 's'):
            dado2 = {f'O jogador {nome}': randint(2,12)} #Variável para o segundo dado a ser jogado
            while(dado2 != dado): #Condição para o dado ser lançado enquanto este for diferente do primeiro
                dado2 = {f'O jogador {nome}': randint(2,12)}
            if (dado2 == dado): #Verificando se o segundo dado é igual ao primeiro
                print(f'{k} tirou {v} no dado!')
                print(f'{nome} Parabéns você Ganhou!')
            elif (dado2 == 7): #Verificando se o segundo dado é igual a 7
                print(f'{k} tirou {v} no dado!')
                print(f'{nome} que pena, esse foi um 7, você Perdeu!')            
            else:
                dado2 = {f'O jogador {nome}': randint(2,12)}
        else:
            exit()


