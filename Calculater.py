el1 = 0
while el1 !="1":
 num1 = input("First number please:")
 num2 = input("Second number please:")
 op1 = input("+,-,*, or / only.Operater please:")
 num1 = int(num1)
 num2 = int(num2)
 if op1 == "+":
     result = (num1 + num2)
    
 elif op1 =="-":
     result = (num1 - num2)

 elif op1 =="/":
     div1 = 0
     while div1 != 1: 
      ask = input("Do you want a decimal or whole number? 1 for decimal,2 for whole number:")
      if ask == "1":
          
       if num2 == 0:
         result = "Error"
         
       else:
        result = (num1 / num2)
        div1 = 1
      elif ask == "2":
       result = (num1 // num2)
       div1 = 1
      else:
       print("You lose everything!")

 elif op1 == "*":
     result = (num1 * num2)

 else:
     print("You lose everything!")
    
 print(result)
 end1 = input("Wanna do more calculations? Yes or No")
 if end1 == "No":
     el1 = 1
     
     


