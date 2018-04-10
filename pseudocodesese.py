#Header Section
#My pseudocode project is based on the magical 8 ball idea, however, more like a daily mood lift with qoutes.
#End header

uplift_list = ["The way to get started is to quit talking and begin doing. -Walt Disney",
    "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. -Winston Churchill",
    "It takes a great deal of courage to stand up to your enemies, but even more to stand up to your friends. ~ J. K. Rowling",
    "You are more powerful than you know; you are beautiful just as you are. ~ Melissa Etheridge",
    "The power you have is to be the best version of yourself you can be, so you can create a better world. ~ Ashley Rickards",
    "If you obey all the rules, you miss all the fun. ~ Katharine Hepburn",
    "It took me quite a long time to develop a voice, and now that I have it, I am not going to be silent. ~ Madeleine Albright"
    "Forget about the fast lane. If you really want to fly, just harness your power to your passion. ~ Oprah Winfrey",
    "I can not think of any better representation of beauty than someone who is unafraid to be herself. ~ Emma Stone",
    "Courage is like a muscle. We strengthen it by use. ~ Ruth Gordo"
    ]

###Start Loop
go = True

####

### Menu options
def menu():
    """This function displays the menu and allows the user to input their choice"""
    
    print "\nWhat do you feel like doing?"
    
    user_options = """
    \tUplift Me [type upliftme] 
    \tShow me List of Qoutes [type showme]
    \tAdd to Qoute list [type add]
    \tDelete a Qoute from list [type del]
    \tEdit a Qoute from the list [type edit]
    \tLucky Number - [type lucky] 
    \tExit [type exit]
    
    Enter your choice: """
    
    user_choice = raw_input(user_options)
    return user_choice

### End Menu options

### Start uplift list fuction
def uplift():
    import random
    print " "
    print '\t' + user_name + " - " + random.choice(uplift_list)
    
###End Uplift fuction

###Start Show me list of qoutes
def show_list(lst):
    print '\n\n'.join(lst)

###End show me list of qoutes

###Start add qoute function

def add_qoute(lst):
    """This will obtain new qoute to add qoute list"""
    new_qoute = raw_input("\tEnter the new qoute you wish to add to list: ")
    
    """This will add the append the qoute list"""
    lst.append(new_qoute)
    print "Your qoute, {}, has been added.".format(new_qoute)
    print '\n\n'.join(lst)
    
    """This will store the qoute into the qoute list"""    
    
    return lst 
    
###End add qoute

### Start delete a qoute function
def delete_qoute(lst):
    """deletes a qoute from the list"""
    
    """This first prints a list of qoutes"""
    print '\n\n'.join(lst)
    
    del_qoute = raw_input("\nWhich qoute would you liked to delete?:\n>>> ")

    for item in lst:

        if item == del_qoute:

            lst.remove(item)
            print "Your qoute, {}, has been deleted.".format(del_qoute)
            
            print '\n\n'.join(lst)
            
            return lst
    
    print "Your qoute, {}, has not been found.".format(del_qoute)

### End delete qoute function

### Start Edit qoute function
def edit(lst):
    """Edits qoute in the list"""
    
    print '\n\n'.join(lst)
    
    edit_qoute = raw_input("\t\nType qoute you wish to edit:\n>>>")
    
    for index in range(len(lst)):

        if lst[index] == edit_qoute:

            edited_qoute = raw_input("\nWhat would you like to change the qoute to?\n>>> ")
            lst[index] = edited_qoute
            print "Your qoute has been edited."
            
            print '\n\n'.join(lst)
            
            return lst
    
### End edit qoute function
### Start lucky_numbers fuction

def lucky_numbers():
    #a command to choose a lucky number, using the random
    import random
    numberList = range(0, 100)
    lucky_1 = random.choice(numberList)
    
    print " "
    print '\t' + user_name + " - your special number today is", lucky_1
    
###End Uplift fuction


print "\nWelcome to your daily uplift!"

user_name = raw_input("\nMay I have your name?: ")

#User will enter if they want to be uplifted or would like a joke

while go:
    user_choice = menu()

    if user_choice == "exit":
        go == False
        break

    elif user_choice == "upliftme":
        uplift()
        
    elif user_choice == "showme":
        show_list(uplift_list)
        
    elif user_choice == "add"        :
        add_qoute(uplift_list)
        
    elif user_choice == "del"        :
        delete_qoute(uplift_list)
    
    elif user_choice == "edit":
        edit(uplift_list)

    elif user_choice == "lucky":
        lucky_numbers()
        
        #Based on user input an lucky numbers will be printed from a table of qoutes.

    else:
        print "Please choose a valid option."

