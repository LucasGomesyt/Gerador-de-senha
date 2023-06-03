import random
import string

#gerador_senha
def gerador_senha(tamanho_senha):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for item in range(tamanho_senha))
    return senha

#tamanho_senha
tamanho_senha = int(input('Digite o tamanho da senha: '))
#execução da função
senha = gerador_senha(tamanho_senha)
#resultado
print(f'senha gerada: {senha}')