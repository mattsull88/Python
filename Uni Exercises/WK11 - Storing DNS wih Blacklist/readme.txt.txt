Problem: The government now requires that DNSs should maintain a secret blacklist of IPAs that must not be returned, even if the domain name exists.
Without changing your DNS class from problem 1, define a new class that extends your old class, adding:
•	a method for adding an IPA to the secret blacklist; and
•	a private attribute for the blacklist. Hint: it may be called a blacklist, but is a Python list the most efficient data structure to use here?
You must also override the lookup method so that it returns None for blacklisted IPA, even if they do exist.
Write a test program that allows the user to test the new class. An example of the output from the test program is like this:
? u www.google.com 8.8.8.8
? u www.amazon.com 2.2.2.2
? b 2.2.2.2
? l www.google.com
8.8.8.8
? l www.amazon.com
None
? q
where:
•	u DNS IPA updates the DNS with a new domain name and its IPA; 
•	b IPA adds the IPA to the secret blacklist;
•	l DNS returns the IPA for a domain name, or None if it does not exist or is in the secret blacklist;
•	q ends the test program.
Bad inputs are to be reported and ignored.
