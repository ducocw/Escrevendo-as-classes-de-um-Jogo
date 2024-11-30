nome = input("Nome do herói: ")
idade = input("Idade: ")
tipo = int(input("""
             Profissão do Herói:
             1) Mago
             2) Guerreiro
             3) Monge
             4) Ninja
             """
             ))
class Heroi:
    def __init__(self, nome, idade, tipo):
        nome = nome
        idade = idade
        tipo = tipo

   
    if tipo == 1:
        maestria = "magia"
        classe = "Mago"
        
    elif tipo == 2:
        maestria = "espada"
        classe = "Guerreiro"
    
    elif tipo == 3:
        maestria = "artes marciais"
        classe = "Monge"

    elif tipo == 4:
        maestria = "shuriken"
        classe = "Ninja"
        
    else:
        maestria = "Nenhuma"
        classe = "Ninguém"
    
    print(f"O {classe} tem melhor habilidade em {maestria}.")
