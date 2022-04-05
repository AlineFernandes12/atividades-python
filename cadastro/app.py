usuario = input("Entre com o seu nome: ")
 print(f"Seja Bem-vindo {usuario} !\n")
 compras = []
 while True:
     print("Selecione uma opção:")
     print("1 - Cadastrar")
     print("2 - Listar")
     print("3 - Sair")
     print("4 - Excluir")
     opcao = int(input(""))
     if opcao in [1,2,3,4]:
         if opcao == 1: #Cadastrar
             nome = ""
             while nome == "":
                 nome = input("Coloque o nome do item de compra: ")
             lista.append(registro)
             print("Sucesso! Cadastrado!")
         elif opcao == 2: #Listar
             for item in lista:
                 print(item)
             
         elif opcao == 3:#Sair
             print("Saindo do sistema...")
             break

         elif opcao == 4:#Excluir
             print ("Excluindo produto!") 
             opcao.pop()

     else:
         print("Opção Inválida!")