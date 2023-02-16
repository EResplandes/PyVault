import mysql.connector
import getpass
import datetime
import os
from datetime import date

# Conexão com o Banco de Dados
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_password',
)

cursor = conexao.cursor()

#Inicio Sistema - Tela de login
data_atual = date.today()

# Cabeçalho do Sistema
print('---------------------------------------------------------------------------------')
print('-------------------- Sistema de Controle de Senhas - PyVault --------------------')
print('---------------------------------------------------------------------------------')
print('--------------------- Seja Bem Vindo - Tela de Autenticação ---------------------')
print('---------------------------------------------------------------------------------')
print('------------------------ Você está sendo monitorado! ----------------------------')
print(f'--------------------------------------------------------------------------------')

#Solicitando Usuário 
usuario = input('Digite seu usuario: ')

#Buscando Usuário no Banco
autenticacao_usuario = f'SELECT nome_usuario FROM tb_usuarios WHERE nome_usuario =  "{usuario}"'
cursor.execute(autenticacao_usuario)
autenticacao_resultado_user = cursor.fetchall()
user_formatado = str(autenticacao_resultado_user)[3:-4]


#Valdiade usuário e senha
if usuario == user_formatado:
    senha_usuario = getpass.getpass('Digite sua senha: ')
    autenticacao_senha = f'SELECT senha_usuario FROM tb_usuarios WHERE senha_usuario =  "{senha_usuario}"'
    cursor.execute(autenticacao_senha)
    autenticacao_resultado_senha = cursor.fetchall()
    senha_formatada = str(autenticacao_resultado_senha)[4:-4]

    if senha_usuario == senha_formatada:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('--------------------------------------------------------------------------------')
        print(f'Seja Bem-vindo, {usuario}!')
        print('--------------------------------------------------------------------------------')


        print('Menu Principal')
        print('1) Cadastrar novo sistema')
        print('2) Verificar informações de sistema')
        print('3) Atualizar informação de sistema')
        opcao_selecionada = input('Selecione umas das opções:')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Modúlo de Cadastro de Sistema
        if (opcao_selecionada == '1'):
            os.system('cls' if os.name == 'nt' else 'clear')
            #Formúlario
            nome_sistema = input('Digite o nome do sistema: ')
            ip_sistema = input('Digite o ip do sistema: ')
            usuario_sistema = input('Digite o nome do usuario: ')
            senha_sistema = getpass.getpass('Digite a senha do sistema: ')

            #Executando o cadastro do sistema
            cadastra_sistema = f'CALL sp_insert_sistema ("{nome_sistema}", "{ip_sistema}", "{usuario_sistema}" , "{senha_sistema}")'
            cursor.execute(cadastra_sistema) 
            conexao.commit()

            #Verificando se o cadastro foi realizado com sucesso
            valida_cadastro_sistema = f'SELECT ip_sistema FROM tb_sistemas WHERE ip_sistema = "{ip_sistema}" LIMIT 1'
            cursor.execute(valida_cadastro_sistema)
            autenticacao_resultado_cad_sis = cursor.fetchall()
            valida_formatado = str(autenticacao_resultado_cad_sis)[3:-4]

            if valida_formatado == ip_sistema:
                    print('Sistema cadastrado com sucesso!')
            else:
                    print(valida_formatado)
                    print('Erro no cadastro, tente novamente!')
        #Fim Modúlo de Cadastro de Sistema 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Modúlo de Verificação de Sistema
        elif (opcao_selecionada == '2'):

            os.system('cls' if os.name == 'nt' else 'clear')
            print('Filtros disponíveis: ')
            print('1) Buscar pelo nome ')
            print('2) Buscar pelo ip')
            guarda_opcao = input('Selecione uma das opções:  ')

            if (guarda_opcao == '1'):

                os.system('cls' if os.name == 'nt' else 'clear')
                busca_nome = input('Digite o nome do sistema: ')

                #busca o nome do sistema
                query_busca_nome_sistema = f'SELECT nome_sistema FROM tb_sistemas WHERE nome_sistema LIKE "%{busca_nome}%" LIMIT 1'
                cursor.execute(query_busca_nome_sistema)
                query_busca_nome_sistema_resultado = cursor.fetchall()
                query_busca_nome_sistema_resultado_formatado = str(query_busca_nome_sistema_resultado)[3:-4]

                #Busca o ip do sistema
                query_busca_ip_sistema = f'SELECT  ip_sistema FROM tb_sistemas WHERE nome_sistema LIKE "%{busca_nome}%" LIMIT 1'
                cursor.execute(query_busca_ip_sistema)
                query_busca_ip_sistema_resultado = cursor.fetchall()
                query_busca_ip_sistema_resultado_formatado = str(query_busca_ip_sistema_resultado)[3:-4]

                #Busca o usuário do sistema
                query_busca_usuario_sistema = f'SELECT usuario_sistema FROM tb_sistemas WHERE nome_sistema LIKE "%{busca_nome}%" LIMIT 1'
                cursor.execute(query_busca_usuario_sistema)
                query_busca_usuario_sistema_resultado = cursor.fetchall()
                query_busca_usuario_sistema_resultado_formatado = str(query_busca_usuario_sistema_resultado)[3:-4]

                #Busca a senha do sistema
                query_busca_senha_sistema =  f'SELECT senha_sistema FROM tb_sistemas WHERE nome_sistema LIKE "%{busca_nome}%" LIMIT 1'
                cursor.execute(query_busca_senha_sistema)
                query_busca_senha_sistema_resultado = cursor.fetchall()
                query_busca_senha_sistema_resultado_formatado = str(query_busca_senha_sistema_resultado)[4:-4]

                os.system('cls' if os.name == 'nt' else 'clear')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('Aqui estão as seguintes informações:')
                print('--------------------------------------------------------------------------------------------------------------------')
                print(f'Nome do Sistema: {query_busca_nome_sistema_resultado_formatado}')
                print(f'Ip do Sistema: {query_busca_ip_sistema_resultado_formatado}')
                print(f'Usuário do Sistema: {query_busca_usuario_sistema_resultado_formatado}')
                print(f'Senha do Sistema: {query_busca_senha_sistema_resultado_formatado}')


            elif(guarda_opcao == '2'): 
                 
                os.system('cls' if os.name == 'nt' else 'clear')
                busca_ip = input('Digite o ip do sistema: ')

                query_busca_nome_sistema = f'SELECT nome_sistema FROM tb_sistemas WHERE ip_sistema LIKE "%{busca_ip}%" LIMIT 1'
                cursor.execute(query_busca_nome_sistema)
                query_busca_nome_sistema_resultado = cursor.fetchall()
                query_busca_nome_sistema_resultado_formatado = str(query_busca_nome_sistema_resultado)[3:-4]

                #Busca o ip do sistema
                query_busca_ip_sistema = f'SELECT  ip_sistema FROM tb_sistemas WHERE ip_sistema LIKE "%{busca_ip}%" LIMIT 1'
                cursor.execute(query_busca_ip_sistema)
                query_busca_ip_sistema_resultado = cursor.fetchall()
                query_busca_ip_sistema_resultado_formatado = str(query_busca_ip_sistema_resultado)[3:-4]

                #Busca o usuário do sistema
                query_busca_usuario_sistema = f'SELECT usuario_sistema FROM tb_sistemas WHERE ip_sistema LIKE "%{busca_ip}%" LIMIT 1'
                cursor.execute(query_busca_usuario_sistema)
                query_busca_usuario_sistema_resultado = cursor.fetchall()
                query_busca_usuario_sistema_resultado_formatado = str(query_busca_usuario_sistema_resultado)[3:-4]

                #Busca a senha do sistema
                query_busca_senha_sistema =  f'SELECT senha_sistema FROM tb_sistemas WHERE ip_sistema LIKE "%{busca_ip}%" LIMIT 1'
                cursor.execute(query_busca_senha_sistema)
                query_busca_senha_sistema_resultado = cursor.fetchall()
                query_busca_senha_sistema_resultado_formatado = str(query_busca_senha_sistema_resultado)[4:-4]

                os.system('cls' if os.name == 'nt' else 'clear')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('Aqui estão as seguintes informações:')
                print('--------------------------------------------------------------------------------------------------------------------')
                print(f'Nome do Sistema: {query_busca_nome_sistema_resultado_formatado}')
                print(f'Ip do Sistema: {query_busca_ip_sistema_resultado_formatado}')
                print(f'Usuário do Sistema: {query_busca_usuario_sistema_resultado_formatado}')
                print(f'Senha do Sistema: {query_busca_senha_sistema_resultado_formatado}')

            else:
                print('Opção Inválida!')
        #Fim Módulo de Verificação de Sistema 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
         #Modúlo de Atualização de Sistema
        elif (opcao_selecionada == '3'):
             print('atualizar')
        elif (opcao_selecionada == '4'):
             print('sei la')
        else:
            print('Atualizar')

    else:
        print('Senha incorreta!')
    
else:
    print('Usuário incorreto!')


cursor.close()
conexao.close()