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

    
        print('Menu Principal')
        print('1) Cadastrar novo sistema')
        print('2) Verificar informações de sistema')
        print('3) Atualizar informação de sistema')   
        print('4) Exclusão de sistema')
        print('5) Cadastro de Usuário')
        print('6) Exclusão de Usuário')
        opcao_selecionada = input('Selecione umas das opções:')
        

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #Modúlo de Cadastro de Sistema''
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
            print('--------------------------------------------------------------------------------------------------------------------')
            print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
            print('--------------------------------------------------------------------------------------------------------------------')

            print('1) Buscar pelo nome:  ')
            print('2) Buscar pelo Ip: ')
            guarda_opcao_a = input('Selecione o parametrô de busca:')

            if (guarda_opcao_a == '1'):
                 os.system('cls' if os.name == 'nt' else 'clear')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 pede_nome = input('Insira o nome do sistema que deseja atualizar a informação: ')
                 qyery_busca_sistema_nome = f'SELECT nome_sistema FROM tb_sistemas WHERE nome_sistema LIKE "%{pede_nome}%"'
                 cursor.execute(qyery_busca_sistema_nome)
                 qyery_busca_sistema_nome_resultado = cursor.fetchall()
                 qyery_busca_sistema_nome_resultado_formatado = str(qyery_busca_sistema_nome_resultado)[3:-4]

                 os.system('cls' if os.name == 'nt' else 'clear')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                 print('--------------------------------------------------------------------------------------------------------------------')

                 print('1) Atualizar nome do sistema: ')
                 print('2) Atualizar ip do sistema: ')
                 print('3) Atualizar usuário do sistema: ')
                 print('4) Atualizar senha do sistema: ')
                 guarda_parametro_atualizacao = input('Selecione o parametrô que deseja atualizar: ')
                
                 if (guarda_parametro_atualizacao == '1'):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    guarda_parametro_atualizacao_novo_nome = input('Informe o novo nome do sistema: ') 

                    atualiza_nome = f'UPDATE tb_sistemas SET nome_sistema = "{guarda_parametro_atualizacao_novo_nome}" WHERE  nome_sistema = "{qyery_busca_sistema_nome_resultado_formatado}"'
                    cursor.execute(atualiza_nome)
                    conexao.commit()

                    # query_confirma_atualizacao_nome = f'SELECT nome_sistema FROM tb_sistemas WHERE nome_sistema = "{guarda_parametro_atualizacao_novo_nome}"'
                    # cursor.execute(query_confirma_atualizacao_nome)
                    # query_confirma_atualizacao_nome_resultado = cursor.fetchall()
                    # query_confirma_atualizacao_nome_resultado_formatado = str(qyery_busca_sistema_nome_resultado)[3:-4]
                    
                    print('Atualização realizada com sucesso!')

                 elif (guarda_parametro_atualizacao == '2'):
                    
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    guarda_parametro_atualizacao_novo_ip = input('Informe o novo ip do sistema: ')

                    atualiza_ip = f'UPDATE tb_sistemas SET ip_sistema = "{guarda_parametro_atualizacao_novo_ip}" WHERE nome_sistema = "{qyery_busca_sistema_nome_resultado_formatado}"'
                    cursor.execute(atualiza_ip)
                    conexao.commit()

                    print('Atualização realizada com sucesso!')

                 elif (guarda_parametro_atualizacao == '3'):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    guarda_parametro_atualizacao_novo_usuario = input('Informe o novo nome do usuário sistema: ')

                    atualiza_usuario = f'UPDATE tb_sistemas SET usuario_sistema = "{guarda_parametro_atualizacao_novo_usuario}" WHERE nome_sistema = "{qyery_busca_sistema_nome_resultado_formatado}"'
                    cursor.execute(atualiza_usuario)
                    conexao.commit()

                    print('Atualização realizada com sucesso!')

                 elif (guarda_parametro_atualizacao == '4'):
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    guarda_parametro_atualizacao_nova_senha = input('Informe a nova senha sistema: ')
                    
                    atualiza_senha = f'UPDATE tb_sistemas SET senha_sistema = "{guarda_parametro_atualizacao_nova_senha}" WHERE nome_sistema = "{qyery_busca_sistema_nome_resultado_formatado}"'
                    cursor.execute(atualiza_senha)
                    conexao.commit()

                 else:
                    print('Parametrô inválido!')
                   

            elif (guarda_opcao_a == '2'):
                 os.system('cls' if os.name == 'nt' else 'clear')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 pede_ip = input('Insira o ip do sistema que deseja atualizar a informação: ')
                 qyery_busca_sistema_ip = f'SELECT ip_sistema FROM tb_sistemas WHERE ip_sistema = "{pede_ip}"'
                 cursor.execute(qyery_busca_sistema_ip)
                 qyery_busca_sistema_ip_resultado = cursor.fetchall()
                 qyery_busca_sistema_ip_resultado_formatado = str(qyery_busca_sistema_ip_resultado)[3:-4]

                 os.system('cls' if os.name == 'nt' else 'clear')
                 print('--------------------------------------------------------------------------------------------------------------------')
                 print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                 print('--------------------------------------------------------------------------------------------------------------------')

                 print('1) Atualizar nome do sistema: ')
                 print('2) Atualizar ip do sistema: ')
                 print('3) Atualizar usuário do sistema: ')
                 print('4) Atualizar senha do sistema: ')
                 guarda_parametro_atualizacao = input('Selecione o parametrô que deseja atualizar: ')
                
                 if (guarda_parametro_atualizacao == '1'):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    guarda_parametro_atualizacao_novo_nome = input('Informe o novo nome do sistema: ') 

                    atualiza_nome = f'UPDATE tb_sistemas SET nome_sistema = "{guarda_parametro_atualizacao_novo_nome}" WHERE  ip_sistema = "{qyery_busca_sistema_ip_resultado_formatado}"'
                    cursor.execute(atualiza_nome)
                    conexao.commit()

                    # query_confirma_atualizacao_nome = f'SELECT nome_sistema FROM tb_sistemas WHERE nome_sistema = "{guarda_parametro_atualizacao_novo_nome}"'
                    # cursor.execute(query_confirma_atualizacao_nome)
                    # query_confirma_atualizacao_nome_resultado = cursor.fetchall()
                    # query_confirma_atualizacao_nome_resultado_formatado = str(qyery_busca_sistema_nome_resultado)[3:-4]
                    
                    print('Atualização realizada com sucesso!')

                 elif (guarda_parametro_atualizacao == '2'):
                    
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    guarda_parametro_atualizacao_novo_ip = input('Informe o novo ip do sistema: ')

                    atualiza_ip = f'UPDATE tb_sistemas SET ip_sistema = "{guarda_parametro_atualizacao_novo_ip}" WHERE ip_sistema = "{qyery_busca_sistema_ip_resultado_formatado}"'
                    cursor.execute(atualiza_ip)
                    conexao.commit()

                    print('Atualização realizada com sucesso!')

                 elif (guarda_parametro_atualizacao == '3'):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    guarda_parametro_atualizacao_novo_usuario = input('Informe o novo nome do usuário sistema: ')

                    atualiza_usuario = f'UPDATE tb_sistemas SET usuario_sistema = "{guarda_parametro_atualizacao_novo_usuario}" WHERE ip_sistema = "{qyery_busca_sistema_ip_resultado_formatado}"'
                    cursor.execute(atualiza_usuario)
                    conexao.commit()

                    print('Atualização realizada com sucesso!')

                 elif (guarda_parametro_atualizacao == '4'):
                    print('--------------------------------------------------------------------------------------------------------------------')
                    print('------------------------------------ Modúlo de Atualização de Informações ------------------------------------------')
                    print('--------------------------------------------------------------------------------------------------------------------')
                    guarda_parametro_atualizacao_nova_senha = input('Informe a nova senha sistema: ')
                    
                    atualiza_senha = f'UPDATE tb_sistemas SET senha_sistema = "{guarda_parametro_atualizacao_nova_senha}" WHERE ip_sistema = "{qyery_busca_sistema_ip_resultado_formatado}"'
                    cursor.execute(atualiza_senha)
                    conexao.commit()

                 else:
                    print('Parametrô inválido!')
                   
            else:
                print('Parametrô inválido!')

# Fim do Modúlo de Atualização de Sistema
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Início do Modúlo de Exclusão de Sistema - Administrador
        elif (opcao_selecionada == '4'):
             #Modúlo de Exclusão de sistema
             print('sei la')
        else:
            print('Opção inválida!')

    else:
        print('Senha incorreta!')
    
else:
    print('Usuário incorreto!')


cursor.close()
conexao.close()