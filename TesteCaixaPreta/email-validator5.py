from email_validator import validate_email, EmailNotValidError

def check(email):
    try:
        # Valida o email e obtem forma normalizada
        v = validate_email(email)
        email = v["email"]
        print('True')
    except EmailNotValidError as e:
        # Se o email não for válido, escreve na tela uma mensagem de erro
        print(str(e))

if __name__ == '__main__':
    # Testando varios endereços de email
    check('otaviolemos@gmail.com') # Esperado: e-mail válido
    check('otaviolemosgmail.com') # Esperado: e-mail inválido
    check('otaviolemossssssssssssssssssssssssssssssssssssssssssssssssssssssssss@gmail.com') # Esperado: e-mail inválido
    check('@gmail.com') # Esperado: e-mail inválido
    check('otavio lemos@gmail.com') # Esperado: e-mail inválido
    check('.otaviolemos@gmail.com') # Esperado: e-mail inválido
    check('otaviolemos.@gmail.com') # Esperado: e-mail inválido
    check('otavio..lemos@gmail.com') # Esperado: e-mail inválido
    check('otaviolemos@gmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaail.com') # Esperado: e-mail inválido
    check('otaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaviolemos@gmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaail.com') # Esperado: e-mail inválido
    check('') # Esperado: e-mail inválido
    check('otaviolemos@') # Esperado: e-mail inválido