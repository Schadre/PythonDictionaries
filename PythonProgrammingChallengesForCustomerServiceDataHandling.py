"""
Python Programming Challenges for Customer Service Data Handling

Task 1: Customer Service Ticket Tracker Demonstrate your ability to use 
nested collections and loops by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, 
issue description, and status (open/closed).

Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
"""
service_tickets = {
    "Ticket 0": {"Customer": "John", "Issue": "Login problem", "Status": "open"}
}

while True:
    try:
        print("Welcome to the service ticket system")
        service_option = input("Please select your option: \n 1. Open a new service ticket \n 2. Update the status of an existing ticket \n 3. Display all tickets \n 4. Filter by status \n 5. Exit \n")

    
        if service_option == "1":
            ticket = "Ticket " + input("Please input your ticket number: ")
            customer = input("Please input the first name of the customer: ")
            issue = input("Please briefly explain the issue: ")

            service_tickets.update({
                ticket : {
                    "Customer" : customer,
                    "Issue" : issue,
                    "Status" : "open"
                }
            })
            print(f"\nYour new ticket {ticket} has been entered\n")

        elif service_option == "2":
            print("\nALERT: Updating the ticket status will close the ticket.\n")
            update_ticket = "Ticket " + input("Which ticket would you like to update? ")
            service_tickets[update_ticket]["Status"] = "closed"
            print(f'\nThe status for {update_ticket} has been {service_tickets[update_ticket]["Status"]}\n')
        
        elif service_option == "3":
            print("\nHere are the tickets we currently have logged: \n")
            for key, value in service_tickets.items():
                print(f"\n {key} : {value}\n")
        
        elif service_option == "4":
            filter_status = input("If you would like the open status only input 'open' or if you would like the closed status only input 'closed': (open/closed) ")
            if filter_status == "open":
                for key, value in service_tickets.items():
                    if value["Status"] == "open":
                        print(f"\n{key}: {value}\n")
            elif filter_status == "closed":
                for key, value in service_tickets.items():
                    if value["Status"] == "closed":
                        print(f"\n{key}: {value}\n")
                
        elif service_option == "5":
            break
            
    except NameError:
        print("\nPlease try again\n")
    except KeyError:
        print("\nThe ticket number does not exist currently\n")
