# Automated-Python-Application-To-Track-Amazon-Prices




Web Scrapper (Amazon Price Tracker)

A few days ago, I had to buy the Hard disk for my computer from amazon. Its price was much higher than I can afford, so decided to wait for the sale so that I can get it at a lower price. But in the daily routine, I got so busy that even sale came and go but I could not get notified about it, especially about the product that I was willing to buy. On that day I decided to do a small web scrapper project Python so that I can get notified in my inbox when the price falls below my expected price.




Project Description 

The idea of the project is very straight forward: Input the URL of the product you want to buy. Scrap the HTML of a webpage of that product and extract useful data like product title, price, in stock, etc. If the product price falls below our expected price, it should send an email notifying that price has fallen down and now you can buy it.

To make such a beneficial task possible, we have used Python as it has all the libraries required to perform this task.

Python modules used in this project:  


request: request is a module that allows you to send the HTTP request without manually adding a query string to your URL. It is extremely easy to use. Request has one special method called request.get (url_of_your_choice) which returns the response object. eg. r = request.get(“https://www.amazon.in/dp/B00UJCZ9K0”,headers = headers), where headers can be obtained by simply searching for ‘My user agent’ in Google.

We use response.txt to make the content human-readable stored in the response object. We get all the information we needed from this object.

bs 4: bs4 stands for Beautiful Soup version 4. It is a library that makes it very easy to scrap information from web pages. It is popular for HTML and XML parsing, providing a Pythonic approach for iterating, searching, and modifying the parse tree. By using bs4, we will find the exact information about the product using find() method.

smtplib: smtplib is a module that defines an SMTP client session object which can send email to any machine with SMTP or ESMTP listener. We will use smtplib to send mail notifying the user regarding the price changes.


libraries: request, bs4, smtplib.

Programming Languages and modules: Python, request-module, bs4- module, smtplib.


