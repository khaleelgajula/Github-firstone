 #BOOK TICKET 
print("Welcome to book my show")
theatre_name=input("Enter the name of the theatre PVR,INOX:")
if theatre_name=="PVR" or theatre_name=="INOX":
    if theatre_name=="PVR":
        print("\n movies available at PVR:")
        movie1="ustaad:bagathsingh-500"
        movie2="toxic:daddyhome-450"
        ticket_price1=500
        ticket_price2=950
    else:
        print("\n movies available at INOX:")
        movie1="paradise:aayasher-500"
        movie2="peddi:Rc-500"
        ticket_price1=500
        ticket_price2=1000
    print(f"1.{movie1}")
    print(f"2.{movie2}")
    movie_choice=input("\n Enter the number to select movie (1 or 2):")
    if movie_choice=="1" or movie_choice=="2":
        if movie_choice=="1":
            selected_movie=movie1
            ticket_price=ticket_price1
        else:
            selected_movie=movie2
            ticket_price=ticket_price2
        print(f"\n you selected:{selected_movie}")
        print(f"\n ticket_price:RS{ticket_price}")
        confirmation=input("\n Do you want to confirm the booking? (yes/no):")
        if confirmation=="yes":
            print(f"\n your ticket for '{selected_movie}' has been booked successfully!")
        else:
            print("\n ticket booking has been cancelled")
    else:
        print("invalid movie choice.please try again")
else:
    print("sorry, the theatre name is not available")