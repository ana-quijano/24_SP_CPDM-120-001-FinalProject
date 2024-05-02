from RentalShop import RentalShop
from Customer import Customer
from datetime import datetime, timedelta


# ---------------------------------------------------------------
# Function to set up the Ski and Snowboard Shop inventory
# ---------------------------------------------------------------

def SetUp_ShopInventory(intTotalSkis, intTotalSnowboards):
    print("")
    print("Bob's Skis and Snowboards Shop is now open.")
    print("There are ", intTotalSkis, " skis and ", intTotalSnowboards, " in the inventory.")



# ---------------------------------------------------------------
# Function to Display Navigational Selection
# display options for navigation and 
# ---------------------------------------------------------------

def Menu(intNavigate):
    print("")
    intNavigate = input("For New Customer Rental, enter 1.\nTo Return Rental, enter 2.\nTo Display Inventory, enter 3. \nTo Close Shop at End of Day, enter 4.\n")
    intNavigate = Validate_Navigation(intNavigate)
    MenuSelect(intNavigate)

# ---------------------------------------------------------------
# Function to Call NewCustomerRental, ReturnRental, DisplayInventory, or CloseShop
# ---------------------------------------------------------------

def MenuSelect(intNavigate):
    if intNavigate == 1:
    # Collect New Customer Rental Inputs
        NewCustomerRental(Customers, strFirstName = "", strLastName = "", strIDNumber = "", strPhoneNumber = "", strCouponCode = "", strRentalPeriod = "", intTime = 0, intSkis = 0, intSnowboards = 0)
    else:
        # This does not work yet
        if intNavigate == 2:
            ReturnRental(Customers)
        else:
            # This works!
            if intNavigate == 3:
                DisplayInventory(intAvailableSkis = 0, intAvailableSnowboards = 0)
            else:
                # This does not work yet
                if intNavigate == 4:
                    CloseShop()
                else:
                    if intNavigate == 0:
                        Menu(intNavigate)



# ---------------------------------------------------------------
# Function to Begin New Customer Rental
# ---------------------------------------------------------------

def NewCustomerRental(Customers, strFirstName, strLastName, strIDNumber, strPhoneNumber, strCouponCode, strRentalPeriod, intTime, intSkis, intSnowboards):
    print("")
    print("Enter Customer Rental Details")
    strFirstName = input("First Name: ")
    strLastName = input("Last Name: ")
    strIDNumber = input("ID Number: ")
    strPhoneNumber = input("Phone Number: ")
    strCouponCode = input("Coupon Code: ")
    strRentalPeriod = input("Rental Period (Hourly, Daily, or Weekly): ")
    intTime = int(input("Rental Time: "))
    intSkis = int(input("Number of Skis: "))
    intSnowboards = int(input("Number of Snowboards: "))
    print("")

    dblEstimate = float(0)
    dtmDateTimeRented = str("")
    dtmDateTimeReturned = str("")
    intAvailableSkis = int()
    intAvailableSnowboards = int()


    # Instantiate customer class
    #customer = Customer(strFirstName, strLastName, strIDNumber, strPhoneNumber, strCouponCode, strRentalPeriod)

    # Add object to list Customers
    Customers.append(Customer(strFirstName, strLastName, strIDNumber, strPhoneNumber, strCouponCode, strRentalPeriod))

    # Give estimate
    dblEstimate = Inventory.CalculateEstimate(strRentalPeriod, intSkis, intSnowboards, intTime, strCouponCode)
    print("Rental Price Estimate: ", dblEstimate)

    # Confirm rental
    strStartRental = input("Start Rental? Y/N: ")
    if strStartRental == 'Y':

        # Get index of latest customer added to list
        intLastCustomer = (len(Customers)) - 1
        
        # Attempt to start rental based on availability
        blnSuccessfulRental = Customers[intLastCustomer].RentItems(intSkis, intSnowboards)
        if blnSuccessfulRental == True:

            # Skis/Snowboards available, get starting rental time
            now = datetime.now()
            dtmDateTimeRented = now.strftime("%m/%d/%Y %H:%M")
            print("")
            print("Rental has started. Time: ", dtmDateTimeRented)

        else:

            # Display available skis and snowboards and ask to try again.
            intAvailableSkis = RentalShop.GetAvailableSkis()
            intAvailableSnowboards = RentalShop.GetAvailableSnowboards()
            print("")
            print("Sorry, only ", intAvailableSkis, " skis and ", intAvailableSnowboards, " snowboards are available.")

            # Give option to try another rental
            intNavigate = input("Enter 1 to try another rental.")
            MenuSelect(1)

    else:
        print("Rental canceled.")
        # Do not continue with rental, option to go back to main menu
        intNavigate = input("Enter 0 to go back to Main Menu.")
        MenuSelect(intNavigate)

    intNavigate = input("Enter 0 to go back to Main Menu.")
    Menu(intNavigate) 



# ---------------------------------------------------------------
# Function to Return Rental
# ---------------------------------------------------------------

def ReturnRental(Customers):

    strIDNumber = input("Enter ID Number: ")
    for obj in Customers:
        if strIDNumber == obj.strIDNumber:

            # Get customer information
            strFirstName = obj.strFirstName
            strLastName = obj.strLastName
            intSkis = obj.GetSkisRented()
            intSnowboards = obj.GetSnowboardsRented()
            strCouponCode = obj._strCouponCode

            # Get time rented and time returned
            now = datetime.now()
            dtmDateTimeRented = now.strftime("%m/%d/%Y %H:%M")

            dtmDateTimeReturned = timedelta(hours=-2)

            ## Get Subtotal, DiscountTotal, Total
            #(dblSubtotal, dblDiscountTotal, dblTotal) = Inventory.CalculateBill(dtmDateTimeRented, dtmDateTimeReturned, intSkis, intSnowboards, strCouponCode)

            # Display Invoice
            print("")
            print("Name: ", strFirstName, " ", strLastName)
            print("Skis Rented: ", intSkis)
            print("Snowboards Rented: ", intSnowboards)
            print("Total Time of Rental: ")
            print("Subtotal: ")
            print("Discount: ")
            print("Total: ")

            # Return rented skis and snowboards to inventory
            obj.ReturnItems()

    print("")
    intNavigate = input("Enter 0 to go back to Main Menu.")
    Menu(intNavigate) 



# ---------------------------------------------------------------
# Function to Display Current Inventory
# ---------------------------------------------------------------

def DisplayInventory(intAvailableSkis, intAvailableSnowboards):
    intAvailableSkis = RentalShop.GetAvailableSkis()
    intAvailableSnowboards = RentalShop.GetAvailableSnowboards()
    print("")
    print("Current Inventory")
    print("  Available Skis: ", intAvailableSkis)
    print("  Available Snowboards: ", intAvailableSnowboards)
    print("")
    intNavigate = input("Enter 0 to go back to Main Menu.")
    Menu(intNavigate)



# ---------------------------------------------------------------
# Function to Close Shop
# ---------------------------------------------------------------

def CloseShop():
    dblDailyRevenue = RentalShop.GetDailyRevenue()
    intDailySkisRented = RentalShop.GetDailySkisRented()
    intDailySnowboardsRented = RentalShop.GetDailySnowboardsRented()
    print("")
    print("Daily Summary")
    print("  Total Revenue: ", dblDailyRevenue)
    print("  Total Skis Rented: ", intDailySkisRented)
    print("  Total Snowboards Rented: ", intDailySnowboardsRented)
    print("Bob's Skis and Snowboards Rental Shop is now closed.\n")



# ---------------------------------------------------------------
# Validation Functions
# ---------------------------------------------------------------

def Validate_InitialSkis(intInput):
    try:
        intInput = int(intInput)
        if intInput > 0:
            global strInitialSkisFlag
            strInitialSkisFlag = True
        else:
            print("Number of skis cannot be less than zero.")
    except ValueError:
        intInput = int(0)
        print("Number of skis must be numeric.")
    return intInput

def Validate_InitialSnowboards(intInput):
    try:
        intInput = int(intInput)
        if intInput > 0:
            global strInitialSnowboardsFlag
            strInitialSnowboardsFlag = True
        else:
            print("Number of snowboards cannot be less than zero.")
    except ValueError:
        intInput = int(0)
        print("Number of snowboards must be numeric.")
    return intInput

def Validate_Navigation(intInput):
    try:
        intInput = int(intInput)
        if 0 < intInput < 5:
            return intInput
        else:
            print("Selection must be 1, 2, 3, or 4.")
    except ValueError:
        intInput = int(0)
        print("Selection must be 1, 2, 3, or 4.")



# ---------------------------------------------------------------
#
# Main Control
#
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# Declare Variables
# ---------------------------------------------------------------

blnShopOpen = bool(False)
strInitialSkisFlag = bool(False)
strInitialSnowboardsFlag = bool(False)
strNavigateFlag = bool(False)
intNavigate = int()
intMain = int(1)

intAvailableSkis = int()
intAvailableSnowboards = int()

Customers = []
Day = []

# ---------------------------------------------------------------
# Get and Validate RentalShop Class Inputs
# ---------------------------------------------------------------
print ("")

while strInitialSkisFlag is False:
    intTotalSkis = input("Enter Number of Skis in Inventory: ")
    intTotalSkis = Validate_InitialSkis(intTotalSkis)

while strInitialSnowboardsFlag is False:
    intTotalSnowboards = input("Enter Number of Snowboards in Inventory: ")
    intTotalSnowboards = Validate_InitialSnowboards(intTotalSnowboards)

# ---------------------------------------------------------------
# Call Functions
# ---------------------------------------------------------------

# Instantiate class RentalShop
Inventory = RentalShop(intTotalSkis, intTotalSnowboards)
SetUp_ShopInventory(intTotalSkis, intTotalSnowboards)

# Get intNavigate to determine next action
#(1 for new customer rental, 2 for return rental, 3 for inventory display, 4 for close shop)
intNavigate = Menu(intNavigate)

# Depending on action selected, call appropriate function
MenuSelect(intNavigate)

                