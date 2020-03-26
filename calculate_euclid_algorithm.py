def calculate_euclid_algorithm(number1,number2): #Function for Algorithm
  if number1 == 0:
    return number2
  elif number2 == 0 :
    return number1;    
  reminder = number1%number2; #Check the Reminder
  return calculate_euclid_algorithm(number2,reminder) # Return Function value


#Taking input from Terminal 

number1 = int(input("Enter Number One= "))
number2 = int(input("Enter Number Two= "))

#Find the GCD and Print as output
gcd = calculate_euclid_algorithm(number1,number2)
print("The GCD of Two Given Number is = ",+gcd)
