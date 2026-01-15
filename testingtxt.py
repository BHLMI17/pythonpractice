#testing reading and writing onto a csv file
import csv
import pandas as pd
import os


class alterCSV:
    #ok so these lines allow you to write to a csv file, but i imagine if i change the mode to 'a' it will append instead of overwrite
    #similarly, changing mode to 'r' will allow reading
    # with open('testfile.csv', mode='w', newline='') as file:
    #     writer = csv.writer(file)
    inputfile = None
    



    @classmethod
    def initialiseCSV(cls, name ):
        filename = name+".csv"
        path = 'C:/github projects/java/pythonpractice'
        with open(os.path.join(path, filename),'w') as file:
          writer = csv.writer(file, delimiter=',', quotechar="|",quoting=csv.QUOTE_MINIMAL)  
          basic_info = ["id","username","password"]
          writer.writerow(basic_info)
        print("new file "+ name + ".csv created")
        # so what now then? I think i want to create a new file with a certain name            
        print(filename)


    
    def __init__(self, inputcsv):
        self.inputfile = inputcsv


    def ReadCSV(self, numberOfRows):
        with open(self.inputfile, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = []
            if self.determineNextAvailableID == 1:
                print("no rows in the csv file")
            for i, row in enumerate(reader):
                if i >= numberOfRows:
                    break
                rows.append(row)
        return rows
    

    def WriteCSV(self, username, password):
        with open(self.inputfile, mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            data = [self.determineNextAvailableID(), username, password]
            writer.writerow(data)

    #ok so apparently if you open it in 'a' mode it appends text to the end of the csv file
    def AppendCSV(self, username, password):
        with open(self.inputfile, mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            data = [self.determineNextAvailableID(), username, password]
            writer.writerow(data)


    #note that this used to be a class method, 
    # however this caused errors with compilation, as it determined that the self.inputfile was still set as none
    #much later down the line, but i might want to make it so that if i get a GUI, 
    # i end making a button that would allow any csv file to be instantiated, 
    # perhaps creating a system that a user can just use a practically empty file and turn it into a csv password file
    #then i could have a method that would instantiate the given column names onto an empty file, or offer to clear the file for them after
    #whats meant to happen here is that the user is asked for the password, which then goes through a whole nother check to 
    #to match the password to the username, but this is currently just for testing, so keep it like this for now
    def removeAccount(self):
        decision = input("would you like to search for the choose by username or ID? \n")

        while decision.lower() not in ("username", "id"):
            print("not a valid option, try again")
            decision = input("would you like to search for the choose by username or ID? \n")

        if decision.lower() == "username":
            self.removebyUsername()
        else:
            self.removebyID()
        
        




    def removebyUsername(self):
        username = input("please enter the username \n")

        df = pd.read_csv(self.inputfile)   # load CSV
        foundAcc = df[df["username"].str.contains(username, na=False)] #find the correct account by the keyword username and by the inputted username
        foundAccDetails = foundAcc.iloc[:, :2]  # id + username only

        if not foundAcc.empty:
            print("Account found, account details are:\n" + foundAccDetails.to_string()) #output the account details to make sure that the user can affirm

            chosenAccPassword = input("please enter the password for the corresponding account you have selected \n") # 2FA (sort of)
            correctPassword = foundAcc.iloc[0]["password"] # find the value in the row "password" in the first column that has the corresponding account

            if chosenAccPassword == correctPassword:
                finalChoice = input("are you certain that you would like to delete the account? 'y' for yes and 'n' for no \n")

                if finalChoice.lower() == "y":
                    row_index = foundAcc.index[0]   # exact row to delete
                    df = df.drop(row_index)         # delete it
                    df.to_csv(self.inputfile, index=False)  # save file
                    print("Account deleted successfully")
                else:
                    print("Deletion cancelled")
            else:
                print("incorrect password")
        else:
            print("no account with that name found")




    def removebyID(self):
        id = input("please enter the id \n")
        df = pd.read_csv(self.inputfile)   # load CSV
        foundAcc = df[df["id"].str.contains(id, na=False)] #find the correct account by the keyword username and by the inputted username
        foundAccDetails = foundAcc.iloc[:, :2]  # id + username only

        if not foundAcc.empty:
            print("Account found, account details are:\n" + foundAccDetails.to_string()) #output the account details to make sure that the user can affirm

            chosenAccPassword = input("please enter the password for the corresponding account you have selected \n") # 2FA (sort of)
            correctPassword = foundAcc.iloc[0]["password"] # find the value in the row "password" in the first column that has the corresponding account

            if chosenAccPassword == correctPassword:
                finalChoice = input("are you certain that you would like to delete the account? 'y' for yes and 'n' for no \n")

                if finalChoice.lower() == "y":
                    row_index = foundAcc.index[0]   # exact row to delete
                    df = df.drop(row_index)         # delete it
                    df.to_csv(self.inputfile, index=False)  # save file
                    print("Account deleted successfully")
                else:
                    print("Deletion cancelled")
            else:
                print("incorrect password")
        else:
            print("no account with that id found")
            
                




    def determineNextAvailableID(self):
        # If file doesn't exist or is empty, start at 1
        #wtf does the os library do?
        #ok, os library is exactly like it sounds, helps with os functionality
        #this method is to be altered later to check for id differences >1 so that it can replace redundant ids
        
        if not os.path.exists(self.inputfile) or os.path.getsize(self.inputfile) == 0:
            return 1

        df = pd.read_csv(self.inputfile)
        return len(df) + 1   
    


    #do i wanna focus on the encryption next or the security by making sure that multiple accounts can not have the same name 
    #it would be similar to a set in that regard
    #i could also work on the way to make sure that if you write on the csv, it ensures the header column is there, 
    #might be able to do that by making a refresh database method that just writes the column headers and nothing else  
    # crap, first thing should probably run a check to see if each id is unique 
    # and then maybe make a way to remove an individual id
    # a way to search up an account by id or username would be useful too      
    # would be similar to a map's way of searching for an item, by searching for the key and finding the value with it
    # should there be a way to also have the csv file rearrange itself after by having pointers,
    # but that would be more similar to a linked list


            