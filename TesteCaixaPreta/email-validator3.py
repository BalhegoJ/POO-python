"""
Uma expressão regular (também conhecida como Python regex) é uma ferramenta poderosa
na caixa de ferramentas de qualquer programador para manipular e validar strings de um
endereço de e-mail. O módulo “re” em Python fornece suporte completo para expressões
regulares do tipo Perl.
"""

import re

#regex = r'/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/'
regex = r'\b[A-Za-z0-9._%+-]+@[A-Aza-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check(email):
    if re.fullmatch(regex, email):
        print('Email valido')
    else:
        print('Email invalido')

if __name__ == '__main__':
    # Testando varios endereços de email
    check('otaviolemos@gmail.com') # Esperado: e-mail válido
    check('otaviolemosgmail.com') # Esperado: e-mail inválido
    check('otaviolemosssssssssssssssssssssssssssssssssssssssssssssssssssssss.gmail.com') # Esperado: e-mail inválido
    check('@gmail.com') # Esperado: e-mail inválido
    check('otavio lemos@gmail.com') # Esperado: e-mail inválido
    check('.otaviolemos@gmail.com') # Esperado: e-mail inválido
    check('otaviolemos.@gmail.com') # Esperado: e-mail inválido
    check('otavio..lemos@gmail.com') # Esperado: e-mail inválido
    check('otaviolemos@gmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaail.com') # Esperado: e-mail inválido
    check('otaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaviolemos@gmaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaail.com') # Esperado: e-mail inválido
    check('') # Esperado: e-mail inválido
    check('otaviolemos@') # Esperado: e-mail inválido