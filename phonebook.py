# phonebook.py
# 클래스를 정의하는 모듈

class phonebook:
    name = ''
    number = ''
    
    def formatNumber(self, number):
        n1 = number[:3]
        n2 = number[3:7]
        n3 = number[7:]
        number = '{}-{}-{}'.format(n1, n2, n3)
        return number
    
    def __str__(self):
        return '{} : {}'.format(self.name, self.number)
    
    def __init__(self, name, number):
        self.name = name
        if len(number) == 11:
            self.number =self.formatNumber(number)
        elif len(number) == 13:
            self.number = number
        else:
            print('전화번호의 길이가 맞지 않습니다 : {}' .format(name))
            self.number = ''