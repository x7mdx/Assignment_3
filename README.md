# Race Ticketing System

## UML
![UML](https://raw.githubusercontent.com/x7mdx/Assignment_3/refs/heads/main/UML.png)


## Classes
1. User 
2. Customer (inherits User)
3. Admin (inherits User)
4. Ticket
5. PurchaseOrder
6. RaceEvent
7. Payment
8. Discount
---
##  Assumptions
- A User can be either a Customer or an Admin.
- Each Customer can make multiple PurchaseOrders.
- Each PurchaseOrder may include one or more Tickets.
- Each Ticket is associated with a RaceEvent.
- Payment is linked to a PurchaseOrder.
- Admin can view and modify discounts, and track ticket sales.
- All object data is saved using pickle (assumed one file for each class type: e.g., users.pkl, orders.pkl, etc.)


## Testing - Screenshots
1. Login
   
   ![image](https://github.com/user-attachments/assets/219b75cc-4a26-41e5-968f-e02b25bc94a9)
2. CustomerDashboard
   
   ![image](https://github.com/user-attachments/assets/b1eaa66e-5685-4d1e-97a4-ca5dbaab294e)
3. View/Edit Profile
   
   ![image](https://github.com/user-attachments/assets/2d958b79-e38a-4f9b-aeac-4b671f3f880e)'
   ![image](https://github.com/user-attachments/assets/c993abc4-9e1f-4ea0-a171-75146df55306)

4. Phurchase Ticket
   
  ![image](https://github.com/user-attachments/assets/1584fb14-d3f1-40d0-b27b-ff4d177fb2ee)![image](https://github.com/user-attachments/assets/d3c4f669-1010-4fee-b94b-0ee1e6c27bae)

5. View Orders
   
   ![image](https://github.com/user-attachments/assets/188837e0-9b5e-4d5a-820d-05ddcaf52068)
6. Modify Order

   ![image](https://github.com/user-attachments/assets/2c5e81d7-4fd4-464d-be50-b06b2938cc05)

7. Delete Order

   ![image](https://github.com/user-attachments/assets/6d73abac-782f-4c3c-9691-a72bf660e906)

8. Signup
   
   ![image](https://github.com/user-attachments/assets/4f928e1c-b95f-4424-ba35-440102dc6bc6)


9. Admin Login

    ![image](https://github.com/user-attachments/assets/b7c7d7fa-ff7e-47ad-a531-272b96a4cd54)

10. Admin DashBoard

![image](https://github.com/user-attachments/assets/07e1b112-e5f5-4a40-ae51-3aac5b6ec0e0)

11. Total Ticket Sales

    ![image](https://github.com/user-attachments/assets/8ed9b484-469a-4331-a8df-e3f8b5707d4f)

13. Manage Discounts

    ![image](https://github.com/user-attachments/assets/f1c0c7f1-2daa-43d0-9957-bd7856d7e652)


   
## Limitations of System

1. Modifying an order will remove the discount
2. No Varification of Email
3. Email can't be changed.




## SAVED CUSTOMERS IN Binary File
1. Email: something@gmail.com, Password: something
2. Email: something2@gmail.com, Password: something2

## ADMIN Credentials
1. Email: admin@raceTicket.sys, Password: UAE@123@


