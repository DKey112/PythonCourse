'''
Создайте класс Validator который позволяет проводить проверку данных пользователя при регистрации передаваемых 
в виде кортежа (login, password, email)
В данном классе реализовать метод validate(user_data), который позволяет проверить передаваемый кортеж по правилам:
login — не менее 6 символов
password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)
email — присутствует символ @, оканчивается . и 2 символами (.by)
Валидация каждого элемента в кортеже производится отдельным методом для каждого элемента (validate_email, validate_login, validate_password) 
в которых в случае непрохождения валидации вызывается ошибка (InvalidPassword, InvalidLogin, InvalidEmail), 
при соответствии — возвращается значение True. В методе validate необходимо предусмотреть обработку этих ошибок и в случае их наличия 
— вызвать ошибку ValidationError.
Ошибки создать самостоятельно
например
validator = Validator()
validator.validate(user_login, Some!Password, mail@mail.com)
# True
validator.validate(user, Some!Password, mail@mail.com)
#  ValidationError
'''
import string
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
        if len(self.login) > 6:
            return True
        else:
            raise InputLoginError

    def validate_password(self)-> bool:
        if len(self.password) < 8:
            raise InputPasswordError
        for i in self.password:
            if i in string.punctuation and i.upper() or i.lower() and i.lower():
                ...
            else:
                raise InputPasswordError
        return True


    def validate_mail(self)-> bool:
        try:
            if "@" in self.mail and self.mail.endswith(".by"):
                return True
        except:
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

    

user_data = Validator("Sasha123", "sashaShauro#", "sobaka@mail.by")
# user_data.validate_login()
# user_data.validate_mail()
# user_data.validate_password()
user_data.valid()




