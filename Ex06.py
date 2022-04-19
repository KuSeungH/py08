# ex06.py
# phoBook 관리 프로그램 만들기

# 1) 어떤 형식의 데이터를 다루는가 -> class phoneBook

# 2) 어떤 기능을 포함하는가 -> 목록, 검색, 정렬, 추가, 수정, 삭제

# 3) 그외 작성할때 규칙이 있는가
# - 사용자의 입력과 화면에 대한 출력은 ex06.py 에서만 처리하고
#   다른 모듈파일에서는 별도의 입출력을 처리하지 않는다


from tkinter.font import names
from phonebook import phonebook     # 전화번호부 자료형
from function import *              # function 모듈 내부 모든 요소를 가져온다

# phoneBookList = []

# 테스트용 더미데이터 주가하기
# phoneBookList.append(phonebook('이지은', '01012341234'))
# phoneBookList.append(phonebook('홍진호', '010-2222-2222'))
# phoneBookList.append(phonebook('나단비', '010-3456-3456'))
# phoneBookList.append(phonebook('주호민', '010-5555-5555'))

phoneBookList = load()

# 정렬 상태를 기억할 변수
sortValue = 0

while True:
    print('1. 목록')
    print('2. 검색')
    print('3. 정렬')
    print('4. 추가')
    print('5. 수정')
    print('6. 삭제')
    print('0. 종료')
    menu = input('메뉴입력 >>> ')
    
    if menu == '1':     # 목록
        showList(phoneBookList)
        
    elif menu == '2':   # 검색
       search = input('검색어 입력 : ')     # 검색어를 입력
       searchList = getSearchList(search, phoneBookList)      # 검색어 포함한 결과만 가져와서
       showList(searchList) # 아까 만든 함수에 전달하면 출력됨
       
    elif menu == '3':   # 이름으로 정렬
      #  phoneBookList.sort() # 정렬 기준이 모호하여 실행되지 않는다
       # phoneBookList = sorted(phoneBookList, key=lambda pd: pd.name)
       
        phoneBookList.sort(key= lambda pd: pd.name, reverse= sortValue == 1)
        # phoneBookList를 정렬하는데, 정렬 기준은 각 요소를 pd라고 할때
        # pd의 name속성을 기준으로 정력한다
       
        sortValue = sortValue != 1 and 1 or -1
        # sortValue값이 1이 아니면 1을 대입, 1이면 -1을 대입
       # 초기상태는 0이르모 1을 대입하게 된다
       # 이후에는 정렬을 수행할때마다 1과 -1이 번갈아가면서 대입된다
       # 위엑서 정렬할때 sortValue 값이 1이면 거꾸로 정렬한다
       
        showList(phoneBookList)
        # 정렬응 수행하면 자동으로 목록을 출력한다
       
    elif menu == '4':   
        name = input('이름 입력 : ')
        pnum = input('전화번호 입력 : ')
        row = insert(name, pnum, phoneBookList)
        
    elif menu == '5':   # 수정
       # 원하는 요소를 하나를 가져오는 함수
       search = input('수정할 데이터 이름을 입력 :')
       pd = getPhoneBook(search, phoneBookList)
       
        # 객체를 찾았다면, 수정할 데이터를 입력받기
       if pd != None:
        name = input('변경할 이름 :')
        number = input('변경할 전화번호 : ')
        newpd = phonebook(name, number)
      
            # 리스트에서 원하는 요소의 값을 변경하기
        idx = phoneBookList.index(pd)    # 위치를 찾아서
        phoneBookList[idx] = newpd       # 그 위치에 새로운 객체 넣기
      
       else:
            print('검색어와 일치하는 결과를 찾을 수 없습니다')
       
    elif menu == '6':   #  삭제
        # 원하는 요소 하나를 가져오는 함수
        search = input('삭제할 데이터의 이름을 입력 : ')
        pd = getPhoneBook(search, phoneBookList)
        
        # 해당 요소를 리스트에서 제거
        if pd != None:
            phoneBookList.remove(pd)
            print('{} : 삭제되었습니다'.format(search))
        else:
            print('메뉴를 확인하고 다시 입력해주세요')
       
    elif menu == '0':
        save(phoneBookList)     # 종료하기 전 저장하기  
        print('프로그램을 종료합니다')
        break
    
    else:               
        print('메뉴를 확인하고 다시 입력해주세요')
    
    print('\n')
        