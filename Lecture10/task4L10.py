'''
* Реализовать кодирование и декодирование ключевых слов для латинского алфавита согласно указанному соответствию (маппингу). 
Шифр (используйте данное соответствие букв при решении задания)
* A B C D E F G H I  J  K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H  I  J  K L M N Q S U V W X Z
Пример:
cipher = Cipher()
cipher.encode("Hello world")
"Btggj vjmgp"

cipher.decode("Fjedhc dn atidsn")
"Kojima is genius"
'''
class Cipher:



    def encode(self,text):
        self.text = text.upper()
        #Результат шифрования 
        res = []
        #Словари латинскуого и шифровального 
        input_dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key_dict = 'CRYPTOABDEFGHIJKLMNQSUVWXZ'

        # после проверки на нахождении в input_dict
        s = ''

        for i in range(len(self.text)):
            if self.text[i] in input_dict:
                s = input_dict
            else:
                res.append(self.text[i])

            if self.text[i] in s:
                for j in range(len(s)):
                    if 0 < j + 1 < len(s) and self.text[i] == s[j]:
                        res.append(key_dict[j + 1])
                    elif j + 1 >= len(s) and self.text[i] == s[j]:
                        res.append(key_dict[(1 - j - 1) % (len(key_dict) - 1)])
                    elif j + 1 < 0 and self.text[i] == s[j]:
                        res.append(key_dict[(j + 1) % len(key_dict)])
        print(''.join(res))


    def decode(self,text):
        self.text = text.upper()
        #Результат шифрования 
        res = []
        #Словари латинскуого и шифровального 
        input_dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key_dict = 'CRYPTOABDEFGHIJKLMNQSUVWXZ'

        # после проверки на нахождении в key_dict
        s = ''

        for i in range(len(self.text)):
            if self.text[i] in key_dict:
                s = key_dict
            else:
                res.append(self.text[i])

            if self.text[i] in s:
                for j in range(len(s)):
                    if 0 < j + 1 < len(s) and self.text[i] == s[j]:
                        res.append(input_dict[j - 1])
                    elif j + 1 >= len(s) and self.text[i] == s[j]:
                        res.append(input_dict[(1 + j + 1) % (len(input_dict) - 1)])
                    elif j + 1 < 0 and self.text[i] == s[j]:
                        res.append(input_dict[(j - 1) % len(input_dict)])
        print(''.join(res))


cipher = Cipher()
cipher.encode("Hello world")
cipher.decode('DOHHK WKNHT')




