raw_grade = input('Enter your grade\n')
try:
    grade = float(raw_grade)
    if grade > 1.0 :
        print("wrong grade")
    elif grade >= 0.9 :
        print("A")
    elif grade >= 0.8 :
        print("B")
    elif grade >= 0.7 :
        print("C")
    elif grade >= 0.6 :
        print("D")
    elif grade < 0.6 and grade >0.0 :
        print("F")
    elif grade < 0.0 :
        print("wrong grade")
except:
    print('wrong grade')