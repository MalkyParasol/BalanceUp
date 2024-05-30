# BalanceUp: Income and Expense Management 
## BalanceUp is an backend designed to help users manage their incomes and expenses efficiently. It provides functionalities for users to sign up, log in, update their details, add, update, and retrieve their incomes and expenses. Additionally, users can visualize their financial data through various graphs generated with Matplotlib.

### Rable of Contents

 * [Features](#Features)

 * [Technologies Used](#TechnologiesUsed)

 * [File Tree](#filetree)

 * [Getting Started](#GettingStarted)

 * [Usage](#Usage)

## Features

**User Authentication:** Users can sign up or log in to access the application.

**Profile Management:** Users can update their personal details.

**Income and Expense Management:** Users can add, update, and retrieve their incomes and expenses.

**Data Visualization:** Users can view graphs depicting their income and expenses based on month, year, day, and expense category.

**Data Storage:** All user data, including income and expense records, is stored in a MongoDB database.

## Technologies Used

**Python:** Backend development language.

**FastAPI:** Web framework used for building APIs.

**MongoDB:** NoSQL database for storing user data.

**Matplotlib:** Library for creating static, animated, and interactive visualizations in Python.

## File tree:

![fileTree](./Backend/assets/file%20tree.png)

#### In this structure:

The **BalanceUp** folder is the root directory.

Inside BalanceUp, there's a **Backend** folder.

Inside Backend, there are three main directories:

**app:** Contains the application logic.

**db_management:** Contains modules for database management.

**config.py:** Configuration settings for the database.

**connectDB.py:** Module for connecting to the database.

**expense_CRUD.py:** Module for expense CRUD operations.

**income_CRUD.py:** Module for income CRUD operations.

**user_crud.py:** Module for user CRUD operations.

**models:** Contains the data models.

**expenseModel.py**: Model for expense data.

**incomeModel.py:** Model for income data.

**userModel.py:** Model for user data.

**routers:** Contains the API routers.

**expenseRouter.py:** Router for expense-related endpoints.

**incomeRouter.py:** Router for income-related endpoints.

**userRouter.py:** Router for user-related endpoints.

**visualRouter.py:** Router for visualization-related endpoints.

**tests:** Contains test files for the application.

**test_expenseRouter.py:** Tests for the expense router.

**test_incomeRouter.py:** Tests for the income router.

**test_userRouter.py:** Tests for the user router.

**utils:** Contains utility modules.

**logDecorator.py:** Module for logging decorators.

## Getting Started

* Clone the Repository: git clone
  ```https://github.com/MalkyParasol/BalanceUp```
  
* Set Up MongoDB: Make sure you have MongoDB installed and running. Update the MongoDB connection details in the application configuration.
  
* Run the Application: uvicorn main:app --reload

## Usage

**Sign Up:** Create a new account with your email and password.

**Log In:** Log in with your credentials to access the application.

**Update Profile:** Update your personal details if needed.

**Add Incomes and Expenses:** Add records of your incomes and expenses.

**View Graphs:** Visualize your financial data using the provided graphs.

**Manage Data:** Update or delete existing income and expense records as necessary


