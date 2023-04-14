class DataHandling:
    conn = squlite3.connect("expenses.db")
    cur = conn.cursor()

while True: 
    print("Select an option: ")
    print("Enter a new expense")
    print("2. View expenses summary")

    choice = int(input())

    if choice == 1:
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        description = input("Enter the description of the expense: ")

         cur.execute ("Select Distinct category FROM expenses")
         
         print("Select a category by number:")
         for idx, category in enumerate(categories):
            print(f"{idx + 1}. {category[0]}")
         print(f"{len(categories) + 1}. Create a new category") 
        
        category_choice = int(input())
        if category_choice == len(categories) + 1:
            category = input("Enter the new category name: ")
        else:
            category = categories[category_choice - 1][0]
        price = input("Enter the price of the expense: ")
        cur.execute("INSERT into expenses (Date, description, category, price) Values (?, ?, ?, ?,)", (date,description,_category, price)) 

        conn.commit()

         
        

            categories = cur.fetchall()
        
        
        

     
    elif choice == 2:
        pass
    else:
        exit()




