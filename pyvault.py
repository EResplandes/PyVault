import mysql.connector

# Conexão com o Banco de Dados
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'db_password',
)

cursor = conexao.cursor()

# Cabeçalho do Sistema
print('--------------------------------------------------------------------------------')
print('-------------------- Sistema de Controle de Senhas - GRAFEx --------------------')
print('--------------------------------------------------------------------------------')
print('--------------------- Seja Bem Vindo - Tela de Autenticação---------------------')
print('--------------------------------------------------------------------------------')

#Solicitando Usuário 
usuario = input('Digite seu usuario: ')

#Buscando Usuário no Banco
autenticacao_usuario = f'SELECT nome_usuario FROM tb_usuarios WHERE nome_usuario =  "{usuario}"'
cursor.execute(autenticacao_usuario)
autenticacao_resultado_user = cursor.fetchall()
user_formatado = str(autenticacao_resultado_user)[3:-4]

#Valdiade usuário e senha
if usuario == user_formatado:
    senha_usuario = input('Digite sua senha: ')
    autenticacao_senha = f'SELECT senha_usuario FROM tb_usuarios WHERE senha_usuario =  "{senha_usuario}"'
    cursor.execute(autenticacao_senha)
    autenticacao_resultado_senha = cursor.fetchall()
    senha_formatada = str(autenticacao_resultado_senha)[4:-4]

    if senha_usuario == senha_formatada:
        print('--------------------------------------------------------------------------------')
        print(f'Seja Bem-vindo, {usuario}!')
        print('--------------------------------------------------------------------------------')
       

        print('Menu Principal')
        print('1 - Cadastrar novo sistema')
        print('2 - Verificar informações de sistema')
        print('3 - Atualizar senha de sistema')
        opcao_selecionada = input('Selecione umas das opções:')

        if (opcao_selecionada == '1'):

            #Formúlario
            nome_sistema = input('Digite o nome do sistema: ')
            ip_sistema = input('Digite o ip do sistema: ')
            usuario_sistema = input('Digite o nome do usuario: ')
            senha_sistema = input('Digite a senha do sistema: ')

            #Executando o cadastro do sistema
            cadastra_sistema = f'CALL sp_insert_sistema ("{nome_sistema}", "{ip_sistema}", "{usuario_sistema}" , "{senha_sistema}")'
            cursor.execute(cadastra_sistema) 
            conexao.commit()

            #Verificando se o cadastro foi realizado com sucesso
            valida_cadastro_sistema = f'SELECT ip_sistema FROM tb_sistema WHERE ip_sistema = {ip_sistema}'
            formatando_ip = str(ip_sistema)[3:-4]

            if valida_cadastro_sistema == ip_sistema:
                    print('Sistema cadastrado com sucesso!')
            else:
                    print('Erro no cadastro, tente novamente!')


        elif (opcao_selecionada == '2'):
            print('Verificar')
        else:
            print('Atualizar')

    else:
        print('Senha incorreta!')
    
else:
    print('Usuário incorreto!')


cursor.close()
conexao.close()