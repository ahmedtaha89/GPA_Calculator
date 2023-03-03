First_Term = ["first","first term",'1']
Second_Term = ["second","second term" , '2']



point = 0 
def get_points(grade):
    if grade < 50 :
        point = 0
    elif grade >=50 and grade <60:
        point = 1.7
    elif grade >=60 and grade <65:
        point = 2
    elif grade >=65 and grade <70:
        point = 2.4
    elif grade >=70 and grade <75:
        point = 2.7
    elif grade >=75 and grade <80:
        point = 3
    elif grade >=80 and grade <85:
        point = 3.3
    elif grade >=85 and grade <90 :
        point = 3.7
    elif grade >=95 and  grade <=100   :
        point = 4
    else:
        point = 0

    return point

######

def calc_gpa(s1,s2,s3,s4,s5,s6,s7):
    total_points = 0        
    total_points  = get_points(s1)*3
    total_points += get_points(s2)*3
    total_points += get_points(s3)*3
    total_points += get_points(s4)*3
    total_points += get_points(s5)*2
    total_points += get_points(s6)*2
    total_points += get_points(s7)*2
    GPA = total_points/18
    print(f"Your GPA: {GPA:.2f}")

print("\n")
print("Academic Year Such as first Level , Second Level or 1 , 2 ")
Academic_Year = str(input("Enter Your Academic Year: ").strip().upper())

 



# First Level Category
if Academic_Year == "first level"  or Academic_Year == '1' or Academic_Year == 'first':
    print("Term Such as first term , second term or 1 , 2")
    term = str(input("Enter The Term: ").strip().lower())

    # First Term Grades
    if  term in First_Term:
        Mathematics_I            =  float(input("Enter Your Grade in Mathematics I: "))
        Physics_II               =  float(input("Enter Your Grade in Physics II: "))
        IT_Fundamentals          =  float(input("Enter Your Grade in IT Fundamentals: "))
        Electronics              =  float(input("Enter Your Grade in Electronics: "))
        History_of_Computing     =  float(input("Enter Your Grade in History of Computing: "))
        Computer_Law             =  float(input("Enter Your Grade in Computer Law: "))
        English_Language_I       =  float(input("Enter Your Grade in English Language I: "))

        print("*"*60)
        print("Mathematics I:       ",get_points(Mathematics_I))
        print("Physics II:          ",get_points(Physics_II))
        print("IT Fundamentals:     ",get_points(IT_Fundamentals)  )
        print("Electronics:         ",get_points(Electronics) )
        print("Computer Law:        ",get_points(Computer_Law) )
        print("History of Computing:",get_points(History_of_Computing) )
        print("English Language I:  ",get_points(English_Language_I))
        print("*"*60)
        calc_gpa(Mathematics_I,Physics_II,IT_Fundamentals,Electronics,Computer_Law,History_of_Computing,English_Language_I)

     # second Term Grades
    elif   term in Second_Term:
            Mathematics_II                  =  float(input("Enter Your Grade in Mathematics II: "))
            Physics_I                       =  float(input("Enter Your Grade in Physics I: "))
            Programming_Fundamentals        =  float(input("Enter Your Grade in Programming Fundamentals : "))
            Digital_Circuits                =  float(input("Enter Your Grade in Digital Circuits: "))
            Social_Context_of_Computing     =  float(input("Enter Your Grade in Social_Context_of_Computing: "))
            Organizational_Behavior         =  float(input("Enter Your Grade in Organizational_Behavior: "))
            English_Language_II             =  float(input("Enter Your Grade in English Language II: "))
            Interpersonal_Communication     =  float(input("Enter Your Grade in Interpersonal Communication: "))
            Islamic_Culture                 =  float(input("Enter Your Grade in Islamic Culture : ")) 

            print("*"*60)
            print("Mathematics I:       ",get_points(Mathematics_II))
            print("Physics II:          ",get_points(Physics_I))
            print("IT Fundamentals:     ",get_points(Programming_Fundamentals)  )
            print("Electronics:         ",get_points(Digital_Circuits) )
            print("Computer Law:        ",get_points(Social_Context_of_Computing) )
            print("History of Computing:",get_points(Organizational_Behavior) )
            print("English Language I:  ",get_points(English_Language_II))
            print("*"*60)
            calc_gpa(Mathematics_II,Physics_I,Programming_Fundamentals,Digital_Circuits,Social_Context_of_Computing,Organizational_Behavior,English_Language_II)

    else:
        print("Please Enter term such as 'first , second' OR  '1 , 2' ")        
else:
    print("Please Enter Correct Academic Year")

