/*1.List all employees with their first name, last name and title.*/
SELECT FirstName, LastName, Title
FROM employees;

/*2.List all employees from Seattle.*/
SELECT FirstName, LastName, Title
FROM Employees
WHERE City='Seattle';

/*3.List all employees from London.*/
SELECT FirstName, LastName, Title
FROM Employees
WHERE City='London';

/*4.List all employees that work in the Sales department.*/
SELECT FirstName, LastName, Title
FROM employees
WHERE Title LIKE "%Sales%";

/*5.List all females employees that work in the Sales department.*/
SELECT FirstName, LastName, Title
FROM employees
WHERE TitleOfCourtesy="Ms." OR TitleOfCourtesy="Mrs." AND Title LIKE "%Sales%";

/*6.List the 5 oldest employees.*/
SELECT *
FROM employees
ORDER BY BirthDate  
LIMIT 5;

/*7.List the first 5 hires of the company.*/
SELECT *
FROM employees
ORDER BY HireDate
LIMIT 5;

/*8.List the employee who reports to no one (the boss).*/
SELECT *
FROM employees
WHERE ReportsTo IS NULL;

/*9.List all employees by their first and last name, and the first and last name of the employees that they report to.*/
SELECT employees.FirstName || " " || employees.LastName AS Employee, 
reportsto.FirstName || " " || reportsto.LastName AS ReportsTo, employees.ReportsTo AS ReportsToID 
FROM employees LEFT JOIN employees AS reportsto
ON employees.ReportsTo = reportsto.EmployeeID;


/*10.Count all female employees.*/
SELECT COUNT(*)
FROM employees
WHERE TitleOfCourtesy IN ("Ms.", "Mrs.");

/*11.Count all male employees.*/
SELECT COUNT(*)
FROM employees
WHERE TitleOfCourtesy IN ("Dr.", "Mr.");

/*12.Count how many employees are there from the different cities. For example, there are 4 employees from London.*/
SELECT City, COUNT(City)
FROM employees
GROUP BY City;

/*13.List all OrderIDs and the employees (by first and last name) that have created them.*/
SELECT FirstName, LastName, OrderID
FROM employees
INNER JOIN orders
ON employees.EmployeeID=orders.EmployeeID;

/*14.List all OrderIDs and the shipper name that the order is going to be shipped via.*/
SELECT orders.OrderID, shippers.CompanyName
FROM orders JOIN shippers
ON orders.ShipVia = shippers.ShipperID;

/*15.List all contries and the total number of orders that are going to be shipped there.*/
SELECT  orders.ShipCountry, COUNT(orders.ShipCountry) AS NumberOfOrders
FROM orders
GROUP BY ShipCountry;

/*16.Find the employee that has served the most orders.*/
SELECT employees.FirstName, employees.LastName, COUNT(orders.OrderID)
FROM employees 
INNER JOIN orders
ON employees.EmployeeID=orders.EmployeeID
GROUP BY employees.FirstName, employees.LastName
ORDER BY COUNT(orders.OrderID) DESC 
LIMIT 1;

/*17.Find the customer that has placed the most orders.*/
SELECT customers.CustomerID, customers.ContactName, COUNT(orders.OrderID)
FROM orders
INNER JOIN customers
ON orders.CustomerID=customers.CustomerID
GROUP BY customers.CustomerID
ORDER BY COUNT(orders.OrderID) DESC
LIMIT 1;

/*18.List all orders, with the employee serving them and the customer, that has placed them.*/
SELECT (employees.FirstName || "  " || employees.LastName) AS EmployeeName, orders.CustomerID, orders.OrderID
FROM employees
INNER JOIN orders
ON employees.EmployeeID=orders.EmployeeID;

/*19.List for which customer, which shipper is going to deliver the order.*/
SELECT shippers.CompanyName AS ShipperCompanyName, customers.CompanyName AS CustomerCompanyName
FROM shippers
JOIN customers ON customers.CustomerID IN (
	SELECT orders.CustomerID
	FROM orders
	WHERE orders.shipVia=shippers.ShipperID);



