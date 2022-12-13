'''
Создайте класс Validator который позволяет проводить проверку данных пользователя при
регистрации передаваемых в виде кортежа (login, password, email)
B данном классе реализовать метод validate(user_data), который позволяет проверить передаваемый кортеж по правилам:
login — от 6 до 10 символов английского алфавит и цифр 0-9 в любой последовательности
password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)
email — присутствует символ @, оканчивается . и 2 символами (.by)
Проверку на соответствие правилам выполнить регулярными выражениями. 
По результатам работы метода validate пользователь получит True если все 3 элемента прошли проверку, 
в противном случае - False
'''

import re
from typing import Any

class InputLoginError(Exception):
    pass

class InputPasswordError(Exception):
    pass

class InputMailError(Exception):
    pass

class ValidError(Exception):
    pass



class Validator:

    def __init__(self, login, password, mail):
        self.login = login
        self.password = password
        self.mail = mail
    

    def validate_login(self)-> bool:
        g = r'^(?=\d*)(?=[a-z]*)(?=[A-Z]*).{6,10}$'
        if (re.match(g, self.login)):
            return True
        else:
            raise InputLoginError

    def validate_password(self)-> bool:
        reg = r'^.*(?=.)(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).{8,}$'
        if(re.match(reg, self.password)):
            return True
        else:
            raise InputPasswordError


    def validate_mail(self)-> bool:
            b = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[by])'
            if (re.match(b, self.mail)):
                return True
            else:
                raise InputMailError
            

    def valid(self):
        try:
            self.validate_mail()
            self.validate_login()
            self.validate_password()
        except InputLoginError:
            raise ValidError
        except InputMailError:
            raise ValidError
        except InputPasswordError:
            raise ValidError

    

user_data = Validator("Ma#ha3#", "Mahsa231#", "some@mail.by")
# user_data.validate_login()
# user_data.validate_mail()
# user_data.validate_password()
user_data.valid()
