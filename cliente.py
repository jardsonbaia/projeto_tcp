# encoding: utf-8
import socket
#conexao ao servidor  
HOST ="localhost"	
PORT = 5000
# Criando a conexao

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

destino = (HOST, PORT)

tcp.connect(destino)

#tela menu login e senha  
def tela_cadrastro_ou_login():
	print (19*"░" + " Tela de Login" + 20*"░")
	print ("░░░░░░░[1]➔ tele de login"+ 28*"░")
	print ("░░░░░░░[2]➔ Cadrastra_ovo"+ 30*"░")
	menu2 = raw_input("⦾ MENU: ")
	tcp.send(str(menu2).encode())
	if menu2 =="2":
		cadastro_user()
	
def  cadastro_user():
	print("\n ================= CADASTRAR NOVO USUARIO ===================== \n ")
	usuario = raw_input("Digite o nome do usuario: ")
	tcp.send(str(usuario).encode())
	s1 = raw_input("Digite uma senha: ")
	tcp.send(str(s1).encode())
def  login():
	print("\n ================= CADASTRAR NOVO USUARIO ===================== \n ")
	usuario = raw_input("Digite o nome do usuario: ")
	tcp.send(str(usuario).encode())
	s1 = raw_input("Digite uma senha: ")
	tcp.send(str(s1).encode())

# Recebendo a mensagem do usuário final pelo teclado
tela_cadrastro_ou_login()

global livros
livros = []
####le o arquivo com os dados e retorna a lista com os livros
def iniciar_biblioteca():
	arquivo = open("arquivo.txt", "r")

	for linha in arquivo.readlines():
		livros.append(linha)
	arquivo.close()
	return livros

### guardar livro
guardou_livro = False
def guardar_livro():    
	global livros
	titulo = raw_input("Título: ").upper()
	autor = raw_input("Autor: ").upper()
	genero = raw_input("Gênero: ").upper()
	if olhar_estante(titulo, autor)== True:
		print ("\n ⚠ Opps! Você já guardou este livro.\n")
	else:
		livros += [titulo + " ╸ " + autor + " ╸ " + genero + "\n"]
		print ("\n ✔ Livro guardado!\n")
		global guardou_livro
		guardou_livro = True


### olha se um livro está na estante
def olhar_estante(titulo, autor):
	global livro	
	for livro in livros:
		if titulo in livro and autor in livro:
			return True	
		else:
			return False
			
			
		print (livro)	 	    

#ver livros		
def ver_livros():
	if estante_vazia():
		print ("\n ⚠ Estante Vazia!\n")
	else:
		print (15*"⚎" + " LISTA DE LIVROS " + 15*"⚎")
		for i, livro in enumerate(livros):
			print ("  ", i+1, livro)
		print ("".join(livros))
			
# Esvaziar Estante
def esvaziar_estante():
	if not estante_vazia():
		global livros
		livros = []			
	else:
		print ("\n ⚠ A estante já está vazia!\n")

# Olha se a estante estpa vazia
def estante_vazia():
	if len(livros) < 1:
		return True
	else:
		return False

# cria menu
def mostrar_menu():
	print (19*"░" + " MINHA ESTANTE " + 20*"░")
	print ("░░░[1]➔ Guardar Livro        [2]➔ Ver Livros      ░░░░\n░░░[3]➔ Informações          [4]➔ Esvaziar Estante░░░░\n░░░[5]➔ Salvar Alterações    [6]➔ Sair            ░░░░")
	print (17*"░" + " [7] RETIRAR LIVRO " + 18*"░")


### Salva as alterações
salvou = False
def salvar_arquivo():
	arquivo = open("arquivo.txt", "w")
	for livro in livros:
		arquivo.write(livro)
		print (livro)
	arquivo.close()
	global salvou
	salvou = True
	print ("\nAlterações Salvas!\n")

# Informações
def info():
	print ("\n" + 15*"░" + " INFORMAÇÕES " + 15*"░" + "\n")
	print (15*" " + "N. LIVROS: ", len(livros))
	print (43*"┄")			
	print ("         ✳ ÚLTIMO LIVRO GUARDADO ✳ ")
	print (43*"┄")
	print ("   ", livros[-1])

# Remover Livro
def remover_livro():
	if  estante_vazia:
		print ("\n" + 14*"░" + " RETIRAR LIVRO " + 14*"░" + "\n")
		remove =  int(raw_input("Num. Livro: ")) - 1
		if remove > -1 and remove < len(livros):
			del livros[remove]
		else:
			print ("\nNúmero fora da lista!\n")
	else:
		print ("\nEstant	e Vazia!\n")




def iniciar_biblioteca():
	while True:
		mostrar_menu()
		menu = int(raw_input("⦾ MENU: "))
		if menu == 1:
			guardar_livro()
		if menu == 2:
			ver_livros()
		if menu == 3:
			info()
		if menu == 4:
			esvaziar_estante()
		if menu == 5:
			if guardou_livro:
				salvar_arquivo()
			else:
				print ("\n ⚠ Nenhum livro foi guardado!\n")
		if menu == 6:
			if salvou:
				break
			else:
				save = raw_input("\nDeseja Salvar suas alterações?[s/n]: ")
				if save == "s" or save == "S":
					salvar_arquivo()	
					break
				else:
					break
		if menu == 7:
			remover_livro()
	print ("\n░░░░ Fim da consulta!")
		
