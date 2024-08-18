# Ticket-Management-System
This Ticket Management System is a web application developed using Django. It is designed to facilitate the management and resolution of tickets, making it easier for small-sized companies to handle incidents effectively. The system supports two types of users:

- **Customer**: Creates and tracks tickets.
- **Engineer**: Resolves tickets and manages the workflow.

## Features

### User Roles

**1. Customer**:

- **Dashboard**: Provides a graphical overview of completed, pending, and active tickets. Includes a bar graph showing tickets resolved in the past 6 months.
  ![Customer Dashboard](https://github.com/user-attachments/assets/9eda56bf-583c-42f1-ab25-d1a598a19e2c)

- **Create Ticket**: Allows users to submit a new ticket with an issue title and description.
  ![Create Ticket](https://github.com/user-attachments/assets/ef0b016a-8e9d-4b29-bf49-31c81da8eac0)

- **View Tickets**: Lists all tickets created by the user.
  ![View Tickets](https://github.com/user-attachments/assets/03a8e7db-785d-423f-82d0-6bd8d6eab020)

**2. Engineer**:

- **Dashboard**: Provides a graphical overview of completed, pending, and active tickets. Includes a bar graph showing tickets resolved in the past 6 months.
  ![Engineer Dashboard](https://github.com/user-attachments/assets/d7354795-5287-4a8c-9945-e110d57eaaaa)

- **Ticket Queue**: Lists all pending tickets.
  ![Ticket Queue](https://github.com/user-attachments/assets/422c9c53-4a2c-412d-adbd-2f5080b8001a)

- **Workspace**: Shows all tickets that are active or under work.
  ![Workspace](https://github.com/user-attachments/assets/78c97cfd-5dc6-4b6e-a994-9e6d3aa80dd3)

- **Closed Tickets**: Lists all tickets that have been resolved.
  ![Closed Tickets](https://github.com/user-attachments/assets/f4811dba-3f53-4a87-bbe3-f0437e8fa3b2)


### Authentication and Registration

- **Login**: For both Customers and Engineers to access their respective pages.
  ![Login](https://github.com/user-attachments/assets/122dd559-2dd8-4322-ae1b-68658ab3bd8d)

- **Register**: Users can only register as Customers on the portal. To change roles to Engineer or create new users as Engineers, use the Admin Panel.
  ![Register](https://github.com/user-attachments/assets/23a30e42-f103-4c21-8158-340c3e2fc8ad)

