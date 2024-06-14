# Financial Tracker

Financial Tracker is a Django-based web application designed to help users manage their expenses and visualize their financial habits effectively. It provides tools for tracking expenses, categorizing spending.

## Features
- User Authentication and Registration: Allows users to sign up, log in, and manage their accounts securely.

- Expense Tracking: Users can add, edit, and delete expenses, categorizing them into predefined types (e.g., Clothes, Food, Transport).
- Currency Determinant: The application automatically determines the user's currency based on their location:
  - Users from the US will see balances in dollars (USD).
  - Users from Poland will see balances in zloty (PLN).

 - Profile Picture: Users can set a profile picture to personalize their accounts.

- Visualization: Provides charts and graphs to visualize spending patterns over time, helping users understand their financial habits better.
## Technologies Used
- Django: Backend framework for handling server-side logic and database interactions.

- Django REST Framework: Facilitates building RESTful APIs for communication with the frontend.

- PostgreSQL: Database management system for storing user data and expenses.

- HTML/CSS/JavaScript: Frontend technologies for rendering the user interface and interactive elements.


## Installation

Install dependencies.

```bash
pip install -r requirements.txt
```

## Usage

 - Sign Up: Create a new account to start tracking your expenses.

 - Log In: Access your account using your credentials.

- Add Expense: Log your expenses by specifying the amount, category, and description.

- View Reports: Navigate through charts and graphs to analyze your spending patterns.
