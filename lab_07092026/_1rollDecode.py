'''
Given roll number 
    205126009
    2 -> PG
        -> 1 -> UG
        -> 2 -> PG
        -> 3 -> Research MS
        -> 4 -> Research Ph.D.

    05 -> Computer Applications
        -> 01 -> Architecture                   -> 10 -> Instrumentation & Control (ICE)
        -> 02 -> Chemical Engineering           -> 11 -> Mechanical Engineering
        -> 03 -> Civil Engineering              -> 12 -> Metallurgical & Materials (MME)
        -> 05 -> Computer Applications          -> 14 -> Production Engineering
        -> 06 -> Computer Science (CSE)         -> 15 -> Management Studies
        -> 07 -> Electrical & Electronics (EEE) -> 16 -> Mathematics
        -> 08 -> Electronics & Comm. (ECE)
    
    1 -> MCA
        -> Core stream in the branch
        -> 1011 -> B.Tech Arch
        -> 2011 -> M.Tech Arch
        -> 2051 -> MCA
        -> 2151 -> MBA

    26 -> Year of admission
    
    009 -> Sequence Number  

'''
'''
PROBLEM STATEMENT: Given roll number of student decode his information 
INPUT: Roll Number (N)
OUTPUT: Output Student's Department, Admission Year, Roll Number
Read N
parts <- {1:temp[:1],2:temp[1:3],3:temp[3:4],4:temp[4:6],5:temp[6:9]}
part1 <- {<code>: <UG/PG/PH.d.>}
part2 <- {<code>: <Department>}
part4 <- "20" + parts[4]
Write parts[part1[<code>]], parts[part2[<code>]], part4, parts[5]
'''

valid:bool = False 
while not valid:
    temp:str = input("Enter a nine digit roll number: ")
    if temp.isnumeric() and len(temp) == 9:
        valid = True
    else:
        print("Enter a valid roll number")

# print(temp)
parts = {1:temp[:1],2:temp[1:3],3:temp[3:4],4:temp[4:6],5:temp[6:9]}

part1 = {
    "1":"Bachelor's of ", 
    "2":"Master's of ",
    "3": "Ph.D. in ",
    "4": "Ph.D. in "
    }
part2 = {
    "01" : "Technology in Architecture", 
    "02" : "Technology in Chemical Engineering", 
    "03" : "Technology in Civil Engineering", 
    "05" : "Computer Applications", 
    "06" : "Technology in Computer Science (CSE)", 
    "07" : "Technology in Electrical & Electronics (EEE)", 
    "08" : "Technology in Electronics & Comm. (ECE)", 
    "10" : "Technology in Instrumentation & Control (ICE)", 
    "11" : "Technology in Mechanical Engineering", 
    "12" : "Technology in Metallurgical & Materials (MME)", 
    "14" : "Technology in Production Engineering", 
    "15" : "Management Studies", 
    "16" : "Mathematics"
    }
part4 = "20" + parts[4]


print(part1[parts[1]] + part2[parts[2]] + "\nYear of Admission: " + part4 + "\nRoll Number: " + parts[5])

                           
                   
                      
                  
                 
         
        