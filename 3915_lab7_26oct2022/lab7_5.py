# your code goes here
def display_applicants(applicants):
    new_display_list=list()
    for x in applicants:
        # print(x)
        display_list=list()
        for y in range(len(applicants)):
            # print(x.split()[0])
            display_list.append("Applicant ID: "+str(x.split()[0]))
            display_list.append("User Name: "+str(x.split()[1].split("@")[0]))
            display_list.append("Phone "+str(x.split()[2]))
            # print(len(x.split()[3:]))
            display_list.append("This applicant applies for "+str(len(x.split()[3:]))+" subjects")
            break
        for z in range(len(x.split()[3:])):
            # print(z)
            tlist=list()
            for t in x.split()[3:]:
                # print(t,"t")
                tlist.append(t)
                # print(tlist)
            display_list.append("Subject "+str(z+1)+": "+tlist[z])

        # print(display_list)
        new_display_list.append(display_list)
        # print(new_display_list)
    print("Total applicants:",len(new_display_list)) 
    for k in new_display_list:
        print("---")
        for n in k:
            print(n)


 
# Output Generation. You are not allowed to modify the following codes
def main():
    applicants = [
        "001 kelvinyip@vtc.edu.hk 25952537 Programming Networking Database",
        "002 cowleung@nomail.com 98765432 Cloud Security AI BigData",
        "003 peterpan@nomail.com 23456789 Web MobileComputing"
    ]
    display_applicants(applicants)
 
if __name__ == "__main__":
    main()
