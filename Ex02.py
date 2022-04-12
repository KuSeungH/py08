#ex02.py
# 다른 파이썬 모듈 불러오기 (import)

import Ex01         # 모듈을 불러오기
                    # 모듈을 불러오면 모듈 파일이 한번 실행된다
                    # 모듈을 import 했다면 하위 요소에는 .으로 접근해야 한다
# a = circleArea(5)

b = Ex01.circleArea(5)  # 모듈.함수이름
print(b)


from Ex01 import circleRound    # from 모듈 import 함수/클래스

c = circleRound(5)      # 함수이름
print(c)

from getpass import getpass

password = getpass('비밀번호 입력 :')
print('입력한 비밀번호는 {}'.format(password))

