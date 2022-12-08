###############################################
# Imports used                                #
# You may import other libraries if necessary #
###############################################
import sys
import re
import locale
locale.setlocale( locale.LC_ALL, 'English_United States.1252' )
#################################################
# Constants used                                #
# You may add other constants here if necessary #
#################################################

# constant tuple named DEPARTMENT to store the department that can be selected when add
DEPARTMENT = ("HR","IT","Admin", "Finance")


# Function ID mapped with name
RETURN = ""
DISPLAY_ALL_EMPLOYEES = 1
ADD_AN_EMPLOYEE = 2
REMOVE_AN_EMPLOYEE = 3
UPDATE_EMPLOYEE_SALARY = 4
DISPLAY_STATISTICS = 5

# Other constants here



#################################################
# Functions used                                #
# You may add other functions here if necessary #
#################################################


# write a function display_all_employees for menu item 1 to display all employees in system
def display_all_employees(list_dict_employees):
    # complete your function here
    # this function have no return value
    print("")
    print("ALL emplotee(s) information:")
    print(f"{'ID':<10s} | {'Name':<21s} | {'Salary':<15s}| {'Department':<11s}" )
    for list_dict_employee in list_dict_employees:
        print(list_dict_employee["ID"].ljust(10),"|",list_dict_employee["Name"].ljust(21),"|",str(locale.currency(float(list_dict_employee["Salary"]), grouping = True).ljust(14)),"|",list_dict_employee["Department"].ljust(11))
    print("")
            

# write a function display_stat for menu item 5 to display company statistics in system
def display_stat(list_dict_employees):
    # complete your function here
    # this function have no return value
    data_hr = dict()
    data_it = dict()
    data_admin = dict()
    data_finance = dict()
    display_all_employees(list_dict_employees)
    for x in range(len(list_dict_employees)):
        
        if list_dict_employees[x]["Department"]=="HR":
            if "no_of_staff" not in data_hr:
                data_hr["no_of_staff"]=1
            else:
                data_hr["no_of_staff"]=data_hr["no_of_staff"]+1

            

            if "Lowest_Salary" not in data_hr:
                data_hr["Lowest_Salary"]=list_dict_employees[x]["Salary"]
            else:
                if float(data_hr["Lowest_Salary"])<float(list_dict_employees[x]["Salary"]):
                    pass
                else:
                    data_hr["Lowest_Salary"]=list_dict_employees[x]["Salary"]

  
  
            if "Highest_Salary" not in data_hr:
                data_hr["Highest_Salary"]=list_dict_employees[x]["Salary"]
            else:
                if float(data_hr["Highest_Salary"])<float(list_dict_employees[x]["Salary"]):
                    data_hr["Highest_Salary"]=list_dict_employees[x]["Salary"]
                else:
                    pass

            
            if "Total_Salary" not in data_hr:
                data_hr["Total_Salary"]=float(list_dict_employees[x]["Salary"])
            else:
                data_hr["Total_Salary"]=data_hr["Total_Salary"]+float(list_dict_employees[x]["Salary"])
 
            
        if list_dict_employees[x]["Department"]=="IT":
            if "no_of_staff" not in data_it:
                data_it["no_of_staff"]=1
            else:
                data_it["no_of_staff"]=data_it["no_of_staff"]+1
   

            if "Lowest_Salary" not in data_it:
                data_it["Lowest_Salary"]=list_dict_employees[x]["Salary"]
            else:
                if float(data_it["Lowest_Salary"])<float(list_dict_employees[x]["Salary"]):
                    pass
                else:
                    data_it["Lowest_Salary"]=list_dict_employees[x]["Salary"]
          
  
  
            if "Highest_Salary" not in data_it:
                data_it["Highest_Salary"]=list_dict_employees[x]["Salary"]
            else:
                if float(data_it["Highest_Salary"])<float(list_dict_employees[x]["Salary"]):
                    data_it["Highest_Salary"]=list_dict_employees[x]["Salary"]
                else:
                    pass
          
            
                        
            if "Total_Salary" not in data_it:
                data_it["Total_Salary"]=float(list_dict_employees[x]["Salary"])
            else:
                data_it["Total_Salary"]=data_it["Total_Salary"]+float(list_dict_employees[x]["Salary"])
         
            
        if list_dict_employees[x]["Department"]=="Admin":
            if "no_of_staff" not in data_admin:
                data_admin["no_of_staff"]=1
            else:
                data_admin["no_of_staff"]=data_admin["no_of_staff"]+1
           
            
            if "Lowest_Salary" not in data_admin:
                data_admin["Lowest_Salary"]=list_dict_employees[x]["Salary"]
            else:
                if float(data_admin["Lowest_Salary"])<float(list_dict_employees[x]["Salary"]):
                    pass
                else:
                    data_admin["Lowest_Salary"]=list_dict_employees[x]["Salary"]
           
  
  
            if "Highest_Salary" not in data_admin:
                data_admin["Highest_Salary"]=list_dict_employees[x]["Salary"]
            else:
                if float(data_admin["Highest_Salary"])<float(list_dict_employees[x]["Salary"]):
                    data_admin["Highest_Salary"]=list_dict_employees[x]["Salary"]
                else:
                    pass
           
            
                        
            if "Total_Salary" not in data_admin:
                data_admin["Total_Salary"]=float(list_dict_employees[x]["Salary"])
            else:
                data_admin["Total_Salary"]=data_admin["Total_Salary"]+float(list_dict_employees[x]["Salary"])
      

            
        if list_dict_employees[x]["Department"]=="Finance":
            if "no_of_staff" not in data_finance:
                data_finance["no_of_staff"]=1
            else:
                data_finance["no_of_staff"]=data_finance["no_of_staff"]+1
      
            
            if "Lowest_Salary" not in data_finance:
                data_finance["Lowest_Salary"]=list_dict_employees[x]["Salary"]
            else:
                if float(data_finance["Lowest_Salary"])<float(list_dict_employees[x]["Salary"]):
                    pass
                else:
                    data_finance["Lowest_Salary"]=list_dict_employees[x]["Salary"]
      
  
  
            if "Highest_Salary" not in data_finance:
                data_finance["Highest_Salary"]=list_dict_employees[x]["Salary"]
            else:
                if float(data_finance["Highest_Salary"])<float(list_dict_employees[x]["Salary"]):
                    data_finance["Highest_Salary"]=list_dict_employees[x]["Salary"]
                else:
                    pass

            
            if "Total_Salary" not in data_finance:
                data_finance["Total_Salary"]=float(list_dict_employees[x]["Salary"])
            else:
                data_finance["Total_Salary"]=data_finance["Total_Salary"]+float(list_dict_employees[x]["Salary"])
   
            
    print("Company statistics:")
    print(f"{'Department':<12s} | {'No. of staff':<12s} | {'Highest Salary':<12s} | {'Lowest Salary':<12s} | {'Average Salary':<12s}" )
    print(f"{'HR':<12s} | {data_hr['no_of_staff']:12} | ${float(data_hr['Highest_Salary']):>13} | ${float(data_hr['Lowest_Salary']):>12} | ${round(data_hr['Total_Salary']/data_hr['no_of_staff'],1):>13}" )
    print(f"{'IT':<12s} | {data_it['no_of_staff']:12} | ${float(data_it['Highest_Salary']):>13} | ${float(data_it['Lowest_Salary']):>12} | ${round(data_it['Total_Salary']/data_it['no_of_staff'],1):>13}" )
    print(f"{'Admin':<12s} | {data_admin['no_of_staff']:12} | ${float(data_admin['Highest_Salary']):>13} | ${float(data_admin['Lowest_Salary']):>12} | ${round(data_admin['Total_Salary']/data_admin['no_of_staff'],1):>13}" )
    print(f"{'Finance':<12s} | {data_finance['no_of_staff']:12} | ${float(data_finance['Highest_Salary']):>13} | ${float(data_finance['Lowest_Salary']):>12} | ${round(data_finance['Total_Salary']/data_finance['no_of_staff'],1):>13}" )
    print("")
    print("Total number of staff:",len(list_dict_employees))
    Hightest_Salary=0
    for x in range(len(list_dict_employees)):
        if Hightest_Salary==0 or float(list_dict_employees[x]["Salary"])>Hightest_Salary:
            Hightest_Salary=float(list_dict_employees[x]["Salary"])
    Hightest_Salary="${:,.1f}".format(Hightest_Salary)
    print(f"Hightest Salary      : {Hightest_Salary:>10}")
    
    Lowest_Salary=0
    for x in range(len(list_dict_employees)):
        if Lowest_Salary==0 or float(list_dict_employees[x]["Salary"])<Lowest_Salary:
            Lowest_Salary=float(list_dict_employees[x]["Salary"])
    Lowest_Salary="${:,.1f}".format(Lowest_Salary)
    print(f"Lowest Salary        : {Lowest_Salary:>10}")
    
    Average_Salary=0
    for x in range(len(list_dict_employees)):
        Average_Salary+=float(list_dict_employees[x]["Salary"])
    Average_Salary="${:,.1f}".format(Average_Salary/len(list_dict_employees))
    print(f"Average Salary       : {Average_Salary:>10}")




# write a function read_employee_from_file to read in employee’s information from file named "employee.txt" located in the same folder
def read_employee_from_file():
    list_dict_employees = list()
    # complete your function here
    filename = "employee_list.txt"
    file_handler = open ( filename )
    pattern = r"^(IVE\d*),(.*),(.*),(.*)"
    #print(file_handler.read ( ) )
    # this function should return a list of dictionary contains all employee's information

    for line in file_handler:
        ldict=dict()
        line = line.rstrip ( )
        result = re.search(pattern, line)
        if result != None:
            #print(result.group(1).lstrip())
            ldict["ID"]=result.group(1)
            #print(result.group(2).lstrip())
            ldict["Name"]=result.group(2).lstrip()
            #print(result.group(3).lstrip())
            ldict["Salary"]=result.group(3).lstrip()
            #print(result.group(4).lstrip())
            ldict["Department"]=result.group(4).lstrip()
            list_dict_employees.append(ldict)
    file_handler.close ( )








    # This static variable is for your development in early stage
    # Zero marks will be given if you assigned the employee data by this static variable    
    """
    list_dict_employees = [
        {"ID": "IVE00001", "Name": "Kelvin Yip", "Salary" : 43210.5, "Department": "IT" },
        {"ID": "IVE00002", "Name": "Cow Leung", "Salary" : 32105.4, "Department": "Admin" },
        {"ID": "IVE00003", "Name": "Leung Pig Hung", "Salary" : 21054.3, "Department": "HR" },
        {"ID": "IVE00004", "Name": "Michael Fung", "Salary" : 10543.2, "Department": "Finance" },
        {"ID": "IVE00005", "Name": "Joe Yeung", "Salary" : 6543.2, "Department": "IT" },
        {"ID": "IVE00006", "Name": "Martin Kung", "Salary" : 5432.1, "Department": "Admin" }
    ]
    """
    return list_dict_employees
    

# You may implement other necessary functions here







# Main function starts here
def main():

    # Read employees record from file
    list_dict_employees = read_employee_from_file()

        


    # Main menu
    while True:
        print("=======================================")
        print("Employee Management System Menu:")
        print("No. | Function")
        print("1   | Display all employee")
        print("2   | Add an employee")
        print("3   | Remove an employee")
        print("4   | Update employee salary")
        print("5   | Display company statistics")
        input_function = None
        input_function = input("Please input your choice. (1 – 5, Enter to exit): ")
        if input_function=="":
            break
        while True:
            try:
                input_function=int(input_function)
                if input_function ==1 or input_function ==2 or input_function ==3 or input_function ==4 or input_function ==5:
                    break
                else:
                    print ( "Invalid input for choice" )
                    input_function = input("Please input your choice. (1 – 5, Enter to exit): ")

            except ValueError:
                print ( "Invalid input for choice" )
                input_function = input("Please input your choice. (1 – 5, Enter to exit): ")
    
        


        # When user input 1 to display all employee
        if input_function == DISPLAY_ALL_EMPLOYEES:
            display_all_employees(list_dict_employees)
        # 2
        elif input_function == ADD_AN_EMPLOYEE:
            ldict=dict()
            while True:
                input_employee_name = input("Please input employee's name,Enter to return:")
                if input_employee_name == "":
                    input_function=None
                    main()
                    break
                if re.fullmatch(r'^([^0-9]*)$', input_employee_name):
                    break
                else:
                    print("Not a valid employee name")
                    print("Employee's name should not contain digit")
                    
            while True:
                if input_employee_name == "":
                    input_function=None
                    main()
                    break
                try:
                    input_employee_salary = input("Please input employee's salary,Enter to return:")
                    # When user pressed enter - break
                    if input_employee_salary == "":
                        input_function=None
                        main()
                        break
                    if float(input_employee_salary)<=0:
                        print("Employee's salary should be greater than 0")
                        pass
                    else:
                        break
                except:
                    print ( "Employee's salary error please try again" )
            while True:
                if input_employee_name == "":
                    input_function=None
                    main()
                    break
                if input_employee_salary == "":
                    input_function=None
                    main()
                    break
                input_employee_department = input("Please input employee's department,Enter to return:") 
                if input_employee_department == "":
                    input_function=None
                    main()
                    break
                try:
                    DEPARTMENT.index(input_employee_department)
                    break
                except:
                    print("Not a valid department")
                    word=""
                    for x in range(len(DEPARTMENT)):
                        if x == len(DEPARTMENT)-1: 
                            word=word+str(DEPARTMENT[x])
                        else:
                            word=word+str(DEPARTMENT[x])+"/"
                            
                    
                    print("Employee's department should be",word)

            for x in range(len(list_dict_employees)):
                if input_employee_name == list_dict_employees[x]["Name"]:
                    
                    list_dict_employees[x]["Salary"]=input_employee_salary
                    list_dict_employees[x]["Department"]=input_employee_department
                    print("***** Employee Added Successfully *****")
                    break
                else:
                    if x == len(list_dict_employees)-1:
                        employee_id=1+int(list_dict_employees[-1]["ID"][3:])
                        ldict["ID"]="IVE"+str(employee_id).zfill(5)
                        ldict["Name"]=input_employee_name
                        ldict["Salary"]=input_employee_salary
                        ldict["Department"]=input_employee_department
                        list_dict_employees.append(ldict)
                        print("***** Employee Added Successfully *****")
                        break
            
        # When user input 3 to remove employee record
        elif input_function == REMOVE_AN_EMPLOYEE:
            display_all_employees(list_dict_employees)
            print("")
            while True:
                input_employee_id = input("Please input employee's ID to remove record,Enter to return:")
                if input_employee_id == "":
                    input_function=None
                    main()
                if re.fullmatch(r'([I][V][E][\d][\d][\d][\d][\d])', input_employee_id):

                    break
                else:
                    print("Not a valid employee's ID")
                    print("Employee's ID record not found")
                
            id_list=list()
            
            for x in range(len(list_dict_employees)):
                id_list.append(list_dict_employees[x]['ID'])
            while True:
                try:
                    list_dict_employees.pop(id_list.index(input_employee_id))
                    print("***** Employee Removed Successfully *****")
                    break
                except:
                    print("Not a valid employee's ID")
                    print("Employee's ID record not found")
                    input_employee_id = input("Please input employee's ID,Enter to return:")
                    if input_employee_id == "":
                        print("")
                        input_function=None
                        main()
                        
                


        # When user input 4 to update an employee salary
        elif input_function == UPDATE_EMPLOYEE_SALARY:
            display_all_employees(list_dict_employees)
            while True:
                input_employee_id = input("Please input employee's ID Enter to return:")
                if input_employee_id == "":
                    input_function=None
                    main()
                if re.fullmatch(r'([I][V][E][\d][\d][\d][\d][\d])', input_employee_id):

                    break
                else:
                    print("Not a valid employee's ID")
                    print("Employee's ID record not found")

            while True:
                id_list=list()
                try:
                    for x in range(len(list_dict_employees)):
                        id_list.append(list_dict_employees[x]['ID'])
                    if id_list.index(input_employee_id)!=None:
                        break
                except:
                    print("Not a valid employee's ID")
                    print("Employee's ID record not found")
                    input_employee_id = input("Please input employee's ID,Enter to return:")
                    if input_employee_id == "":
                        print("")
                        main()
            while True:
                try:
                    input_employee_salary = input("Please input employee's updated salary,Enter to return:")
                    # When user pressed enter - break
                    if input_employee_salary == "":
                        input_function=None
                        main()
                        break
                    input_employee_salary=float(input_employee_salary)
                    if float(input_employee_salary)<=0:
                        print("Employee's salary should be greater than 0")
                        pass
                    else:
                        break
                except:
                    print ( "Employee's salary error please try again" )
            while True:
                if input_employee_salary == "":
                    input_function=None
                    main()
                    break
                # input_employee_department = input("Please input employee's department,Enter to return:")
                # if re.fullmatch(r'(IT|HR|Admin|Finance)', input_employee_department):
                #     break
                # else:
                #     print("Not a valid department")
                #     print("Employee's department should be HR/IT/Admin/Finance")

            for list_dict_employee_len in range(len(list_dict_employees)):
                if list_dict_employees[list_dict_employee_len]["ID"] == input_employee_id:
                    print(list_dict_employees[list_dict_employee_len]["Salary"])
                    list_dict_employees[list_dict_employee_len]["Salary"] = input_employee_salary

            print("***** Employee Updated Successfully *****")





        # When user input 5 to display company statistics
        elif input_function == DISPLAY_STATISTICS:
            display_stat(list_dict_employees)
        


    
if __name__ == "__main__":
    # Welcome message
    print("Welcome to Employee Management System.")
    input_function=None
    main()
