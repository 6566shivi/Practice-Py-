print("Welcome to Kon Banega Crrorepati ")

questionBank=[ {"question":"WHO IS FATHER OF NATION?",
                "option": ["A. Sharukh Khan", "B. Nathu RAM Godse",
                           "C. Michael Jackson","D. Mahatma Gandhi"],
                "answer":"D"
                  },
               {"question":"Full form of GK?",
                "option": ["A. General Khan", "B. Gabaar Kishor",
                           "C. General Knowledge","D. Goa kolkata"],
                "answer":"C"
                  }
                   
                 ]
myamount=0
# logic part
totalAmount=0
for i,q in enumerate(questionBank):

  print(f"The {i+1 } Question for Rs {myamount[i] } is  { q['question'] } ")
 
  for option in  q["option"]:
    print(option)

  user_input = input("Enter option A / B / C / D , Quit => Press Q")
  if(user_input == q["answer"] ):
    totalAmount += myamount[i]
    print(f"Aap Jeet chuke hai {totalAmount}")

  elif(user_input == "Q"):
    print(f"Mubarak ho bhaisahab, aap kyaa karenge itni {totalAmount} rashi ka")
    break
  else:
    print("Game over! aapka khel khatam hota hai yha")
    break