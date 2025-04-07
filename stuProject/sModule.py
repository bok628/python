
# 변수선언 & 변수 출력 순서 삽입 클래스
class Student :
    count = 1
    
    def __init__(self,name,kor,eng,math):
        self.no = Student.count  # 클래스변수
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = self.total / 3
        self.rank = 0
        Student.count += 1
        
    def __str__(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"
        
# 리스트를 생성하여 데이터 넣기
class Students :
    def __init__(self):
        self.students = []
        
    def add(self,s) :
        self.students.append(s)
    
    def __str__(self):
        for s in self.students :
            print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
        return ""    # 문자열로 리턴
            
            
         
         
         
         
          
# # 변수생성&문자 나열 클래스
# class Student :
#     count = 1 # 클래스 변수
#     def __init__(self,name,kor,eng,math) :
#         self.no = Student.count
#         self.name = name
#         self.kor = kor
#         self.eng = eng
#         self.math = math
#         self.total = kor + eng + math
#         self.avg = self.total / 3
#         self.rank = 0
#         count += 1
#     def __str__(self):
#         return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg},{self.rank}"
    

# # 리스트 생성후 데이터를 리스트에 넣기 출력클랫,
# class Students :
#     def __init__(self):
#         self.students = []
#     def add(self,s):                # s가 참조변수
#         self.students.append(s)
#     def __str__(self):
#         for s in self.students :
#             print(s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank)
                 
         
         
         
         
         
         
         
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            