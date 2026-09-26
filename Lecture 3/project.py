#Intelligent customer churn monitoring system
customers = [
    {
       "customer id" : "k001",
       "Name" : 'Ali',
       "age": 28,
       "monthly bill": 8600,
        "support tickets":6,
        "month with company":4,
        "contract": " monthly"   
           
    },

    {
       "customer id" : "k002",
       "Name" : 'Ali khan',
       "age": 28,
        "monthly bill":9000,
        "support tickets":8,
        "month with company":4,
        "contract": " monthly"   
            
     },
 

    {
       "customer id" : "k003",
       "Name" : 'Sara',
       "age": 28,
        "monthly bill":15000,
        "support tickets":9,
        "month with company":7,
        "contract": " monthly"   
           
   },
 

    {
       "customer id" : "k004",
       "Name" : 'Ahmad',
       "age": 28,
        "monthly bill":25000,
        "support tickets":8,
        "month with company":7,
        "contract": "monthly"   
           
     }
] 
while True:
    print("--------------------================")
    print("Customer churn monitoring system ")
    print("------------------------------------")
    print("1 : view customer")
    print("2 :analyze customer")
    print("3 : Exit")
    choice =input("enter your choice : ")
    if choice == '1':
       print("customer list")
       for customer in customers:
         print(  
           ["id"],"|",
           customer["Name"],
       "age",customer['age'],
       "| Bill:", customer["monthly bill"],
    "| Tenure:", customer["month with company"],
    "month",
    "| Tickets:", customer["support tickets"],
    "| contract:", customer["contract"]

         )
    elif choice =='2':
       print("customer risk analysis")
       for customer in customers:
          score = 0
          if customer['support tickets'] <= 5:
             score +=2
             if customer['contract'] == 'monthly':
              score +=2
             if customer['monthly bill'] >= 18999:
                score +=2
                if customer['month with company'] == 10:
                   score +=2
                   # RISK CALCULATION
                   if score >= 4:
                      risk = 'HIGH'
                   elif score == 2:
                      risk = 'MEDIUM'
                   else:
                      risk = 'LOW'
                      # customer infomationm
                      print(
                          customer["id"],
    "|",
    customer["name"],
    "| Score:", score,
    "| Risk:", risk
                      )
  


    elif choice == "3":

        print("Program closed.")
        break
    
    else:

        print("Invalid choice. Please try again.")
        continue