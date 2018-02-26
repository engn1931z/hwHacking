# Homework Hacking Template Code
#
# This initial helper code will 
#
# Your goal is to:
#  - Find all the supported Mode 01 PIDs and store them as a list of strings.
#  - Query the ambient air temperature and return the value in degress Celcius.
#  - Query the control module voltage and return the value in Volts for each responding ECU.
# 
# When you have a final answer, you can submit your assignment to the autograde by running the submit.py script 

initialURL='https://script.google.com/macros/s/AKfycbw24E3r_y1Gq3IpFWUZtfx3chNr1uYgz8kKp6DgHx_4dOoKXlM/exec?'

email= "YOUR_EMAIL_GOES_HERE@brown.edu" #REPLACE THIS

##################################################################
### YOUR CODE TO FIND THE SUPPORTED PIDS AND QUERY THE VALUES
##################################################################

# import anything you might need here

supportedPIDs=[]; #REPLACE THIS BY A LIST OF STRINGS

ambientAirTemperature=0.0; #REPLACE THIS BY THE TEMPERATURE IN DEGREE CELCIUS AS A FLOAT

controlModuleVoltage=[0.0]; #REPLACE THIS BY A LIST OF FLOAT

##################################################################
### DO NOT CHANGE THE FOLLOWING - Used in submission process
##################################################################
def yourSubmission():
	return {'email':email,'hw':'Hacking','supportedPIDs':json.dumps(supportedPIDs),'ambientAirTemperature':ambientAirTemperature,'controlModuleVoltage':json.dumps(controlModuleVoltage)}