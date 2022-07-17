#list
print("=리스트 기본 ====================================================")

tList = [1,2,"python"] #tList = [] #tList = list()
print(tList[0], tList[1], tList[2])
print(tList[-1], tList[-2])

ttList = tList[1:3]
print(tList[1:3])
print(tList)
print(ttList)

print(tList*2) #tlist가 2개
print(tList+[3,4,5]) #기존값에 새로운 값 집어넣기
print(len(tList)) #원래 값의 갯수

print(2 in tList)

print("====삭제===================================================================")
del(tList[0]) #0번째 자리 삭제
print(tList)
#리스트는 변경이 가능한 자료형 

print("===수정======================================================================")
tList[0] = "일"
print(tList)

bList = ['apple', 'banana', 10, 20]
bList[2] = bList[2] + 90 #2번째가 100으로 바뀜 (10+90)
print(bList)

print("")



print("============= 리스트 수정방법(슬라이스 사용) =============")
# 값만 사라지고 배열은 사라지지 않는다.
cList = [1, 12, 123, 1234]
cList[0:2] = [10, 20]  #10 20, 123,1234
print(cList)

cList[0:2] = [10]
print(cList)

cList[1:2] = [20]
print(cList)

cList[2:3] = [30]
print(cList)

print("")
print("========== dList ==========")
dList = [1, 12, 123, 1234]
print(dList)
dList[1:2] = [] #2번째 비우기
print(dList)

dList[0:] = []                             # 전체 비우기
print(dList)

print("")
print("============= 리스트 값 추가(슬라이스 사용) =============")
print("========== eList ==========")
eList = [1, 12, 123, 1234]

#eList[1:2] = "a"                           # 수정
eList[1:1] = "a"                            # 추가    [1:1] 처럼 같은 숫자이면 배열에 값이 추가된다.
print(eList)

eList[5:] = [12345]                         #[입력숫자:] 만약에 입력한 숫자가 배열의 len 이상이면 추가된다.
print(eList)

eList[:0] = [12, -1, 0]                     #[:0] 배열 앞에 값을 추가
print(eList)

print("=================== 리스트의 메소드 ===================")
print("============ a ============")
a = [1, 12, 123, "hello", 3.14, 1000]
print(a)

#배열 뒤 값 추가
a.append(5)
print(a)

#배열 원하는 위치에 값 추가
a.insert(3, 1000) #3번째 자리 1000 추가 
print(a)

