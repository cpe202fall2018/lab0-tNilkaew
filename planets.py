#
# Tantum Nilkaew
# 014752396
#
# Lab 00
# CPE 202-13
# Purpose of Lab: To learn how to set up a GitHub Repository and code with basic python functions and operators.
#

def weight_on_planets():

   #write your code here
   earth = float(input('What do you weigh on earth? \n')) #cast input to float
   mars = (earth) * 0.38 #calculate mars weight
   jupiter = (earth) * 2.34 #calculate jupiter weight
   print("On Mars you would weigh", mars, "pounds.\nOn Jupiter you would weigh", jupiter, "pounds.") #print statement

   
   
if __name__ == '__main__':
   weight_on_planets()