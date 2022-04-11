# ex01.py
# 파이썬 모듈
'''
    파이썬의 소스코그 하나는 각각 모듈로 취급된다
    파이썬 소스는 함수나 클래스만 정의하고
    다른 파일에서 모듈을 불러와서 (import) 실행할 수고 있다
    
    이때, 모듈이 직접 실행되는 내용을 분라할 수도 있다
'''

# 원의 넓이를 구하는 함수
def circleArea(radius):
    return radius * radius * 3.14

def circleRound(radius):
    return radius * 2 * 3.14

if __name__ == '_main_':        # 직접 실행되었을 때만 아래 코드를 실행
                                # 모듈형태로 다른 코드에서 참조할 때는 실행되지 않음
    radius = float(input('원의 반지름 입렵 : '))
    area = circleArea(radius)
    round = circleRound(radius)

    text = '반지름이 {}cm 인 원의 넓이는 {}cm² 이고, 둘레는 {:.2f}cm입니다'
    print(text.format(radius, area, round))
