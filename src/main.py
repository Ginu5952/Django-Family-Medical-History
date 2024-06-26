
class MenuDisplay:

    @staticmethod
    def display_main_menu():
        print(
            """
            WELCOME TO FAMILY MEDICAL INFO APP

            MENU
            --------------
            1. INSERT DETAILS
            2. FETCH DETAILS
            3. QUIT
            """
        )

    @staticmethod
    def display_insert_menu():
        print(
            """
            1. INSERT HEALTH INSURANCE CARD DETAILS
            2. INSERT FAMILY MEDICAL INFO
            3. INSERT YEALY CHECK UP DETAILS
            4. INSERT CHILDREN VACCINATION DETAILS
            5. INSERT DOCTOR DETAILS
            6. INSERT HOSPITAL DETAILS
            7. INSERT FAMILY MEMBER DETAILS
            """
        )    

    @staticmethod
    def display_fetch_data_menu():
        print(
            """
            1. DISPLAY MEDICAL HISTORY
            2. DISPLAY HEALTH INSURANCE CARD EXPIRY DATE
            3. DISPLAY HOSPITAL DETAILS
            4. DISPLAY DOCTOR DETAILS
            5. DISPLAY YEARLY CHECK UP DETAILS
            6. DISPLAY CHILDREN VACCINATION DETAILS
            

        """
        )    

def main():
        MenuDisplay.display_main_menu()    
        option:int = int(input('Choose an option to continue: '))    

        if option == 1:
            MenuDisplay.display_insert_menu()
        elif option == 2:
            MenuDisplay.display_fetch_data_menu()
        elif option == 3:
            pass
        else:
            print("Invalid option")    


if __name__ == '__main__':
        main()                