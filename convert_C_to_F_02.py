# FILE NAME - convert_C_to_F_02.py

# NAME: Caden Warren
# DATE: 9/29/25
# BRIEF DESCRIPTION:  conditional C to F converter



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########






print("===== Temperature Converter =====\n\n  1. Convert from Celsius to Fahrenheit\n  2. Convert from Fahrenheit to Celsius\n")

choice = int(input("Please choose from the above menu: "))
start = int(input("Enter a temperature to convert: "))

if choice == 1:
  temp = start * 9/5 + 32
  print(f"{start} degrees Celsius is {temp} degrees Fahrenheit.")
elif choice == 2:
  temp = (start - 32 ) * 5/9
  print(f"{start} degrees Fahrenheit is {temp} degrees Celsius.")






########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?







'''