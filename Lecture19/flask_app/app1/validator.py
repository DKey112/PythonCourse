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
            b = r'^[\w.-]+@[\w.-]+\.(\S{2}$)'
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
        return True