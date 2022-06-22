2.1	Class design
Case study: A Go Card account maintains a balance that may be spent on public transport. Users may request a statement that shows all transactions. The only transactions are to top up the account with some positive number of dollars, and to take a ride costing some dollars and cents.
The goal for this exercise is to develop a class for a Go Card Account. The class will be tested by a program that simulates transactions, like this:
Creating account. Input initial balance: 100
? r 3.50
? r 10.90
? b
Balance = $85.60
? t 20
? x gghhg
Bad command.
? t
Bad command.
? q
Statement:
event			amount ($) 	balance ($) 
Initial balance				       100.00
Ride	3.50	     96.50
Ride	10.90	     85.60
Top up	20.00	     105.60
Final balance	     105.60
where:
•	r number simulates a ride costing number dollars; 
•	t number simulates a top up of number dollars; 
•	b requests the current balance; and 
•	q ends input and prints a statement.
Bad inputs are to be reported and ignored.

Let us consider the design for a class that represents a Go Card account. To design a class, we consider what services the object(s) must provide (its methods), and what data needs to be stored in the object(s) to support those services. Questions:
•	What is a good name for a class that represents a Go Card account?
o	Be descriptive of what the class represents. Don’t include the word “class” in the name.
•	What services should be provided?
o	A constructor (__init__) is required to set up the account with an initial balance.
o	It needs to record the amount each ride costs. A method that accepts the amount as a parameter is required.
o	It needs to record the amount for each top-up. A method that accepts the amount as a parameter is required.
o	It needs to be able to report the current balance at any time. A method that returns this is required.
o	A method is required print out a statement of all of the transactions.
We can see from the output of the proposed program that the class needs to store the details of every transaction in order.
•	What data is required to be stored in the object to enable those services?
o	So that a method can return the current balance at any time, it would be useful have a field for the current balance.
o	So that the full statement can be printed, the object must store the amount of each transaction, in order. What data type can grow and keep multiple values in the order they are added?
2.2	Problem 1 
Problem: Implement the program described above, leaving out the printing of a full statement at the end.
Answer: Submit your code as problem1.py and insert a screenshot of your program output for the following scenario:
Creating account. Input initial balance: 200
? r 2.35
? r 1.30 
? b
? r 9.45
? t 10
? q
