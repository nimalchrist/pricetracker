# PriceTracker Documentation

Welcome to the documentation for PriceTracker, a web application developed using React for the front end, Flask (Python) for the back end, BeautifulSoup for web scraping, and MySQL for the database. PriceTracker allows users to track prices of products and create wishlists.

## Team Member
- Mary Fency J - Flask Developer and UI Designer

## Installation and Setup

Before running PriceTracker, you need to set up React, Flask, BeautifulSoup, and MySQL on your machine.

### React

To install React:

1. Ensure that you have Node.js installed on your system.

2. Open your terminal and run the following command to install React globally:
   ```
   npm install -g create-react-app
   ```

### Flask and BeautifulSoup

To install Flask and BeautifulSoup:

1. Ensure that you have Python installed on your system.

2. Create a new virtual environment:
   ```
   python3 -m venv pricetracker-env
   ```

3. Activate the virtual environment:
   - For macOS/Linux:
     ```
     source pricetracker-env/bin/activate
     ```
   - For Windows (PowerShell):
     ```
     .\pricetracker-env\Scripts\Activate.ps1
     ```

4. Install Flask and BeautifulSoup:
   ```
   pip install flask beautifulsoup4
   ```

### MySQL

To install MySQL:

1. Visit the [MySQL website](https://www.mysql.com/) and download the appropriate version for your operating system.

2. Run the installer and follow the instructions.

3. Set up a MySQL user and password for your development environment.

## Project Structure

The PriceTracker repository consists of two main folders:

1. `pricetracker/` - Contains the React project for the front end of the application.
2. `backend/` - Contains the Flask application for the back end of the application.

The structure of each folder is as follows:

### Frontend (React)

- `src/` - Contains the main JavaScript code for the React app.
- `public/` - Holds static assets such as images, fonts, and the main HTML file.

### Backend (Flask)

- `app.py` - The main Flask application file.
- `scraper.py` - Contains web scraping logic using BeautifulSoup.

## Database Table Design

PriceTracker utilizes a MySQL database with the following table design:

1. `users` - Stores user details, including username, password, and other relevant information.
2. `wishlist` - Manages the wishlist items of users, including the product name, URL, price, and associated user ID.
