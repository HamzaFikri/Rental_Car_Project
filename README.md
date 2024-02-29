# Project: Build your portfolio project

# Rental Car Project

## Description
    
The project aims to develop a robust web application for a car rental service using Django, Python's powerful web framework. This solution utilizes Bootstrap for an elegant and responsive front-end design and SQLite3 as the database management system for efficient data handling.

This project is a rental car management system built using Django, a high-level Python web framework. It facilitates the rental process by allowing users to browse available vehicles, make bookings, and manage bookings and vehicle inventory.

## Features
- **User Authentication**: Secure login and registration system for both customers and administrators.
- **Vehicle Management**: Add, edit, and remove vehicles from the inventory.
- **Booking Management**: Allow customers to book vehicles for specific dates and times.
- **Transaction History**: Keep track of rental transactions for accounting purposes.
- **Customer Management**: Maintain customer records and contact information.
- **Admin Dashboard**: Provide administrators with a centralized dashboard to manage all aspects of the rental system.

## Technologies Used
- **Framework**: Django
- **Database**: SQLite 
- **Authentication**: Django's built-in authentication system
- **Frontend**: HTML, CSS, JavaScript (with Django templating)
- **UI Framework**: Bootstrap

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/HamzaFikri/Rental_Car_Project.git
   ```
2. Navigate to the project directory:
   ```
   cd rental-car-project
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Apply database migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser (administrator account):
   ```
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Access the application through a web browser at `http://localhost:8000`.
- Customers can sign up, log in, browse available vehicles, and make bookings.
- Administrators can log in, manage vehicle inventory, view bookings, and access transaction history.

## Contributors
- [Mohammed Hamza Fikri](https://github.com/HamzaFikri)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

![Screenshot 2023-12-17 143955](https://github.com/HamzaFikri/Rental_Car_Project/assets/103943413/2842fbb8-4845-41f5-b98c-e24be195d724)

![Screenshot 2023-12-17 143822](https://github.com/HamzaFikri/Rental_Car_Project/assets/103943413/15679f77-32bf-47f5-a7d5-d9f6a7953cdd)

Technologies Used
Django: Utilized as the primary web framework for rapid development and structured implementation.

Python: Backend logic and functionalities are developed using Python for robustness and flexibility.

Bootstrap: Front-end design and user interface enhancement for a responsive and visually appealing layout.

SQLite3: Employed as the relational database system for efficient data management.

Workflow and Implementation
Database Design: Utilize SQLite3 to design the database schema, including tables for cars, users, and bookings.

Backend Development: Implement logic for user authentication, car listings, booking handling, and admin functionalities using Django and Python.

Frontend Integration: Employ Bootstrap for creating a sleek and user-friendly interface to interact with the backend functionalities.

Testing & Deployment: Thoroughly test the application's functionalities and deploy it on a server for public access.

![Screenshot 2023-12-17 143839](https://github.com/HamzaFikri/Rental_Car_Project/assets/103943413/fe171838-e939-4a63-9e2c-e11b3608aa42)

Conclusion
This project demonstrates the seamless integration of Django, Python, Bootstrap, and SQLite3 to create an efficient and user-friendly car rental service. By leveraging these technologies, we ensure a reliable and scalable solution for both customers and administrators, enhancing the overall car rental experience.



![Screenshot 2023-12-24 161830](https://github.com/HamzaFikri/Rental_Car_Project/assets/103943413/bb43af7d-64d7-44fb-9e0d-0eebd90dddda)
