# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input ('[E] Entrar [S] Sair: ')
senha_digitada = input('Senha: ') 

senha_permitida = '1233456'

if (entrada == 'E' or entrada == 'e')and senha_digitada == senha_permitida
    print('Entrar')

# Avaliação de curto circuito
