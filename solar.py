import math
##  Solar angle calculator class

class Solar:

    def __init__(self, lat, timezone):
        self.tz = timezone
        self.lat = math.radians(lat)

    def dateToN(self, date_val):
        #change the date to a number N that can be used for declination calcs
        return()

    def getElevation(self, curr_hour_angle, curr_date):
        #calculate the sun's elevation angle
        
        declination = 23.45 * math.sin((360/365)*(284+curr_date))
        elevation = math.asin(math.sin(declination)*math.sin(self.lat) + math.cos(declination)*math.cos(curr_hour_angle)*math.cos(self.lat))
        return(elevation)
    
    def getAzimuth(self, curr_hour_angle, curr_date):
        #calculate the sun's Azimuth angle
        curr_hour_angle = math.radians(curr_hour_angle)

        declination = math.radians(23.45 * math.degrees(math.sin(math.radians((360/365)*(284+curr_date)))))
        print(math.degrees(declination))
        elevation = math.asin(math.sin(declination)*math.sin(self.lat) + math.cos(declination)*math.cos(curr_hour_angle)*math.cos(self.lat))
        print(math.degrees(elevation))
        Azprime = math.degrees(math.acos(((math.sin(declination)*math.cos(self.lat)) - (math.cos(declination)*math.cos(curr_hour_angle)*math.sin(self.lat))) / math.cos(elevation)))
        if curr_hour_angle > 0:
            azimuth = 360 - Azprime
        else:
            azimuth = Azprime
        
        return(azimuth)
