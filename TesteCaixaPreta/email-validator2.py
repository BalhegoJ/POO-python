import re

regex = r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

def check(email):
    if re.fullmatch(regex, email):
        print('Email valido')
    else:
        print('Email invalido')

if __name__ == '__main__':
    # Testando varios endereços de email
    check('sarah.connor@futurenet.com') # Esperado: e-mail válido
    check('john.doe@workplace.org') # Esperado: e-mail válido
    check('jane.smith@personal') # Esperado: e-mail inválido
    check('no_at_symbol.com') # Esperado: e-mail inválido
    check('admin@tech-hu.io') # Esperado: e-mail válido
    check('invalid-email@123') # Esperado: e-mail inválido