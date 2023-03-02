"""
User:
1- Academic Year 
2- Grades of Subjects
3- term
4- Credits
5- Points
"""

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
         
    # second Term Grades
    # elif    term == "second" or "second term" or '2':
    #         Mathematics_II                  =  float(input("Enter Your Grade in Mathematics II: "))
    #         Physics_I                       =  float(input("Enter Your Grade in Physics I: "))
    #         Programming_Fundamentals        =  float(input("Enter Your Grade in Programming Fundamentals : "))
    #         Digital_Circuits                =  float(input("Enter Your Grade in Digital Circuits: "))
    #         Social_Context_of_Computing     =  float(input("Enter Your Grade in Social_Context_of_Computing: "))
    #         Organizational_Behavior         =  float(input("Enter Your Grade in Organizational_Behavior: "))
    #         English_Language_II             =  float(input("Enter Your Grade in English Language II: "))
    #         Interpersonal_Communication     =  float(input("Enter Your Grade in Interpersonal Communication: "))
    #         Islamic_Culture                 =  float(input("Enter Your Grade in Islamic Culture : ")) 
            
# 
# # Second Level Category
# elif Academic_Year == "second level" or '2':
#         # first Term Grades
#         if term == "first" or "first term" or '1':
#             Mathematics_I            =  float(input("Enter Your Grade in Mathematics I: "))
#             Physics_II               =  float(input("Enter Your Grade in Physics II: "))
#             IT_Fundamentals          =  float(input("Enter Your Grade in IT Fundamentals: "))
#             Electronics              =  float(input("Enter Your Grade in Electronics: "))
#             History_of_Computing     =  float(input("Enter Your Grade in History of Computing: "))
#             Computer_Law             =  float(input("Enter Your Grade in Computer Law: "))
#             English_Language_I       =  float(input("Enter Your Grade in English Language I: "))

#         # second Term Grades
#         elif term == "second" or "second term" or '2':
#             Mathematics_II                  =  float(input("Enter Your Grade in Mathematics II: "))
#             Physics_I                       =  float(input("Enter Your Grade in Physics I: "))
#             Programming_Fundamentals        =  float(input("Enter Your Grade in Programming Fundamentals : "))
#             Digital_Circuits                =  float(input("Enter Your Grade in Digital Circuits: "))
#             Social_Context_of_Computing     =  float(input("Enter Your Grade in Social_Context_of_Computing: "))
#             Organizational_Behavior         =  float(input("Enter Your Grade in Organizational_Behavior: "))
#             English_Language_II             =  float(input("Enter Your Grade in English Language II: "))
#             Interpersonal_Communication     =  float(input("Enter Your Grade in Interpersonal Communication: "))
#             Islamic_Culture                 =  float(input("Enter Your Grade in Islamic Culture : ")) 

# # Third Level Category
# elif Academic_Year == "third level" or '3':
#         # first Term Grades
#         if term == "first" or "first term" or '1':
            
#             Mathematics_I            =  float(input("Enter Your Grade in Mathematics I: "))
#             Physics_II               =  float(input("Enter Your Grade in Physics II: "))
#             IT_Fundamentals          =  float(input("Enter Your Grade in IT Fundamentals: "))
#             Electronics              =  float(input("Enter Your Grade in Electronics: "))
#             History_of_Computing     =  float(input("Enter Your Grade in History of Computing: "))
#             Computer_Law             =  float(input("Enter Your Grade in Computer Law: "))
#             English_Language_I       =  float(input("Enter Your Grade in English Language I: "))
#         # second Term Grades
#         elif term == "second" or "second term" or '2':
#             Mathematics_II                  =  float(input("Enter Your Grade in Mathematics II: "))
#             Physics_I                       =  float(input("Enter Your Grade in Physics I: "))
#             Programming_Fundamentals        =  float(input("Enter Your Grade in Programming Fundamentals : "))
#             Digital_Circuits                =  float(input("Enter Your Grade in Digital Circuits: "))
#             Social_Context_of_Computing     =  float(input("Enter Your Grade in Social_Context_of_Computing: "))
#             Organizational_Behavior         =  float(input("Enter Your Grade in Organizational_Behavior: "))
#             English_Language_II             =  float(input("Enter Your Grade in English Language II: "))
#             Interpersonal_Communication     =  float(input("Enter Your Grade in Interpersonal Communication: "))
#             Islamic_Culture                 =  float(input("Enter Your Grade in Islamic Culture : ")) 

# # Fourth Level Category
# elif Academic_Year == "fourth level" or '4':
#         # first Term Grades
#         if term == "first" or "first term" or '1':
#             Mathematics_I            =  float(input("Enter Your Grade in Mathematics I: "))
#             Physics_II               =  float(input("Enter Your Grade in Physics II: "))
#             IT_Fundamentals          =  float(input("Enter Your Grade in IT Fundamentals: "))
#             Electronics              =  float(input("Enter Your Grade in Electronics: "))
#             History_of_Computing     =  float(input("Enter Your Grade in History of Computing: "))
#             Computer_Law             =  float(input("Enter Your Grade in Computer Law: "))
#             English_Language_I       =  float(input("Enter Your Grade in English Language I: "))

#         # second Term Grades
#         elif term == "second" or "second term" or '2':
#             Mathematics_II                  =  float(input("Enter Your Grade in Mathematics II: "))
#             Physics_I                       =  float(input("Enter Your Grade in Physics I: "))
#             Programming_Fundamentals        =  float(input("Enter Your Grade in Programming Fundamentals : "))
#             Digital_Circuits                =  float(input("Enter Your Grade in Digital Circuits: "))
#             Social_Context_of_Computing     =  float(input("Enter Your Grade in Social_Context_of_Computing: "))
#             Organizational_Behavior         =  float(input("Enter Your Grade in Organizational_Behavior: "))
#             English_Language_II             =  float(input("Enter Your Grade in English Language II: "))
#             Interpersonal_Communication     =  float(input("Enter Your Grade in Interpersonal Communication: "))
#             Islamic_Culture                 =  float(input("Enter Your Grade in Islamic Culture : ")) 



# First_LVL_First_Term = [Mathematics_I,Physics_II,IT_Fundamentals,English_Language_I,Electronics,Computer_Law,History_of_Computing]
# def calc(*First_LVL_First_Term):
#  pass
    point = 0
    rating = None

def get_points(grade):
    if grade < 50 :
        point == 0
        rating == 'F'

    elif grade >=50 and grade <60:
        point == 1.7
        rating == 'D'

    elif grade >=60 and grade <65:
        point = 2
        rating == 'D+'    

    elif grade >=65 and grade <70:
        point = 2.4
        rating == 'C'    

    elif grade >=70 and grade <75:
        point = 2.7
        rating == 'C+'

    elif grade >=75 and grade <80:
        point = 3
        rating == 'B'   

    elif grade >=80 and grade <85:
        point = 3.3
        rating == 'B+'   

    elif grade >=85 and grade <90 :
        point = 3.7
        rating == 'A'   
        
    elif grade >=85 and grade <90 :
        point = 4
        rating == 'A+' 
    else:
        point = 0
        rating == 'F'   
          
    return point , rating    