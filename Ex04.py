#ex04.py

from urllib.request import url2pathname
from Ex03 import Unit       # 잘 만들어진 클래스를 가져오면

u1 = Unit('Guardian', 150, 20, 2, 8, 1.2, 1.5)  # 손쉽게 객체를 생성할수 있고
u2 = Unit('Goliath', 125, 20, 1, 8, 1.4, 1.5)   # 객체마다 다른 값을 지정할 수 있고

while True:
    
    u1.attackUnit(u2)       # 각 객체는 동일한 구조의 함수를 호출할 수 있고
    if u2.hp < 0:
        print('{} 파괴됨'.format(u2.name))
        break
    u2.attackUnit(u1)       # 같은 함수를 호출해도 서로 다른 작종이 일어날 수 있다
    if u1.hp < 0:
       print('{} 파괴됨'.format(u1.name))
       break 
    
print(u1)
print(u2)

# 만약 위 코드를 클래스와 import 없이 구성한다면
# 코드가 더 복잡해지면서 만들기도 읽기도 어려울 것이다