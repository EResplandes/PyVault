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
os.system('cls' if os.name == 'nt' else 'clear')
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

        query_busca_tipo_usuario = f'SELECT tipo_usuario FROM tb_usuarios WHERE nome_usuario = "{usuario}"'
        cursor.execute(query_busca_tipo_usuario)
        query_busca_tipo_usuario_resultado = cursor.fetchall()
        query_busca_tipo_usuario_resultado_formatado = str(query_busca_tipo_usuario_resultado)[3:-4]

        print('')
        print('Menu Principal')
        print('')
        print('1) Cadastrar novo sistema')
        print('2) Verificar informações de sistema')
        print('3) Atualizar informação de sistema')   
        print('4) Exclusão de sistema')
        print('5) Cadastro de Usuário')
        print('6) Exclusão de Usuário')
        print('7) Verifica todos sistemas')
        print('')
        opcao_selecionada = input('Selecione umas das opções:')
        

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Modúlo de Cadastro de Sistema''
        if (opcao_selecionada == '1'):
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('--------------------------------------- Modúlo de Cadastro de Sistemas ---------------------------------------------')
            print('--------------------------------------------------------------------------------------------------------------------')
            nome_sistema = input('Digite o nome do sistema: ')

            os.system('cls' if os.name == 'nt' else 'clear')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('--------------------------------------- Modúlo de Cadastro de Sistemas ---------------------------------------------')
            print('--------------------------------------------------------------------------------------------------------------------')
            ip_sistema = input('Digite o ip do sistema: ')

            os.system('cls' if os.name == 'nt' else 'clear')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('--------------------------------------- Modúlo de Cadastro de Sistemas ---------------------------------------------')
            print('--------------------------------------------------------------------------------------------------------------------')
            usuario_sistema = input('Digite o nome do usuario: ')

            os.system('cls' if os.name == 'nt' else 'clear')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('--------------------------------------- Modúlo de Cadastro de Sistemas ---------------------------------------------')
            print('--------------------------------------------------------------------------------------------------------------------')
            senha_sistema = getpass.getpass('Digite a senha do sistema: ')

            os.system('cls' if os.name == 'nt' else 'clear')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('--------------------------------------- Modúlo de Cadastro de Sistemas ---------------------------------------------')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('')
            print('Tipos do sistema: ')
            print('1) Sistema Web')
            print('2) Sistema')
            print('3) Máquina Virtual')
            print('4) Servidor')
            print('5) Banco de dados')
            print('')
            tipo_sistema = input('Digite o tipo do sistema: ')
            
            #Executando o cadastro do sistema
            cadastra_sistema = f'INSERT INTO tb_sistemas (nome_sistema, ip_sistema, usuario_sistema, senha_sistema, id_tipo_sistema) VALUES ("{nome_sistema}", "{ip_sistema}", "{usuario_sistema}" , "{senha_sistema}", "{tipo_sistema}")'
            cursor.execute(cadastra_sistema) 
            conexao.commit()

            #Inserir Log de Cadastro
            mensagem = f'O usuário {usuario} cadastrou um novo sistema: {nome_sistema}!'

            insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
            cursor.execute(insert_log_cadastro)
            conexao.commit()

            #Verificando se o cadastro foi realizado com sucesso
            valida_cadastro_sistema = f'SELECT ip_sistema FROM tb_sistemas WHERE ip_sistema = "{ip_sistema}" LIMIT 1'
            cursor.execute(valida_cadastro_sistema)
            autenticacao_resultado_cad_sis = cursor.fetchall()
            valida_formatado = str(autenticacao_resultado_cad_sis)[3:-4]

            if valida_formatado == ip_sistema:
                     
                     os.system('cls' if os.name == 'nt' else 'clear')
                     print('--------------------------------------------------------------------------------------------------------------------')
                     print('--------------------------------------- Modúlo de Cadastro de Sistemas ---------------------------------------------')
                     print('--------------------------------------------------------------------------------------------------------------------')
                     print('Sistema cadastrado com sucesso!')
                     print('')
                     input('Pressione Enter para sair...')
            else:
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('--------------------------------------- Modúlo de Cadastro de Sistemas ---------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('Erro no cadastro, tente novamente!')
                    print('')
                    input('Pressione Enter para sair...')
        #Fim Modúlo de Cadastro de Sistema 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Modúlo de Verificação de Sistema
        elif (opcao_selecionada == '2'):

            os.system('cls' if os.name == 'nt' else 'clear')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('-------------------------------------- Modúlo de Verificação de Sistemas -------------------------------------------')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('')
            print('Filtros disponíveis: ')
            print('')
            print('1) Buscar pelo nome ')
            print('2) Buscar pelo ip')
            print('')
            guarda_opcao = input('Selecione uma das opções:  ')

            if (guarda_opcao == '1'):
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('-------------------------------------- Modúlo de Verificação de Sistemas -------------------------------------------')
                print('--------------------------------------------------------------------------------------------------------------------')
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
                print('-------------------------------------- Modúlo de Verificação de Sistemas -------------------------------------------')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('')
                print('Aqui estão as informações do sistema: ')
                print('')
                print(f'Nome do Sistema: {query_busca_nome_sistema_resultado_formatado}')
                print(f'Ip do Sistema: {query_busca_ip_sistema_resultado_formatado}')
                print(f'Usuário do Sistema: {query_busca_usuario_sistema_resultado_formatado}')
                print(f'Senha do Sistema: {query_busca_senha_sistema_resultado_formatado}')
                print('')
                input('Pressione Enter para sair...')
               #Inserir Log de Cadastro
                mensagem = f'O {usuario} buscou as informações do sistema: {busca_nome}!'
                insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                cursor.execute(insert_log_cadastro)
                conexao.commit()

            elif(guarda_opcao == '2'): 
                 
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('-------------------------------------- Modúlo de Verificação de Sistemas -------------------------------------------')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('') 
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
                print('-------------------------------------- Modúlo de Verificação de Sistemas -------------------------------------------')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('')
                print('Aqui estão as informações do sistema: ')
                print('')
                print(f'Nome do Sistema: {query_busca_nome_sistema_resultado_formatado}')
                print(f'Ip do Sistema: {query_busca_ip_sistema_resultado_formatado}')
                print(f'Usuário do Sistema: {query_busca_usuario_sistema_resultado_formatado}')
                print(f'Senha do Sistema: {query_busca_senha_sistema_resultado_formatado}')
                print('')
                input('Pressione Enter para sair...')

                #Inserir Log de Cadastro
                mensagem = f'O {usuario} buscou as informações do sistema: {busca_ip}!'
                insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                cursor.execute(insert_log_cadastro)
                conexao.commit()

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('-------------------------------------- Modúlo de Verificação de Sistemas -------------------------------------------')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('Opção Inválida!')
                print('')
                input('Pressione Enter para sair...')
        #Fim Módulo de Verificação de Sistema 
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
         #Modúlo de Atualização de Sistema
        elif (opcao_selecionada == '3'):
            
            print('--------------------------------------------------------------------------------------------------------------------')
            print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('')
            print('1) Buscar pelo nome:  ')
            print('2) Buscar pelo Ip: ')
            print('')
            guarda_opcao_a = input('Selecione o parametrô de busca:')

            if (guarda_opcao_a == '1'):
                 os.system('cls' if os.name == 'nt' else 'clear')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 print('')
                 pede_nome = input('Insira o nome do sistema que deseja atualizar a informação: ')
                 qyery_busca_sistema_nome = f'SELECT nome_sistema FROM tb_sistemas WHERE nome_sistema LIKE "%{pede_nome}%"'
                 cursor.execute(qyery_busca_sistema_nome)
                 qyery_busca_sistema_nome_resultado = cursor.fetchall()
                 qyery_busca_sistema_nome_resultado_formatado = str(qyery_busca_sistema_nome_resultado)[3:-4]

                 os.system('cls' if os.name == 'nt' else 'clear')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 print('')
                 print('Selecione o parametrô que deseja atualizar: ')
                 print('')
                 print('1) Atualizar nome do sistema: ')
                 print('2) Atualizar ip do sistema: ')
                 print('3) Atualizar usuário do sistema: ')
                 print('4) Atualizar senha do sistema: ')
                 print('')
                 guarda_parametro_atualizacao = input('Selecione o parametrô que deseja atualizar: ')
                
                 if (guarda_parametro_atualizacao == '1'):
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    guarda_parametro_atualizacao_novo_nome = input('Informe o novo nome do sistema: ') 

                    atualiza_nome = f'UPDATE tb_sistemas SET nome_sistema = "{guarda_parametro_atualizacao_novo_nome}" WHERE  nome_sistema = "{qyery_busca_sistema_nome_resultado_formatado}"'
                    cursor.execute(atualiza_nome)
                    conexao.commit()
                    
                    #Inserir Log de Cadastro
                    mensagem = f'O {usuario} atualizou o nome do sistema: {qyery_busca_sistema_nome_resultado_formatado} para {guarda_parametro_atualizacao_novo_nome}!'

                    insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                    cursor.execute(insert_log_cadastro)
                    conexao.commit()

                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    print('Atualização realizada com sucesso!')
                    print('')
                    input('Pressione Enter para sair...')

                 elif (guarda_parametro_atualizacao == '2'):
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    guarda_parametro_atualizacao_novo_ip = input('Informe o novo ip do sistema: ')

                    atualiza_ip = f'UPDATE tb_sistemas SET ip_sistema = "{guarda_parametro_atualizacao_novo_ip}" WHERE nome_sistema = "{qyery_busca_sistema_nome_resultado_formatado}"'
                    cursor.execute(atualiza_ip)
                    conexao.commit()

                    #Inserir Log de Cadastro
                    mensagem = f'O {usuario} atualizou o ip do sistema: {qyery_busca_sistema_nome_resultado_formatado} para {guarda_parametro_atualizacao_novo_ip}!'
                    
                    insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                    cursor.execute(insert_log_cadastro)
                    conexao.commit()
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    print('Atualização realizada com sucesso!')
                    print('')
                    input('Pressione Enter para sair...')

                 elif (guarda_parametro_atualizacao == '3'):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    guarda_parametro_atualizacao_novo_usuario = input('Informe o novo nome do usuário sistema: ')

                    atualiza_usuario = f'UPDATE tb_sistemas SET usuario_sistema = "{guarda_parametro_atualizacao_novo_usuario}" WHERE nome_sistema = "{qyery_busca_sistema_nome_resultado_formatado}"'
                    cursor.execute(atualiza_usuario)
                    conexao.commit()
                   
                    #Logs
                    mensagem = f'O {usuario} atualizou o usuario do sistema: {qyery_busca_sistema_nome_resultado_formatado} para {guarda_parametro_atualizacao_novo_usuario}!'
                    
                    insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                    cursor.execute(insert_log_cadastro)
                    conexao.commit()


                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    print('Atualização realizada com sucesso!')
                    print('')
                    input('Pressione Enter para sair...')

                 elif (guarda_parametro_atualizacao == '4'):
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    guarda_parametro_atualizacao_nova_senha = getpass.getpass('Informe a nova senha sistema: ')
                    
                    atualiza_senha = f'UPDATE tb_sistemas SET senha_sistema = "{guarda_parametro_atualizacao_nova_senha}" WHERE nome_sistema = "{qyery_busca_sistema_nome_resultado_formatado}"'
                    cursor.execute(atualiza_senha)
                    conexao.commit()

                    #Logs
                    mensagem = f'O {usuario} atualizou a senha do sistema: {qyery_busca_sistema_nome_resultado_formatado} para {guarda_parametro_atualizacao_nova_senha}!'
                    
                    insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                    cursor.execute(insert_log_cadastro)
                    conexao.commit()

                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    print('Atualização realizada com sucesso!')
                    print('')
                    input('Pressione Enter para sair...')

                 else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    print('Parametrô inválido!')
                    print('')
                    input('Pressione Enter para sair...')
                   

            elif (guarda_opcao_a == '2'):
                 os.system('cls' if os.name == 'nt' else 'clear')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 print('')
                 pede_ip = input('Insira o ip do sistema que deseja atualizar a informação: ')
                 qyery_busca_sistema_ip = f'SELECT ip_sistema FROM tb_sistemas WHERE ip_sistema = "{pede_ip}"'
                 cursor.execute(qyery_busca_sistema_ip)
                 qyery_busca_sistema_ip_resultado = cursor.fetchall()
                 qyery_busca_sistema_ip_resultado_formatado = str(qyery_busca_sistema_ip_resultado)[3:-4]

                 os.system('cls' if os.name == 'nt' else 'clear')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 print('')
                 print('1) Atualizar nome do sistema: ')
                 print('2) Atualizar ip do sistema: ')
                 print('3) Atualizar usuário do sistema: ')
                 print('4) Atualizar senha do sistema: ')
                 print('')
                 guarda_parametro_atualizacao = input('Selecione o parametrô que deseja atualizar: ')
                
                 if (guarda_parametro_atualizacao == '1'):
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    guarda_parametro_atualizacao_novo_nome = input('Informe o novo nome do sistema: ') 

                    atualiza_nome = f'UPDATE tb_sistemas SET nome_sistema = "{guarda_parametro_atualizacao_novo_nome}" WHERE  ip_sistema = "{qyery_busca_sistema_ip_resultado_formatado}"'
                    cursor.execute(atualiza_nome)
                    conexao.commit()

                    #Logs
                    mensagem = f'O {usuario} atualizou o nome do sistema: {pede_ip} para {guarda_parametro_atualizacao_novo_nome}!'
                    
                    insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                    cursor.execute(insert_log_cadastro)
                    conexao.commit()

                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    print('Atualização realizada com sucesso!')
                    print('')
                    input('Pressione Enter para sair...')

                 elif (guarda_parametro_atualizacao == '2'):
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    guarda_parametro_atualizacao_novo_ip = input('Informe o novo ip do sistema: ')

                    atualiza_ip = f'UPDATE tb_sistemas SET ip_sistema = "{guarda_parametro_atualizacao_novo_ip}" WHERE ip_sistema = "{qyery_busca_sistema_ip_resultado_formatado}"'
                    cursor.execute(atualiza_ip)
                    conexao.commit()

                    #Logs
                    mensagem = f'O {usuario} atualizou o ip do sistema: {pede_ip} para {guarda_parametro_atualizacao_novo_ip}!'
                    
                    insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                    cursor.execute(insert_log_cadastro)
                    conexao.commit()

                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    print('Atualização realizada com sucesso!')
                    print('')
                    input('Pressione Enter para sair...')

                 elif (guarda_parametro_atualizacao == '3'):
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    guarda_parametro_atualizacao_novo_usuario = input('Informe o novo nome do usuário sistema: ')

                    atualiza_usuario = f'UPDATE tb_sistemas SET usuario_sistema = "{guarda_parametro_atualizacao_novo_usuario}" WHERE ip_sistema = "{qyery_busca_sistema_ip_resultado_formatado}"'
                    cursor.execute(atualiza_usuario)
                    conexao.commit()

                    #Logs
                    mensagem = f'O {usuario} atualizou o usuario do sistema: {pede_ip} para {guarda_parametro_atualizacao_novo_usuario}!'
                    
                    insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                    cursor.execute(insert_log_cadastro)
                    conexao.commit()
                   
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    print('Atualização realizada com sucesso!')
                    print('')
                    input('Pressione Enter para sair...')

                 elif (guarda_parametro_atualizacao == '4'):
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    guarda_parametro_atualizacao_nova_senha = input('Informe a nova senha sistema: ')
                    
                    atualiza_senha = f'UPDATE tb_sistemas SET senha_sistema = "{guarda_parametro_atualizacao_nova_senha}" WHERE ip_sistema = "{qyery_busca_sistema_ip_resultado_formatado}"'
                    cursor.execute(atualiza_senha)
                    conexao.commit()

                    #Logs
                    mensagem = f'O {usuario} atualizou a senha do sistema: {pede_ip} para {guarda_parametro_atualizacao_nova_senha}!'
                    
                    insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                    cursor.execute(insert_log_cadastro)
                    conexao.commit()


                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    print('Atualização realizada com sucesso!')
                    print('')
                    input('Pressione Enter para sair...')


                 else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('')
                    print('Parametrô inválido!')
                    print('')
                    input('Pressione Enter para sair...')
                   
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('')
                print('Atualização realizada com sucesso!')
                print('')
                input('Pressione Enter para sair...')


# Fim do Modúlo de Atualização de Sistema
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Início do Modúlo de Exclusão de Sistema - Administrador
        elif (opcao_selecionada == '4') and (query_busca_tipo_usuario_resultado_formatado == 'Administrador'):
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('')
            print('1) Busca o sistema pelo nome')
            print('2) Buscar o sistema pelo ip')
            print('')
            guarda_opcao_e = input('Selecione o método de busca: ')

            if (guarda_opcao_e == '1'):

               os.system('cls' if os.name == 'nt' else 'clear')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('')
               guarda_informacao_e_nome = input('Informe o nome do sistema que deseja excluir: ')

               query_busca_exclu_sis_nome = f'SELECT * FROM tb_sistemas WHERE nome_sistema = "{guarda_informacao_e_nome}"'
               cursor.execute(query_busca_exclu_sis_nome)
               query_busca_exclu_sis_nome_resultado = cursor.fetchall()
               query_busca_exclu_sis_nome_resultado_formatado = str(query_busca_exclu_sis_nome_resultado)

               os.system('cls' if os.name == 'nt' else 'clear')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('')
               print(query_busca_exclu_sis_nome_resultado_formatado) 
               print('')
               guarda_confirmacao_exclusao = input('Deseja realmente excluir esse sistema? Se sim digite "s" se deseja cancelar essa operação digite "n": ')

               if (guarda_confirmacao_exclusao == 's'):
                   
                   os.system('cls' if os.name == 'nt' else 'clear')
                   print('--------------------------------------------------------------------------------------------------------------------')
                   print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
                   print('--------------------------------------------------------------------------------------------------------------------')
                   print('')
                   query_exclusao_confirmada = f'DELETE FROM tb_sistemas WHERE nome_sistema = "{guarda_informacao_e_nome}"'
                   cursor.execute(query_exclusao_confirmada)
                   conexao.commit()

                   #Logs
                   mensagem = f'O {usuario} excluiu o sistema: {guarda_informacao_e_nome}!'
                    
                   insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                   cursor.execute(insert_log_cadastro)
                   conexao.commit()

                   os.system('cls' if os.name == 'nt' else 'clear')

                   print('--------------------------------------------------------------------------------------------------------------------')
                   print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
                   print('--------------------------------------------------------------------------------------------------------------------')
                   print('')
                   print('A exclusão foi realizada com sucesso!')
                   print('')
                   input('Pressione Enter para sair...')
                   

               elif (guarda_confirmacao_exclusao == 'n'):
                   
                   os.system('cls' if os.name == 'nt' else 'clear')
                   print('--------------------------------------------------------------------------------------------------------------------')
                   print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
                   print('--------------------------------------------------------------------------------------------------------------------')
                   print('')
                   print('Operação cancelada!')
                   print('')
                   input('Pressione Enter para sair...')

               else:

                  os.system('cls' if os.name == 'nt' else 'clear')
                  print('--------------------------------------------------------------------------------------------------------------------')
                  print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
                  print('--------------------------------------------------------------------------------------------------------------------')
                  print('')
                  print('Opção inválida!')
                  print('')
                  input('Pressione Enter para sair...')

            elif (guarda_opcao_e == '2'):

               os.system('cls' if os.name == 'nt' else 'clear')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('')
               guarda_informacao_e_ip = input('Informe o ip do sistema que deseja excluir: ')

               query_busca_exclu_sis_ip = f'SELECT * FROM tb_sistemas WHERE ip_sistema = "{guarda_informacao_e_ip}"'
               cursor.execute(query_busca_exclu_sis_ip)
               query_busca_exclu_sis_ip_resultado = cursor.fetchall()
               query_busca_exclu_sis_ip_resultado_formatado = str(query_busca_exclu_sis_ip_resultado)

               os.system('cls' if os.name == 'nt' else 'clear')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('')
               print(query_busca_exclu_sis_ip_resultado_formatado) 
               print('')
               guarda_confirmacao_exclusao = input('Deseja realmente excluir esse sistema? Se sim digite "s" se deseja cancelar essa operação digite "n": ')

               if (guarda_confirmacao_exclusao == 's'):

                   os.system('cls' if os.name == 'nt' else 'clear')
                   print('--------------------------------------------------------------------------------------------------------------------')
                   print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
                   print('--------------------------------------------------------------------------------------------------------------------')
                   print('')
                   query_exclusao_confirmada = f'DELETE FROM tb_sistemas WHERE ip_sistema = "{guarda_informacao_e_ip}"'
                   cursor.execute(query_exclusao_confirmada)
                   conexao.commit()

                   #Logs
                   mensagem = f'O {usuario} excluiu o sistema: {guarda_informacao_e_ip}!'
                    
                   insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                   cursor.execute(insert_log_cadastro)
                   conexao.commit()

                   os.system('cls' if os.name == 'nt' else 'clear')
                   print('--------------------------------------------------------------------------------------------------------------------')
                   print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
                   print('--------------------------------------------------------------------------------------------------------------------')
                   print('')
                   print('A exclusão foi realizada com sucesso!')
                   print('')
                   input('Pressione Enter para sair...')
                   

               elif (guarda_confirmacao_exclusao == 'n'):
                   
                   os.system('cls' if os.name == 'nt' else 'clear')
                   print('--------------------------------------------------------------------------------------------------------------------')
                   print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
                   print('--------------------------------------------------------------------------------------------------------------------')
                   print('')
                   print('Operação cancelada!')
                   print('')
                   input('Pressione Enter para sair...')

               else:

                  os.system('cls' if os.name == 'nt' else 'clear')
                  print('--------------------------------------------------------------------------------------------------------------------')
                  print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
                  print('--------------------------------------------------------------------------------------------------------------------')
                  print('')
                  print('Opção inválida!')
                  print('')
                  input('Pressione Enter para sair...')

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('--------------------------------------- Modúlo de Exclusão de Sistemas ---------------------------------------------')
                print('--------------------------------------------------------------------------------------------------------------------')
                print('')
                print('Opção inválida!')
                print('')
                input('Pressione Enter para sair...')

# Fim do modúlo de exclusão de sistemas
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
# Início do modúlo de Cadastro de Usuário      
        elif (opcao_selecionada == '5') and (query_busca_tipo_usuario_resultado_formatado == 'Administrador'):    
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('--------------------------------------- Modúlo de Cadastro de Usuários ---------------------------------------------')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('')
            guarda_nome_cadastro = input('Insira o nome do usuário:  ')
            guarda_senha_usuario = getpass.getpass('Insira a senha do usuário:  ')
            guarda_senha_confir = getpass.getpass('Insira  a senha do usuário novamente:  ')

            if (guarda_senha_usuario == guarda_senha_confir):
               
               guarda_tipo_usuário = input('Insira o tipo do usuário: "Administrador" ou "Usuário"')

               query_insert_usuario = f'INSERT INTO tb_usuarios (nome_usuario, senha_usuario, tipo_usuario) VALUES ("{guarda_nome_cadastro}", "{guarda_senha_usuario}", "{guarda_tipo_usuário}")'
               cursor.execute(query_insert_usuario)
               conexao.commit()

               #Logs
               mensagem = f'O {usuario} cadastrou um novo usuário com o seguinte nome: {guarda_nome_cadastro}!'
                    
               insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
               cursor.execute(insert_log_cadastro)
               conexao.commit()

               os.system('cls' if os.name == 'nt' else 'clear')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('--------------------------------------- Modúlo de Cadastro de Usuários ---------------------------------------------')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('')
               print(f'Usuário {guarda_nome_cadastro} foi cadastrado com sucesso!')
               print('')
               input('Pressione Enter para sair...')

            else:
               os.system('cls' if os.name == 'nt' else 'clear')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('--------------------------------------- Modúlo de Cadastro de Usuários ---------------------------------------------')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('')
               print('A senhas não coincidem iguais!')
               print('')
               input('Pressione Enter para sair...')
# Fim Modúlo de Cadastro Usuário
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Início do Modúlo de Exclusão de Usuário
        elif (opcao_selecionada == '6') and (query_busca_tipo_usuario_resultado_formatado == 'Administrador'):
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('--------------------------------------- Modúlo de Exclusão de Usuários ---------------------------------------------')
            print('--------------------------------------------------------------------------------------------------------------------')
            print('')
            guarda_nome_usuario_exclu = input('Insira o nome do usuário que deseja excluir: ')

            query_busca_usuario_exclu = f'SELECT * FROM tb_usuarios WHERE nome_usuario = "{guarda_nome_usuario_exclu}"'
            cursor.execute(query_busca_usuario_exclu)
            query_busca_usuario_exclu_resultado = cursor.fetchall()
            query_busca_usuario_exclu_resultado_formatado = str(query_busca_usuario_exclu_resultado)

            query_valida_usuario = f'SELECT nome_usuario FROM tb_usuarios WHERE nome_usuario = "{guarda_nome_usuario_exclu}"'
            cursor.execute(query_valida_usuario)
            query_valida_usuario_resultado = cursor.fetchall()
            query_valida_usuario_resultado_formatado = str(query_valida_usuario_resultado)[3:-4]

            if (query_valida_usuario_resultado_formatado == guarda_nome_usuario_exclu):

               os.system('cls' if os.name == 'nt' else 'clear')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('--------------------------------------- Modúlo de Exclusão de Usuários ---------------------------------------------')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('')
               print(query_busca_usuario_exclu_resultado_formatado)
               print('')
               confirmacao_exclusao_usuario = input('Tem certeza que deseja excluir este usuário? Digite "s" para sim e "n" para não.')

               if (confirmacao_exclusao_usuario == "s"):
                  
                  query_delete_usuario = f'DELETE FROM tb_usuarios WHERE nome_usuario = "{guarda_nome_usuario_exclu}"'
                  cursor.execute(query_delete_usuario)
                  conexao.commit()

                  #Logs
                  mensagem = f'O {usuario} excluiu o seguinte usuário: {guarda_nome_usuario_exclu}!'
                    
                  insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
                  cursor.execute(insert_log_cadastro)
                  conexao.commit()

                  os.system('cls' if os.name == 'nt' else 'clear')
                  print('--------------------------------------------------------------------------------------------------------------------')
                  print('--------------------------------------- Modúlo de Exclusão de Usuários ---------------------------------------------')
                  print('--------------------------------------------------------------------------------------------------------------------')
                  print('')
                  print(f'O usuário {guarda_nome_usuario_exclu} foi excluído com sucesso!')
                  print('')
                  input('Pressione Enter para sair...')

               elif (confirmacao_exclusao_usuario == "n"):
                  
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print('--------------------------------------------------------------------------------------------------------------------')
                  print('--------------------------------------- Modúlo de Exclusão de Usuários ---------------------------------------------')
                  print('--------------------------------------------------------------------------------------------------------------------')
                  print('')
                  print('Operação cancelada')
                  print('')
                  input('Pressione Enter para sair...')
                  
               else:
                  
                  os.system('cls' if os.name == 'nt' else 'clear')
                  print('--------------------------------------------------------------------------------------------------------------------')
                  print('--------------------------------------- Modúlo de Exclusão de Usuários ---------------------------------------------')
                  print('--------------------------------------------------------------------------------------------------------------------')
                  print('')
                  print('Opção Inválida')
                  print('')
                  input('Pressione Enter para sair...')

            else:
               os.system('cls' if os.name == 'nt' else 'clear')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('--------------------------------------- Modúlo de Exclusão de Usuários ---------------------------------------------')
               print('--------------------------------------------------------------------------------------------------------------------')
               print('')
               print('Usuário não encontrado!')
               print('')
               input('Pressione Enter para sair...')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         #Menu principal - Caso não tenha escolhido nenhuma das opções
        elif (opcao_selecionada == '7') and (query_busca_tipo_usuario_resultado_formatado == 'Administrador'):

         query_consulta_sistemas = f'SELECT * FROM tb_sistemas'
         cursor.execute(query_consulta_sistemas)
         query_consulta_sistemas_resultado = cursor.fetchall()

         #Logs
         mensagem = f'O {usuario} verificou a informação de todos os sistemas!'
                    
         insert_log_cadastro = f'INSERT INTO tb_logs (descricao_log) VALUES ("{mensagem}")'
         cursor.execute(insert_log_cadastro)
         conexao.commit()

         os.system('cls' if os.name == 'nt' else 'clear')
         print('--------------------------------------------------------------------------------------------------------------------')
         print('-------------------------------------- Modúlo de Verificação de Sistemas -------------------------------------------')
         print('--------------------------------------------------------------------------------------------------------------------')
         print('')
         for row in query_consulta_sistemas_resultado: 
            print(row) 
         print('')
         input('Pressione Enter para sair...')

         

        else:
            print('Opção inválida!')

    else:
        print('Senha incorreta!')
    
else:
    print('Usuário incorreto!')


cursor.close()
conexao.close()