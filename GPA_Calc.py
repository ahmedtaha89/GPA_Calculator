"""
User:
1- Academic Year 
2- Grades of Subjects
3- term
4- Credits
5- Points
"""

First_Term = ["first","first term",'1']
Second_Term = ["second","second term" , '2']

Academic_Year_1 = ["first level","first","1"]
Academic_Year_2 = ["second level","second","2"]
Academic_Year_3 = ["third level","third","3"]
Academic_Year_4 = ["fourth level","fourth","4"]


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


print("\n\n")
print("Academic Year Such as first Level , Second Level or 1 , 2 ")
Academic_Year = str(input("Enter Your Academic Year: ").strip().upper())

print("Term Such as first term , second term or 1 , 2")
term = str(input("Enter The Term: ").strip().lower())


# First Level Category
if Academic_Year in Academic_Year_1:

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
            print("Mathematics II:       ",get_points(Mathematics_II))
            print("Physics_I:          ",get_points(Physics_I))
            print("Programming_Fundamentals :     ",get_points(Programming_Fundamentals)  )
            print("Social_Context of Computing:        ",get_points(Social_Context_of_Computing) )
            print("Organizational Behavior:",get_points(Organizational_Behavior) )
            print("Interpersonal Communication:  ",get_points(Interpersonal_Communication))
            print("English Language II:  ",get_points(English_Language_II))
            print("Islamic Culture:  ",get_points(Islamic_Culture))
            print("*"*60)

            calc_gpa(Mathematics_II,Physics_I,Programming_Fundamentals,Social_Context_of_Computing)







    else:
        print("Please Enter term such as 'first , second' OR  '1 , 2' ")        
 
# Second Level Category
elif Academic_Year in Academic_Year_2:
        # first Term Grades
        if term in First_Term:
            Mathematics_III                     =  float(input("Enter Your Grade in Mathematics III : "))
            Discrete_Structures                 =  float(input("Enter Your Grade in Discrete Structures: "))
            Object_Oriented_Programming         =  float(input("Enter Your Grade in Object Oriented Programming: "))
            Foundations_of_Information_Systems  =  float(input("Enter Your Grade in FoundationsofInformationSystems : "))
            File_Organization                   =  float(input("Enter Your Grade in File Organization: "))
            Project_Management                  =  float(input("Enter Your Grade in Project Management: "))
            Digital_Signal_Processing           =  float(input("Enter Your Grade in Digital Signal Processing: "))

  

        # second Term Grades
        elif term in Second_Term:
            Data_Structures                  =  float(input("Enter Your Grade in Data_Structures: "))
            Databases                        =  float(input("Enter Your Grade in Databases: "))
            systems_Analysis_and_Design      =  float(input("Enter Your Grade in systems Analys is and Design : "))
            Web_Programming                  =  float(input("Enter Your Grade in Web Programming: "))
            Data_Communications              =  float(input("Enter Your Grade in Data Communications: "))
            Probability                      =  float(input("Enter Your Grade in Probability: "))
            Computers_and_Ethic              =  float(input("Enter Your Grade in Computers_and_Ethic : "))

# Third Level Category
elif Academic_Year in Academic_Year_3:
        # first Term Grades
        if term in First_Term:
            
            Mathematics_I            =  float(input("Enter Your Grade in Mathematics I: "))
            Physics_II               =  float(input("Enter Your Grade in Physics II: "))
            IT_Fundamentals          =  float(input("Enter Your Grade in IT Fundamentals: "))
            Electronics              =  float(input("Enter Your Grade in Electronics: "))
            History_of_Computing     =  float(input("Enter Your Grade in History of Computing: "))
            Computer_Law             =  float(input("Enter Your Grade in Computer Law: "))
            English_Language_I       =  float(input("Enter Your Grade in English Language I: "))
        # second Term Grades
        elif term in Second_Term:
            Mathematics_II                  =  float(input("Enter Your Grade in Mathematics II: "))
            Physics_I                       =  float(input("Enter Your Grade in Physics I: "))
            Programming_Fundamentals        =  float(input("Enter Your Grade in Programming Fundamentals : "))
            Digital_Circuits                =  float(input("Enter Your Grade in Digital Circuits: "))
            Social_Context_of_Computing     =  float(input("Enter Your Grade in Social_Context_of_Computing: "))
            Organizational_Behavior         =  float(input("Enter Your Grade in Organizational_Behavior: "))
            English_Language_II             =  float(input("Enter Your Grade in English Language II: "))
            Interpersonal_Communication     =  float(input("Enter Your Grade in Interpersonal Communication: "))
            Islamic_Culture                 =  float(input("Enter Your Grade in Islamic Culture : ")) 

# Fourth Level Category
elif Academic_Year in Academic_Year_4:
        # first Term Grades
        if term in First_Term:
            Mathematics_I            =  float(input("Enter Your Grade in Mathematics I: "))
            Physics_II               =  float(input("Enter Your Grade in Physics II: "))
            IT_Fundamentals          =  float(input("Enter Your Grade in IT Fundamentals: "))
            Electronics              =  float(input("Enter Your Grade in Electronics: "))
            History_of_Computing     =  float(input("Enter Your Grade in History of Computing: "))
            Computer_Law             =  float(input("Enter Your Grade in Computer Law: "))
            English_Language_I       =  float(input("Enter Your Grade in English Language I: "))

        # second Term Grades
        elif term in Second_Term:
            Mathematics_II                  =  float(input("Enter Your Grade in Mathematics II: "))
            Physics_I                       =  float(input("Enter Your Grade in Physics I: "))
            Programming_Fundamentals        =  float(input("Enter Your Grade in Programming Fundamentals : "))
            Digital_Circuits                =  float(input("Enter Your Grade in Digital Circuits: "))
            Social_Context_of_Computing     =  float(input("Enter Your Grade in Social_Context_of_Computing: "))
            Organizational_Behavior         =  float(input("Enter Your Grade in Organizational_Behavior: "))
            English_Language_II             =  float(input("Enter Your Grade in English Language II: "))
            Interpersonal_Communication     =  float(input("Enter Your Grade in Interpersonal Communication: "))
            Islamic_Culture                 =  float(input("Enter Your Grade in Islamic Culture : ")) 

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

print("*"*60)
print("Mathematics I:       ",get_points(Mathematics_I))
print("Physics II:          ",get_points(Physics_II))
print("IT Fundamentals:     ",get_points(IT_Fundamentals)  )
print("Electronics:         ",get_points(Electronics) )
print("Computer Law:        ",get_points(Computer_Law) )
print("History of Computing:",get_points(History_of_Computing) )
print("English Language I:  ",get_points(English_Language_I))
print("*"*60)

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


calc_gpa(Mathematics_I,Physics_II,IT_Fundamentals,Electronics,Computer_Law,History_of_Computing,English_Language_I)

