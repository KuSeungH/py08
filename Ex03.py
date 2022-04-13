# ex03.py
# 파이썬 클래스

'''
    파이썬의 클래스는 변수, 함수, 이니셜라이저로 구성된다
    클래스 : 객채를 표현하기 위한 자료형
    - 클래스의 함수 및 이니셜라이저는 첫번째 매개변수로 반드시 self를 가져야 한다
    - self는 같은 클랙스로 작성된 여러 객체 중 객체 자신을 가리킬때 사용한다
'''



class Unit:
    name = ''
    hp = 0
    attack = 0
    deffense = 0
    attackRange = 0
    moveSpeed = 0
    attackSpeed = 0
    
    # 내가 추가한 기능 (대상을 전달받아서 대상의 체력을 감소시키는 가능)
    def attackUnit(self, target):
        target.hp -= (self.attack - target.deffense)
    
    # 객체를 출력할 때 형식을 문자열형태로 지정해주고 싶다면 정의하세요 능  
    def __str__(self):
        format = '{} : {} / {} / {}'
        return format.format(self.name, self.hp, self.attack, self.deffense)
    # 객체를 생성하면서 동시에 초기값을 지정하고 싶다면 이니셜라이저를 작성 
    def __init__(self, name, hp, attack, deffense, attackRange, moveSpeed, attackSpeed):
        self.name = name
        self.hp = hp 
        self.attack = attack
        self.deffense = deffense
        self.attackRange = attackRange
        self.moveSpeed = moveSpeed
        self.attackSpeed = attackSpeed
        print(name, '객체 생성 완료')
    # 파이썬에서는 하나의 함수에 여러 내용을 중복적용할수 없다
    # def __init__(self): # 이니셜라이저는 매개변수 형태에 따라 여러개를 작성할 수 없다
    #    pass    # 특별히 진보할  내용이 없다면 pass를 작성한다 (제어문 및 함수 적용 가능)
  
if __name__ == '__main__':      
    u1 = Unit('Marine', 40, 6, 0, 5, 2.0, 1.4)
    # u1.name ='Marine'
    # u1.hp = 40
    # u1.attack = 6
    # u1.attackRange = 5
    # u1.moveSpeed = 2.0
    # u1.attackSpeed = 1.4
    print(u1)

    u2 = Unit('Medic', 60, 0, 2, 12, 2.0, 0)
    print(u2)

    u1.attackUnit(u2)       # Marine이 Medic에게 공격한번
    print(u1, u2)