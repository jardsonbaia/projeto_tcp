import psycopg2
import socket

HOST = "localhost"    # Endereco IP do Servidor

PORT = 5000            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

origem = (HOST, PORT)

# Colocando um endereco IP e uma porta no Socket

tcp.bind(origem)

# Colocando o Socket em modo passivo

tcp.listen(1)

print('\nServidor TCP iniciado no IP', HOST, 'na porta', PORT)

while True:

   # Aceitando uma nova conexao

   conexao, cliente = tcp.accept()

   print('\nConexao realizada por:', cliente)

   while True:
	   mensagem = conexao.recv(1024)
	   if mensagem == 1:
		   print "test"
	   if mensagem == 2:
		   cadastro_user()			

       # Exibindo a mensagem recebida

print('\nCliente..:', cliente)

print('Mensagem.:', mensagem.decode())

print('Finalizando conexao do cliente', cliente)

   # Fechando a conexao com o Socket
conexao.close()

def  cadastro_user():
	print("\n ================= CADASTRAR NOVO USUARIO ===================== \n ")
	 # Recebendo as mensagens atraves da conexao o nome do usuario
	usuario = conexao.recv(1024)  
	s1 = conexao.recv(1024)
	senha=s1
	# Connect to an existing database
	conn = psycopg2.connect(dbname='testcon', user='postgres',password='was12ret',host='localhost')
# Open a cursor to perform database operations
	cur = conn.cursor()
	#Verificar se usuario ja existe
	cur.execute("SELECT login FROM cadotro_usuario;")
	rows = cur.fetchall()
	for row in rows:
		i=0
		if row[i] == usuario:
			print "usuario ja existe"
			break;
		else:
			login = usuario
		#guardar_usuario no banco de dados 
			cur.execute("INSERT INTO cadotro_usuario (login,senha ) VALUES (%s, %s)",(login,senha))
			print("\n  Usuario cadastrado!\n")
			conn.commit()
			break;
		i=i+1
# Make the changes to the database persistent
	conn.commit()

# Close communication with the database
	cur.close()
	conn.close()
	
def guardar_livro():
	conn = psycopg2.connect(dbname='testcon', user='postgres',password='was12ret',host='localhost')
# Open a cursor to perform database operations
	cur = conn.cursor()
	#cur.execute("CREATE TABLE livros (id serial PRIMARY KEY, titulo varchar,autor varchar,genero  varchar);")
	global livros
	titulo = raw_input("Titulo: ")
	autor = raw_input("Autor: ")
	genero = raw_input("Genero: ")
	if olhar_estante(titulo, autor)== True:
		print ("\n  Opps! Voce ja guardou este livro.\n")
	else:
		#guardar_usuario no banco de dados 
			cur.execute("INSERT INTO livros (login,senha ) VALUES (%s, %s,%s)",(titulo,autor,genero))
			print ("\n Livro guardado\n")
			conn.commit()



#conexao com  o banco de dados
import psycopg2



# Execute a command: this creates a new table
cur.execute("CREATE TABLE cadotro_usuario (id serial PRIMARY KEY, login varchar,senha varchar);")

        
	








