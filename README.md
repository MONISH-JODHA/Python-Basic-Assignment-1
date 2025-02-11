Python Basic Assignment

Q1. Write a Python program to perform the following: 
Validate a given public IP address to check if it follows the correct format (IPv4).
Validate a given email address to check if it’s a valid Gmail address, considering:
It should contain "@gmail.com".
The username before "@gmail.com" should contain only lowercase letters , numbers and permitted symbols.
Provide informative error messages for invalid IP or email.

Q2. Write a Python program that generates a password with the following conditions:
At least one uppercase letter.
At least one lowercase letter.
At least two numbers.
At least one special character (e.g., !@#$%&*).
The password should be exactly 16 characters long.
The password should contain no repeating characters.
The password should have a random order each time.
(Do above both problems with Regex and Without Regex)

Q3. Uptime Monitoring and Alert System

Write a Python script that checks the uptime of provided URLs and notifies the user if any of the URLs return 4xx or 5xx HTTP status codes (indicating client or server errors). For demonstration purposes, you can use the following URLs as inputs:
4xx (Client Error):
http://www.example.com/nonexistentpage or
http://httpstat.us/404
5xx (Server Error):
http://httpstat.us/500
200 (Successful Response):
https://www.google.com/
Requirements:
URL Check: The script should check the provided URLs and get their HTTP status codes.
Handle Multiple URLs: The script should be able to handle multiple URLs at once, checking each one.
Error Detection: If the status code of any URL is either 4xx or 5xx, the program should:
Notify the user via a print message.
Alternatively, you can implement more advanced logging methods, (log in any log file).
Loop and Monitor: You should set up a simple loop that continuously monitors the URLs for a certain interval (e.g., every 10 seconds) to simulate a basic uptime monitoring system.
Status Message: For each URL, the script should output the URL and its current HTTP status code (e.g., 200 OK, 404 Not Found).

Bonus (Optional):
Implement an exponential backoff in case of multiple consecutive errors (e.g., retry after increasing intervals).
Add logging functionality to save the status check results to a log file.
Example Expected Output (if status codes are returned):
Checking URL: http://www.example.com/nonexistentpage
Status Code: 404 Not Found
ALERT: 4xx error encountered for URL: http://www.example.com/nonexistentpage

Checking URL: http://httpstat.us/500
Status Code: 500 Internal Server Error
ALERT: 5xx error encountered for URL: http://httpstat.us/500

Checking URL: https://www.google.com/
Status Code: 200 OK
The website is UP and running.


Q4. Automating Software Package Updates
Write a Python program to automate the checking and updating of installed software packages on a Linux server. The script should:
Function to check for available updates using the system’s package manager (e.g., apt, yum). and list all available updates.
Ask user to Update all at once or provide any specific package name to update (take package index number for ease)
Install the available updates based on user input.
If any updates fail to install, log the error and send an alert (e.g., console log).
Optionally, schedule the script to run at a certain cron.

Q5. Duplicate File Finder and Cleaner
Write a Python script to find duplicate files within a specified directory and its subdirectories. The script should:
Scan the directory for all files and calculate a checksum (e.g., sha256sum) for each file.
Identify and list duplicate files by comparing their checksums.
Optionally, give the user the option to delete or move duplicate files.
Bonus:
Allow the user to specify the minimum file size for duplication detection (e.g., only consider files larger than 1MB).
Create a report listing the duplicate files and their checksums.

Q6. CSV to Table Visualizer
Write a Python script which reads a csv file and Visualizes a table with proper indentations and borders. (make sure to don’t use any table making module or package)	
Example : CSV file like this
Name,Age,Department
Alice,30,HR
Bob,25,Engineering
Charlie,35,Marketing
Diana,28,Sales
Output:



Q7. EC2 Recommendation
Python script that provides EC2 instance recommendations based on a given instance's type, size, and CPU utilization. The script will help in recommending appropriate EC2 instances for optimizing performance and costs based on the utilization metrics.
Input:
Current EC2 Instance: A string representing the instance type and size (e.g., t2.nano, t3.medium).
CPU Utilization: A percentage value representing the current CPU utilization (e.g., 40%).

The output will be a recommendation for a new EC2 instance based on the following logic:

Underutilized: If the CPU utilization is less than 20%, recommend a smaller instance.
Optimized: If the CPU utilization is between 20% and 80%, recommend the same instance size but suggest the latest generation instance type.
Overutilized: If the CPU utilization is greater than 80%, recommend a larger instance.
 
Instance Size Comparison: The EC2 instance sizes follow a specific hierarchy:

nano > micro > small > medium > large > xlarge > 2xlarge > 4xlarge > 8xlarge > 16xlarge > 32xlarge..

If the CPU is underutilized (CPU < 20%), the script should recommend a smaller instance by one step.
If the CPU is overutilized (CPU > 80%), the script should recommend a larger instance by one step.
If the instance size is the smallest (nano), it cannot be reduced further, so no smaller size is recommended.
If the instance is the largest (32xlarge), it cannot be upgraded further.

Input 1: 
Current EC2 : t2.large
CPU : 20%

Output 1:
Table showing columns and its value (use Que 6 function to make table with following columns)
Columns are : serial no., current ec2, current CPU, status, recommended ec2


Q8. File Restructuring and JSON Formating
You are given a large dataset in JSON format representing an e-commerce platform's order history, which includes orders from multiple customers. Each order has multiple items, with detailed attributes such as price, quantity, and shipping cost. Additionally, you need to extract specific information, perform calculations like the total cost, apply discounts, and sort the data based on various criteria like the total amount spent by each customer.
The goal is to:
Extract and restructure the data into a tabular format.
Perform calculations such as:
Total order value (price * quantity).
Apply a discount based on the total value of an order (e.g., 10% discount if the order exceeds $100).
Calculate shipping cost based on the number of items ordered (e.g., $5 per item).
Sort the data by the total amount spent by each customer.
Format the output so that it can be easily saved into a CSV file.

So Write a Python program that:
Extract and restructure the data to create a flat list of each product purchased by each customer, containing:
Order ID
Customer Name
Product Name
Product Price
Quantity Purchased
Total Value (price * quantity)
Discount (10% if the total order value > $100)
Shipping Cost (based on the number of items ordered)
Final Total (after discount + shipping)
Shipping Address
Country Code
Calculate:
For each order, apply a 10% discount to the total value if the total order value is over $100.
Calculate the total shipping cost (e.g., $5 per item).
Compute the final total by adding the shipping cost and applying the discount (if any).
Sort the list of orders by the final total amount spent by each customer.
Output the data in CSV format with the following columns:
Order ID, Customer Name, Product Name, Product Price, Quantity Purchased, Total Value, Discount, Shipping Cost, Final Total, Shipping Address, Country Code
Constraints:
The JSON file can contain a variable number of orders.
Each order contains a variable number of items.
Handle missing fields or unexpected values gracefully.
Copy this given JSON and save it as a sales.json file and take it as an input (read file)
{'orders': [{'order_id': 'O001', 'customer': {'id': 'C001', 'name': 'John Doe', 'email': 'john@example.com'}, 'items': [{'product_id': 'P001', 'name': 'Laptop', 'price': 999.99, 'quantity': 1}, {'product_id': 'P002', 'name': 'Mouse', 'price': 25.99, 'quantity': 2}], 'shipping_address': '123 Main St, Springfield, IL'}, {'order_id': 'O002', 'customer': {'id': 'C002', 'name': 'Jane Smith', 'email': 'jane@example.com'}, 'items': [{'product_id': 'P003', 'name': 'Phone', 'price': 599.99, 'quantity': 1}], 'shipping_address': '456 Oak St, Seattle, WA'}, {'order_id': 'O003', 'customer': {'id': 'C001', 'name': 'John Doe', 'email': 'john@example.com'}, 'items': [{'product_id': 'P004', 'name': 'Headphones', 'price': 149.99, 'quantity': 1}, {'product_id': 'P005', 'name': 'Keyboard', 'price': 99.99, 'quantity': 1}], 'shipping_address': '123 Main St, Springfield, IL'}]}

Q9. File Version Control System
Write a Python program to simulate a basic version control system for a directory of files. The script should:
Accept a directory path as input and store versions of files whenever changes are made.
Each time a file is modified, the script should create a new version and save it in a separate folder (e.g., ./versions).
Keep track of file versions by naming them with a version number or timestamp (e.g., file_v1.txt, file_v2.txt).
When a file is restored to a previous version, it should be copied from the version folder back to the original directory.
Bonus:
Implement the ability to compare file versions and show differences (similar to diff).
Add an option to automatically clean up old versions, keeping only the last n versions of each file.


Q10. Tuple Item Update
You have to modify a tuple item without converting it into a list. Provide an example of any case where this exactly can happen. 

