print("Academic Year Such as first Level , Second Level or 1 , 2 ")
Academic_Year = str(input("Enter Your Academic Year: ").strip().upper())

print("Term Such as first term , second term or 1 , 2 ")
term = str(input("Enter The Term: ").strip().lower())


# First Level Category
if Academic_Year == "first level" or '1' or 'first':

    # First Term Grades
    if  term == "first" or "first term" or '1':
        Mathematics_I            =  float(input("Enter Your Grade in Mathematics I: "))
        Physics_II               =  float(input("Enter Your Grade in Physics II: "))
        IT_Fundamentals          =  float(input("Enter Your Grade in IT Fundamentals: "))
        Electronics              =  float(input("Enter Your Grade in Electronics: "))
        History_of_Computing     =  float(input("Enter Your Grade in History of Computing: "))
        Computer_Law             =  float(input("Enter Your Grade in Computer Law: "))
        English_Language_I       =  float(input("Enter Your Grade in English Language I: "))




point = 0
rating = 0

def get_points(grade):
    if grade < 50 :
        point = 0
        rating = 'F'

    elif grade >=50 and grade <60:
        point = 1.7
        rating = 'D'

    elif grade >=60 and grade <65:
        point = 2
        rating = 'D+'    

    elif grade >=65 and grade <70:
        point = 2.4
        rating = 'C'    

    elif grade >=70 and grade <75:
        point = 2.7
        rating = 'C+'

    elif grade >=75 and grade <80:
        point = 3
        rating = 'B'   

    elif grade >=80 and grade <85:
        point = 3.3
        rating = 'B+'   

    elif grade >=85 and grade <90 :
        point = 3.7
        rating = 'A'   
        
    elif grade >=95 and  grade <=100   :
        point = 4
        rating = 'A+' 

    else:
        point = 0
        rating = 'F'   
          
    return (f"{float(point)} Points => {rating} ")  
print("*"*60)
print("Mathematics I:       ",get_points(Mathematics_I))
print("Physics II:          ",get_points(Physics_II))
print("IT Fundamentals:     ",get_points(IT_Fundamentals))
print("Electronics:         ",get_points(Electronics))
print("Computer Law:        ",get_points(Computer_Law))
print("History of Computing:",get_points(History_of_Computing))
print("English Language I:  ",get_points(English_Language_I))

def calc_gpa(*subject):
    total_points = 0        

    total_points  = get_points(subject)
    total_points += get_points(subject)
    total_points += get_points(subject)
    total_points += get_points(subject)
    total_points += get_points(subject)
    total_points += get_points(subject)
    total_points += get_points(subject)
    
    gpa = total_points / (3*6)
    print(f"GPA: {gpa}") 

calc_gpa(Mathematics_I,Physics_II,IT_Fundamentals,Electronics,History_of_Computing,Computer_Law,English_Language_I)