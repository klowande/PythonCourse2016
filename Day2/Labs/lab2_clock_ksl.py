# clock lab

class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    def __str__(self):
    	return 'The clock reads %d:%02d' % (self.hour, self.minutes)
    
    def __repr__(self):
    	return 'The clock reads %d:%02d' % (self.hour, self.minutes)
    	    
	def __add__(self, minutes):
		secondhand = self.minutes + minutes
		firsthand = self.hour + secondhand//60
		if firsthand < 13:
			result_hour = firsthand
		else:
			result_hour = firsthand % 12
		if secondhand < 60:
			result_minutes = secondhand
		else:
			result_minutes = secondhand % 60			
		return 'The new time is %d:%02d' % (result_hour,result_minutes)

    def __sub__(self, minutes):
		secondhand = self.minutes - minutes
		firsthand = self.hour + secondhand//60
		if firsthand > 0:
			result_hour = firsthand 
		else:
			result_hour = firsthand % 12
		if secondhand > -1:
			result_minutes = secondhand
		else:
			result_minutes = secondhand % 60
		return 'The new time is %d:%02d' % (result_hour,result_minutes)
		
    def __eq__(self, other):
    	return self.hour==other.hour and self.minutes==other.minutes
    
    def __ne__(self, other):
    	return not self.__eq__(other)
    	
### Check ###
a = Clock(3,15)
b = Clock(3,16)
print a
a
a==b
a!=b
a + 7
a + 1000
a - 7
a - 1000



		