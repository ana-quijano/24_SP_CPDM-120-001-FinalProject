from RentalShop import RentalShop
from Customer import Customer
from datetime import datetime


# ---------------------------------------------------------------
# Function to set up the Ski and Snowboard Shop inventory
# ---------------------------------------------------------------

def SetUp_ShopInventory(intTotalSkis, intTotalSnowboards):
    print("Bob's Skis and Snowboards Shop is now open.\n")
    print("There are ", intTotalSkis, " skis and ", intTotalSnowboards, " in the inventory.\n")

# ---------------------------------------------------------------
# Function to Display Navigational Selection
# display options for navigation and 
# ---------------------------------------------------------------
def NavigationalSelection(intNavigate):
    intNavigate = input("For New Customer Rental, enter 1.\nTo Return Rental, enter 2.\nTo Display Inventory, enter 3. \nTo Close Shop at End of Day, enter 4.\n")
    intNavigate = Validate_Navigation(intNavigate)
    return intNavigate 

def GetNavigate(intNavigate):
    if intNavigate == 1:
    # Collect New Customer Rental Inputs
        NewCustomerRentalInputs(strFirstName = "", strLastName = "", strIDNumber = "", strPhoneNumber = "", strCouponCode = "", strRentalPeriod = "", intTime = 0, intSkis = 0, intSnowboards = 0, dblEstimate = 0, intAvailableSkis = 0, intAvailableSnowboards = 0)
    else:
        # This does not work yet
        if intNavigate == 2:
            ReturnRental()
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
                        NavigationalSelection(intNavigate)

# ---------------------------------------------------------------
# Function to Begin New Customer Rental
# ---------------------------------------------------------------

def NewCustomerRentalInputs(strFirstName, strLastName, strIDNumber, strPhoneNumber, strCouponCode, strRentalPeriod, intTime, intSkis, intSnowboards, dblEstimate, intAvailableSkis, intAvailableSnowboards):
    print("")
    print("Enter Customer Rental Request Details Details")
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

    dtmDateTimeRented = str("")
    dtmDateTimeReturned = str("")

    # Give estimate
    dblEstimate = Inventory.CalculateEstimate(strRentalPeriod, intSkis, intSnowboards, intTime, strCouponCode)
    print("Rental Price Estimate: ", dblEstimate)
    # Confirm rental
    strStartRental = input("Would you like to start your rental? Y/N: ")
    if strStartRental == 'Y':
        # Attempt to start rental based on availability
        blnSuccessfulRental = Customer.RentItems(intSkis, intSnowboards)
        if blnSuccessfulRental == True:
            customer1 = Customer(strFirstName, strLastName, strIDNumber, strPhoneNumber, strCouponCode, strRentalPeriod)
            now = datetime.now()
            dtmDateTimeRented = now.strftime("%m/%d/%Y %H:%M")
            print("Your rental has started. Time: ", dtmDateTimeRented, ".")
    else:
        # Display available skis and snowboards and ask to try again.
        intAvailableSkis = RentalShop.GetAvailableSkis()
        intAvailableSnowboards = RentalShop.GetAvailableSnowboards()
        print("Sorry, we only have ", intAvailableSkis, " skis and ", intAvailableSnowboards, " snowboards available.")
        # Give option to try another rental
        intNavigate = input("Enter 1 to try another rental.\nEnter 0 to return to Main Menu.")
        GetNavigate(intNavigate)

# ---------------------------------------------------------------
# Function to Return Rental
# ---------------------------------------------------------------

def ReturnRental():
    print("...")


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
    NavigationalSelection(intNavigate)




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
    blnShopOpen = False
    return blnShopOpen


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
intNavigate = NavigationalSelection(intNavigate)

# Depending on action selected, call appropriate function
GetNavigate(intNavigate)

                