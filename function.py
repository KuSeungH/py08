# function.py
# ex06.py 에서 수행할 내용을 함수로 정리한 모듈

from ast import In
from phonebook import phonebook

def insert(name, pnum, pdlist):
    pd = phonebook(name, pnum)
    pdlist.append(pd)
    
def showList(pdlist):
    for pd in pdlist:
        print(pd)
        
def getSearchList(search, pdlist):
    searchList = [] 
    for pd in pdlist:       # 전체 목록 중에서
        if search in pd.name or search in pd.number:    # 이름에 검색어가 포함하거나, 번호에 검색어가 포함되면
            searchList.append(pd)   # 검색 리스트에 추가한다
    return searchList

def getPhoneBook(search, pdlist):
    for pd in pdlist:
        if pd.name == search:   # 일치하는 요소가 있으면 
            return pd           # 해당 요소를 반환
    return None
    # 처음부터 끝까지 찾아봐도 없으면
    # 객채를 변환하지 않는다
   
# 리스트(객체)를 문자열 형태가 아닌 바이너리 형태로 저장 
# pickle : 파이썬에서 바이너리 파일 입출력을 위해 제공하는 기본 모듈
import pickle

def save(pdlist):
    # f = open('phonebook.dat', 'w')
    with open('phonebook.dat', 'wb') as f:
        pickle.dump(pdlist, f)
        

def load():
    try:    # try 내부 코드를 실행하다가
            # 에러가 발생하면 except로 넘어가다
        
        with open('phonebook.dat', 'rd') as f:
            pdlist = pickle.load(f)
            return pdlist
    
    except:
        # 프로그램을 중단하지 않고, 아래 코드를 수행한다
        return[]
    
    