from datetime import datetime
from RentalShop import RentalShop

class Customer():
    'Class for customers who can rent skis and snowboards'

    def __init__(self, strFirstName, strLastName, strIDNumber, strPhoneNumber, strCouponCode, strRentalPeriod):
        self._strFirstName = strFirstName
        self._strLastName = strLastName
        self._strIDNumber = strIDNumber
        self._strPhoneNumber = strPhoneNumber
        self._strCouponCode = strCouponCode
        self._intSkisRented = int(0)
        self._intSnowboardsRented = int(0)
        self._strRentalPeriod = strRentalPeriod
        self.dtmDateTimeRented = None
        self.dtmDateTimeReturned = None



    @property
    def strFirstName(self):
        return self._strFirstName

    @strFirstName.setter
    def strFirstName(self, strFirstName):
        if strFirstName == "":
            raise Exception("You must enter a first name.")
        elif type(strFirstName) != str:
            raise Exception("First Name Must be a string")
        else:
            self._strFirstName = strFirstName
            


    @property
    def strLastName(self):
        return self._strLastName

    @strLastName.setter
    def strLastName(self, strLastName):
        if strLastName == "":
            raise Exception("You must enter a Last name.")
        elif type(strLastName) != str:
            raise Exception("Last Name Must be a string")
        else:
            self._strLastName = strLastName
            


    @property
    def strIDNumber(self):
        return self._strIDNumber

    @strIDNumber.setter
    def strIDNumber(self, strIDNumber):
        if strIDNumber == "":
            raise Exception("You must enter an ID Number.")
        elif type(strIDNumber) != str:
            raise Exception("ID Number Must be a string")
        else:
            self._strIDNumber = strIDNumber
            


    @property
    def strRentalPeriod(self):
        return self._strRentalPeriod

    @strRentalPeriod.setter
    def strRentalPeriod(self, strRentalPeriod):
        if strRentalPeriod == "hourly" or strRentalPeriod == "daily" or strRentalPeriod == "weekly":
            self._strRentalPeriod = strRentalPeriod
        else:
            raise Exception("Rental period must be hourly, daily, or weekly.")
        


    @property
    def intSkisRented(self):
        return self._intSkisRented

    @intSkisRented.setter
    def intSkisRented(self, intSkisRented):
        if intSkisRented < 0:
            raise Exception("Skis rented can't be negative")
        elif type(intSkisRented) != int:
            raise Exception("Skis Rented Must be an integer")
        else:
            self._intSkisRented = intSkisRented
            


    @property
    def intSnowboardsRented(self):
        return self._intSnowboardsRented

    @intSnowboardsRented.setter
    def intSnowboardsRented(self, intSnowboardsRented):
        if intSnowboardsRented < 0:
            raise Exception("Snowboards Rented can't be negative.")
        elif type(intSnowboardsRented) != int:
            raise Exception("Snowboards Must be an integer")
        else:
            self._intSnowboardsRented = intSnowboardsRented



    # ####################################################################
    # Name: Rent Items
    # Abstract: Rents an item out to the customer. Returns a boolean
    # ####################################################################
    def RentItems(self, intSkis = 0, intSnowboards = 0):
        blnSuccessfulRental = bool(False)
        if RentalShop._intSkisAvailable >= intSkis and RentalShop._intSnowboardsAvailable >= intSnowboards:
            if intSkis > 0 or intSnowboards > 0:    
                self._intSkisRented += intSkis
                self._intSnowboardsRented += intSnowboards
                
                RentalShop._intSkisAvailable -= intSkis
                RentalShop._intSnowboardsAvailable -= intSnowboards
                
                RentalShop._intDailySkisRented += intSkis
                RentalShop._intDailySnowboardsRented += intSnowboards
                
                blnSuccessfulRental = True
            else:
                blnSuccessfulRental = False
        else:
            blnSuccessfulRental = False
            
        return blnSuccessfulRental
            


    # ####################################################################
    # Name: Return Items
    # Abstract: Returns items to the shop
    # ####################################################################
    def ReturnItems(self):
        if self._intSkisRented > 0:
            RentalShop._intSkisAvailable += self._intSkisRented
            self._intSkisRented = 0
            
        if self._intSnowboardsRented > 0:
            RentalShop._intSnowboardsAvailable += self._intSnowboardsRented
            self._intSnowboardsRented = 0
        


    # ####################################################################
    # Name: Get Skis Rented
    # Abstract: Gets the amount of skis the customer has rented
    # ####################################################################
    def GetSkisRented(self):
        return self._intSkisRented
    


    # ####################################################################
    # Name: Get Snowboards Rented
    # Abstract: Gets the amount of snowboards the customer has rented
    # ####################################################################
    def GetSnowboardsRented(self):
        return self._intSnowboardsRented
    

    
       
        


