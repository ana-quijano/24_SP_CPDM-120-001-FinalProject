from RentalShop import RentalShop
from Customer import Customer
import msvcrt


# ---------------------------------------------------------------
# Function to set up the Ski and Snowboard Shop inventory
# ---------------------------------------------------------------

def SetUp_ShopInventory(intTotalSkis, intTotalSnowboards):
    Inventory = RentalShop(intTotalSkis, intTotalSnowboards)
    print("Bob's Skis and Snowboards Shop is now open!\n")
    print("There are ", intTotalSkis, " skis and ", intTotalSnowboards, " in the inventory.")
    print("===========================================\n")

# ---------------------------------------------------------------
# Function to Display Navigational Selection
# ---------------------------------------------------------------
def NavigationalSelection(intNavigate):
    intNavigate = input("For New Customer Rental, enter 1.\n To Return Rental, enter 2.\n To Display Inventory, enter 3. \n To Close Shop at End of Day, enter 4.\n")
    intNavigate = Validate_Navigation(intNavigate)
    return intNavigate 

def NewCustomerRental(strFirstName, strLastName, strIDNumber, strPhoneNumber, strCouponCode, strRentalPeriod, intTime, intSkis, intSnowboards, dblEstimate):
    print("Enter Customer Rental Request Details Details\n")
    strFirstName = input("First Name: ")
    strLastName = input("Last Name: ")
    strIDNumber = input("ID Number: ")
    strPhoneNumber = input("Phone Number: ")
    strCouponCode = input("Coupon Code: ")
    strRentalRate = input("Rental Period (Hourly, Daily, or Weekly): ")
    if strRentalPeriod == "hourly":
        intTime = input("Rental Time, in hours: ")
    else:
        if strRentalPeriod == "daily":
            intTime = input("Rental Time, in Days: ")
        else:
            intTime = input("Rental Time, in weeks: ")
    intSkis = input("Number of Skis: ")
    intSnowboards = input("Numbber of Snowboards: ")
    dblEstimate = RentalShop.CalculateEstimate(strRentalPeriod, intSkis, intSnowboards, intTime, strCouponCode)
    print (strFirstName, strLastName, strIDNumber, strPhoneNumber, strCouponCode, strRentalPeriod, intTime, intSkis, intSnowboards)
    print ("Rental Price Estimate: ", dblEstimate)
    
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

strInitialSkisFlag = bool(False)
strInitialSnowboardsFlag = bool(False)
strNavigateFlag = bool(False)
intNavigate = int()

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

# Call function to instantiate class RentalShop
SetUp_ShopInventory(intTotalSkis, intTotalSnowboards)

# Get intNavigate to determine next action
#(1 for new customer rental, 2 for return rental, 3 for inventory display, 4 for close shop)
intNavigate = NavigationalSelection(0)

# Depending on action selected, call appropriate function
if intNavigate == 1:
    # add new customer to a list of customers
    NewCustomerRental(strFirstName = "", strLastName = "", strIDNumber = "", strPhoneNumber = "", strCouponCode = "", strRentalPeriod = "", intTime = 0, intSkis = 0, intSnowboards = 0, dblEstimate = 0)
    if intNavigate == 2:
        ReturnRental()
        if intNavigate == 3:
            DisplayInventory()
            if intNavigate == 4:
                CloseShop()
