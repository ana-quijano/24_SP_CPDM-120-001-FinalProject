from datetime import datetime

class RentalShop():
    'Class for rental shops that rent out skis and snowboards'

    # inventory
    _intTotalSkis = int(0)
    _intTotalSnowboards = int(0)
    
    _intSkisAvailable = int(0)
    _intSnowboardsAvailable = int(0)
    
    # daily totals
    _dblDailyRevenue = float(0)
    
    _intDailySkisRented = int(0)
    _intDailySnowboardsRented = int(0)
    
    # ski rates
    _dblSkiHourlyRate = int(15)
    _dblSkiDailyRate = int(50)
    _dblSkiWeeklyRate = int(200)
    
    # snowboard rates
    _dblSnowboardHourlyRate = int(10)
    _dblSnowboardDailyRate = int(40)
    _dblSnowboardWeeklyRate = int(160)

    

    def __init__(self, intTotalSkis, intTotalSnowboards):
        RentalShop._intTotalSkis = intTotalSkis
        RentalShop._intTotalSnowboards = intTotalSnowboards

        RentalShop._intSkisAvailable = intTotalSkis
        RentalShop._intSnowboardsAvailable = intTotalSnowboards
        


    @property
    def intTotalSkis(self):
        return self._intTotalSkis

    @intTotalSkis.setter
    def intTotalSkis(self, intTotalSkis):
        if intTotalSkis < 0:
            raise Exception("Total skis can't be negative.")
        elif type(intTotalSkis) != int:
            raise Exception("Total skis must be an integer.")
        else:
            self._intTotalSkis = intTotalSkis



    @property
    def intTotalSnowboards(self):
        return self._intTotalSnowboards

    @intTotalSnowboards.setter
    def intTotalSnowboards(self, intTotalSnowboards):
        if intTotalSnowboards < 0:
            raise Exception("Total snowboards can't be negative.")
        elif type(intTotalSnowboards) != int:
            raise Exception("Total snowboards must be an integer.")
        else:
            self._intTotalSnowboards = intTotalSnowboards
            


    # ####################################################################
    # Name: Get Available Skis
    # Abstract: Returns the number of available skis as an integer
    # ####################################################################
    def GetAvailableSkis():
        intSkisAvailable = int(RentalShop._intSkisAvailable)
        return intSkisAvailable
    


    # ####################################################################
    # Name: Get Available Snowboards
    # Abstract: Returns the number of available snowboards as an integer
    # ####################################################################
    def GetAvailableSnowboards():
        intSnowboardsAvailable = int(RentalShop._intSnowboardsAvailable)
        return intSnowboardsAvailable
            


    # ####################################################################
    # Name: Get Daily Revenue
    # Abstract: Returns the daily revenue as a float
    # ####################################################################
    def GetDailyRevenue():
        dblRevenue = RentalShop._dblDailyRevenue
        return dblRevenue
    


    # ####################################################################
    # Name: Get Daily Skis Rented
    # Abstract: Returns the daily skis rented as an integer
    # ####################################################################
    def GetDailySkisRented():
        intSkisRented = RentalShop._intDailySkisRented
        return intSkisRented
    


    # ####################################################################
    # Name: Get Daily Items rented
    # Abstract: Returns the daily items rented as an integer
    # ####################################################################
    def GetDailySnowboardsRented():
        
        return RentalShop._intDailySnowboardsRented
        


    # ####################################################################
    # Name: Convert Date to Time Units
    # Abstract: Takes two dates and converts them to hours, days, weeks
    # returns 3 integers hours, days, weeks
    # ####################################################################
    def ConvertDateToTimeUnits(self, dtmDateTimeRented, dtmDateTimeReturned):
        intTimeUnitsRented = dtmDateTimeReturned - dtmDateTimeRented
        
        intHours = int((intTimeUnitsRented.seconds / 3600) + (intTimeUnitsRented.days * 24))
        intDays = int(0)
        intWeeks = int(0)
    
        while intHours >= 24:
            intDays += 1
            intHours -= 24
            
        while intDays >= 7:
            intWeeks += 1
            intDays -= 7
        

        if intHours > 3:
            intDays += 1
            intHours -= intHours
         
        if intDays > 4:
            intWeeks +=1
            intDays -= intDays
            intHours -= intHours


        return intHours, intDays, intWeeks



    # ####################################################################
    # Name: Calculate Estimate
    # Abstract: Calculates the estimate by taking the estimated rate, time,
    # and possible coupon code and returns a float
    # ####################################################################
    def CalculateEstimate(self, strRentalRate, intSkis, intSnowBoards, intTime, strCouponCode = ""):
        dblEstimate = float(0)

        if strRentalRate == "hourly":
            dblEstimate = self._CalculateBestPrice(intTime,0,0,intSkis,intSnowBoards, strCouponCode)
        elif strRentalRate == "daily":
            dblEstimate = self._CalculateBestPrice(0,intTime,0,intSkis,intSnowBoards, strCouponCode)
        elif strRentalRate == "weekly":
            dblEstimate = self._CalculateBestPrice(0,0,intTime,intSkis,intSnowBoards, strCouponCode)
        else:
            raise Exception("Rental period must be hourly, daily, or weekly.")  
       
        return dblEstimate



    # ####################################################################
    # Name: Calculate Bill
    # Abstract: Takes the dates, units rented, and coupon code and 
    # calculates the final bill returns a float
    # ####################################################################
    def CalculateBill(self, dtmDateTimeRented, dtmDateTimeReturned, intSkis = 0, intSnowboards = 0, strCouponCode = ""):
        intHours = int(0)
        intDays = int(0)
        intWeeks= int(0)
        
        dblTotal = float(0)

        intHours, intDays, intWeeks = self.ConvertDateToTimeUnits(dtmDateTimeRented, dtmDateTimeReturned)
        
        dblSubtotal = self._CalculateSubTotal(intHours, intDays, intWeeks, intSkis, intSnowboards)        
        dblDiscountTotal = self._CalculateFamilyDiscount(intHours, intDays, intWeeks, intSkis, intSnowboards) + self._CalculateCouponDiscount(strCouponCode, dblSubtotal)
        dblTotal = dblSubtotal - dblDiscountTotal
        
        RentalShop._dblDailyRevenue += dblTotal
            
      
        return dblSubtotal, dblDiscountTotal, dblTotal

        
    
    # ####################################################################
    # Name: Calculate Subtotal
    # Abstract: Calculates the subtotal of the rental returns a float
    # ####################################################################
    def _CalculateSubTotal(self, intHours, intDays, intWeeks, intSkis = 0, intSnowBoards = 0):
        dblSubTotal = float(0)
        
        dblSubTotal += (intSkis * intHours * RentalShop._dblSkiHourlyRate)
        dblSubTotal += (intSkis * intDays * RentalShop._dblSkiDailyRate)
        dblSubTotal += (intSkis * intWeeks * RentalShop._dblSkiWeeklyRate)
        
        dblSubTotal += (intSnowBoards * intHours * RentalShop._dblSnowboardHourlyRate)
        dblSubTotal += (intSnowBoards * intDays * RentalShop._dblSnowboardDailyRate)
        dblSubTotal += (intSnowBoards * intWeeks * RentalShop._dblSnowboardWeeklyRate)
        
        return dblSubTotal
        

    
    # ####################################################################
    # Name: Calculate Family Discount
    # Abstract: Calculates the possible Family Discount returns a float
    # ####################################################################
    def _CalculateFamilyDiscount(self, intHours = 0, intDays = 0, intWeeks = 0, intSkis = 0, intSnowboards = 0):
        dblSkiDiscount = float(0)
        dblSnowboardDiscount = float(0)
        intTotalItems = int(0)

        intTotalItemsDiscounted = int(0)
        intTotalItems = intSkis + intSnowboards

        if intTotalItems >= 3 and intTotalItems <= 5:
            dblSkiDiscount += self._CalculateSkiDiscount(intHours, intDays, intWeeks, intSkis)
            
            dblSnowboardDiscount += self._CalculateSnowboardDiscount(intHours, intDays, intWeeks, intSnowboards)
        elif intTotalItems > 5:
            while intTotalItemsDiscounted < 5:
                if intSkis > 0:
                    dblSkiDiscount += self._CalculateSkiDiscount(intHours, intDays, intWeeks)
                    
                    intSkis -= 1
                    intTotalItemsDiscounted += 1
                else:
                    dblSnowboardDiscount += self._CalculateSnowboardDiscount(intHours, intDays, intWeeks)
                    
                    intSnowboards -= 1
                    intTotalItemsDiscounted +=1
        
        dblTotalDiscount = dblSnowboardDiscount + dblSkiDiscount  
        return dblTotalDiscount



    # ####################################################################
    # Name: Calculate Ski Discount
    # Abstract: Calculates the possible Ski Discount returns a float
    # ####################################################################
    def _CalculateSkiDiscount(self, intHours, intDays, intWeeks, intSkis = 1):
        dblSkiDiscount = float(0)

        dblSkiDiscount += (intSkis * intHours * RentalShop._dblSkiHourlyRate * .25)
        dblSkiDiscount += (intSkis * intDays * RentalShop._dblSkiDailyRate * .25)
        dblSkiDiscount += (intSkis * intWeeks * RentalShop._dblSkiWeeklyRate * .25)    

        return dblSkiDiscount
    


    ######################################################################
    # Name: Calculate Snowboard Discount
    # Abstract: Calculates the possible Snowboard Discount returns a float
    # ####################################################################
    def _CalculateSnowboardDiscount(self, intHours, intDays, intWeeks, intSnowboards = 1):
        dblSnowboardDiscount = float(0)

        dblSnowboardDiscount += (intSnowboards * intHours * RentalShop._dblSnowboardHourlyRate * .25)
        dblSnowboardDiscount += (intSnowboards * intDays * RentalShop._dblSnowboardDailyRate * .25)
        dblSnowboardDiscount += (intSnowboards * intWeeks * RentalShop._dblSnowboardWeeklyRate * .25)    

        return dblSnowboardDiscount



    ######################################################################
    # Name: Calculate Coupon Discount
    # Abstract: Calculates the possible Coupon Discount if the customer 
    # provides a useable coupon code returns a float
    # ####################################################################
    def _CalculateCouponDiscount(self, strCouponCode, dblSubtotal):
        
        dblCouponDiscount = float(0)

        if len(strCouponCode) == 6:
            if strCouponCode[-3:] == "BBP":
                dblCouponDiscount = dblSubtotal * 0.10
        
        return dblCouponDiscount



    # ###################################################################
    # Name: Calculate Best Price
    # Abstract: Calculates the best price based on the best rate and 
    # applicable discounts returns a float
    # ###################################################################
    def _CalculateBestPrice(self, intHours = 0, intDays = 0, intWeeks = 0, intSkis = 0, intSnowboards = 0, strCouponCode = ""):
        dblSubtotal = float(0)
        dblDiscountTotal = float(0)
        dblBestPriceTotal = float(0)
        
        if intHours > 3:
            intDays += 1
            intHours -= intHours
         
        if intDays > 4:
            intWeeks +=1
            intDays -= intDays
            intHours -= intHours


        dblSubtotal = self._CalculateSubTotal(intHours, intDays, intWeeks, intSkis, intSnowboards)        
        dblDiscountTotal = self._CalculateFamilyDiscount(intHours, intDays, intWeeks, intSkis, intSnowboards) + self._CalculateCouponDiscount(strCouponCode, dblSubtotal)
        dblBestPriceTotal = dblSubtotal - dblDiscountTotal
        
        return dblBestPriceTotal




