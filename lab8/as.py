# Assignment  
# 任務
# Write a program to compute the employee management system.  The requirements are listed below: 
# 編寫一個程序來計算員工管理系統。要求如下：
# This Employee Management System has 5 functions.  Users are allowed to display all employee information, display company statistics, add and remove an employee, update employee salary by specify employee's ID  
# 該員工管理系統有5個功能。允許用戶顯示所有員工信息，顯示公司統計，添加和刪除員工，通過指定員工ID更新員工工資
# To add an employee record, user is required to input employee's name, salary and department.  Employee ID  should be auto generate follow along with the last employee's record ID  
# 要添加員工記錄，用戶需要輸入員工的姓名、工資和部門。員工 ID 應該是自動生成的，跟在最後一個員工的記錄 ID 之後
# To remove an employee record, user is required to input the employee's ID  
# 要刪除員工記錄，用戶需要輸入員工的 ID
# To update an employee salary, user is required to input the employee's ID and salary. 
# 要更新員工工資，用戶需要輸入員工的 ID 和工資。
# All employee information should be displayed for user as a reference when user perform remove employee  and update employee's salary action  
# 當用戶執行刪除員工和更新員工工資操作時，應顯示所有員工信息以供用戶參考
# The list of all employee information is stored in a text file named " employee_list.txt" 
# 所有員工信息的列表存儲在名為“employee_list.txt”的文本文件中
# A sample output of normal flow is shown below:
# 正常流的示例輸出如下所示：

# Follow the steps below to implement the program:
# 請按照以下步驟實施該計劃：
# 1. Declare a constant tuple named DEPARTMENT to store the department that can be selected when add an employee
# 1.聲明一個名為DEPARTMENT的常量元組，用於存儲添加員工時可以選擇的部門
# record. Department includes HR, IT, Admin and Finance.
# 記錄。部門包括人力資源、信息技術、行政和財務。
# 2. Declare the following constants for index of functions in the main menu.
# 2. 為主菜單中的函數索引聲明以下常量。

# 4. Write a function display_all_employees to display all employee records for the menu item 1 - Display all employee
# 4.寫一個函數display_all_employees來顯示菜單項1的所有員工記錄-顯示所有員工
# function as shown in the above sample output. This function should also be called before remove an employee, update
# 功能如上面的示例輸出所示。在刪除員工、更新之前也應該調用此函數
# employee salary and display company statistics. The list of employees (i.e. Iist_dict_employee) should also be passed
# 員工工資並顯示公司統計數據。還應傳遞員工列表（即 Iist_dict_employee）
# into this function when calling.
# 調用時進入這個函數。

# 5. Write a function read_employee_from_file to read in employee's information from file named “employee.txt”
# 5. 編寫函數read_employee_from_file，從名為“employee.txt”的文件中讀取員工信息
# located in the same folder. The sample file “employee.txt“ is given for you already and should follow the same format.
# 位於同一文件夾中。示例文件“employee.txt”已經為您提供，並且應遵循相同的格式。
# Zero marks will be given if you assigned the employee data by static variable such as list_dict_employees = {...}
# 如果您通過 list_dict_employees = {...} 等靜態變量分配員工數據，則將給出零分

# 6. The main function should contain the following logics:
# 6. main函數應該包含如下邏輯：
# • Read in employee's information from file named “employee.txt“ located in the same folder.
# • 從位於同一文件夾中名為“employee.txt”的文件中讀取員工信息。
# • Display a welcome message and followed by the main menu of employee management system. Users can display
# • 顯示歡迎信息，然後是員工管理系統的主菜單。用戶可以顯示
# all employee's information, add and remove employee, update employee salary and display company statistics.
# 所有員工的信息，添加和刪除員工，更新員工工資和顯示公司統計數據。
# • To add an employee, user is required to input employee's name, salary and department. Employee ID should be
# • 要添加員工，用戶需要輸入員工姓名、工資和部門。員工 ID 應該是
# auto-generated follow along with the last employee's employee ID
# 自動生成的跟隨以及最後一名員工的員工 ID
# • To remove an employee record, user is required to input the employee's ID.
# • 要刪除員工記錄，用戶需要輸入員工的ID。
# • To update an employee salary, user is required to input the employee/s ID and salary.
# • 要更新員工工資，用戶需要輸入員工ID 和工資。
# • Display all employee and company's employee statistics on request. For details please reference to sample output provided.
#  根據要求顯示所有員工和公司的員工統計數據。有關詳細信息，請參考提供的示例輸出。
# • Handle all errors inputted by user and ask user to correct and input the same data again immediately, such as
# • 處理用戶輸入的所有錯誤，並要求用戶立即更正並再次輸入相同的數據，例如
# but not limited to incorrect menu function number, incorrect employee name, incorrect employee ID, incorrect
# 但不限於錯誤的菜單功能編號、錯誤的員工姓名、錯誤的員工 ID、錯誤的
# salary, incorrect department, etc.
# 工資，錯誤的部門等。

# 7. Complete the corresponding parts in the main() function to perform the add employee function for menu item 2 -
# Add an employee. This part does at least the followings：
# • Ask user to input for employee's name, employee's salary and employee's department. Return to previous menu
# when user pressed Enter directly and validate user's input where necessary.
# • Obtain the employee ID from the last employee ID in the system and calculate the employee ID of the new
# employee ID
# • Create the employee record based on user's input and new employee ID calculated (should be in dictionary data
# type)
# • Append the new created employee record to the list of employees
# 7.完成main()函數中的相應部分，執行菜單項2的添加員工功能——
# 添加一名員工。這部分至少做了以下工作：
# • 要求用戶輸入員工姓名、員工工資和員工部門。返回上一級菜單
# 當用戶直接按下 Enter 並在必要時驗證用戶的輸入。
# • 從系統中最後一個工號獲取工號，計算新的工號
# 員工ID
# • 根據用戶輸入和計算出的新員工ID 創建員工記錄（應在字典數據中
# 類型）
# • 將新創建的員工記錄附加到員工列表中

# 8. Complete the corresponding parts in the main() function to perform the remove employee function for menu item 3
# - Remove an employee. This part does at least the followings:
# • Display all employees by calling the display_all_employees function for user to choose the employee to remove.
# • Ask user to input for employee's ID. Return to previous menu when user pressed Enter directly and validate user's
# input where necessary.
# • Loop through the list of employees and remove the employee record from the list if exist.
# 8.完成main()函數中的相應部分，執行菜單項3的remove employee功能
# - 刪除員工。這部分至少做了以下工作：
# • 通過調用display_all_employees 函數顯示所有員工，供用戶選擇要刪除的員工。
# • 要求用戶輸入員工ID。當用戶直接按下 Enter 時返回上一級菜單並驗證用戶的
# 必要時輸入。
# • 遍歷員工列表並從列表中刪除員工記錄（如果存在）。

# 9. Complete the corresponding parts in the main() function to perform the update employee salary function for menu
# item 4 - Update employee salary. This part does at least the followings:
# • Display all employees by calling the display_all_employees function for user to choose the employee to perform
# salary update.
# • Ask user to input for employee's ID and employee's updated salary. Return to previous menu when user pressed
# Enter directly and validate user's input where necessary.
# • Loop through the list of employees and update the employee's salary in the list if exist.
# 9.完成main()函數中的相應部分，執行menu的更新員工工資功能
# 第 4 項 - 更新員工薪水。這部分至少做了以下工作：
# • 調用display_all_employees函數顯示所有員工，供用戶選擇執行的員工
# 工資更新。
# • 要求用戶輸入員工ID 和員工更新後的薪水。用戶按下時返回上一級菜單
# 直接輸入並在必要時驗證用戶的輸入。
# • 遍歷員工列表並更新列表中員工的薪水（如果存在）。

# 10. Complete the corresponding parts in the main()function to perform the display company statistics function for mitem 5 - Display company statistics. This part does at least the followings:
# 10.完成main()函數中的相應部分，為mitem 5-Display company statistics執行顯示公司統計功能。這部分至少做了以下工作：
# • Display all employees information by calling the display_all_employees function
# • 調用display_all_employees函數顯示所有員工信息
# • Display the company statistics by showing the no. of staff, highest salary, lowest salary and average salary in each
# • 通過顯示編號來顯示公司統計信息。員工人數、最高薪資、最低薪資和平均薪資
# department.
# 部。
# • Display the total number of staff, highest salary, lowest salary and average salary in this company
# • 顯示該公司員工總數、最高薪資、最低薪資及平均薪資

# Important Hints:
# You may implement some minor functions at last, such as reading employee's information from the file, and most
# of the input validation. Such as validation of new add employee name, salary, department, employee ID for remove
# and update function, etc.
# 重要提示：
# 最後你可能會實現一些小功能，比如從文件中讀取員工的信息，以及大多數
# 輸入驗證。比如新增員工姓名、薪水、部門、員工ID的校驗等
# 和更新功能等。

# Instruction to students:
# 1. This is an End of Module Assessment and the weighting of this assignment is 20% of the Module Mark.
# 2. This assignment should be done by each individual student. Plagiarism will be treated seriously. All assignments that
# have been found involved wholly or partly in plagiarism (no matter these assignments are from the original authors
# or from the plagiarists) will score Zero marks.
# 3. You must use Python 3 to develop the programs.
# 4. Your programs must follow the style guide stated in PEP8 - Style Guide for Python Code published by .
# htt—s:〃 . Marks may be deducted if the style guide is not followed.
# py
# 對學生的指導：
# 1. 這是模塊評估的結束，此作業的權重為模塊標記的 20%。
# 2. 這個作業應該由每個學生單獨完成。抄襲將嚴肅處理。所有作業
# 已被發現全部或部分涉及剽竊（無論這些作業來自原作者
# 或來自剽竊者）將獲得零分。
# 3. 您必須使用Python 3 來開發程序。
# 4. 您的程序必須遵循 PEP8 - Style Guide for Python Code 發布的風格指南。
# htt—s:〃 .如果不遵循風格指南，可能會扣分。
# py