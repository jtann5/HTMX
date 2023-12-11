# HTMX Website (Group 39)

Group Members: Mike Kadoshnikov and Jacob Tanner


## Links

Mike Kadoshnikov: http://csci331.cs.montana.edu:3061/

Jacob Tanner: http://csci331.cs.montana.edu:3070


Presentation: https://github.com/jtann5/HTMX/blob/main/Presentation/HTMX.pptx

## Running Instructions
**Make sure that you have these python packages installed on your computer using these commands!**
```
pip install Flask
pip install flask_sqlalchemy
pip install pandas
```



**Server will run on port 3061 on localhost, make sure no other services are using that port!**

**If you are unable to use port 3061 use the following code to change the port number to one that suites you!**




```app.run(debug=True, host="localhost", port=3061)```


In order to run the server to get the Interplanetary Technologies website in the terminal type:


```python app.py```


or in an IDE like VSCode open the project go to the app.py file and click run!

Then to reach the website go to http://localhost:3061/

## Features
Tabs - Used to changed page content without refreshing URL.

Confirm Button - Can be used for extra function on back end using HTMX.

Store - Uses HTMX to return products, as well as using HTMX for the Search.

Product Page - Uses a template returned by HTMX and populated with an SQL query and flask.

Product Not Found - Uses HTMX to return content.

# Objectives

Our objective was to leverage HTMX to design and implement a custom web application, featuring tab functionalities and utilizing HTMX features such as hx-confirmation, hx-get, and hx-target. Our goal was to create a functional website, demonstrating the versatility and effectiveness of HTMX in enhancing user interactions within web applications. We also demonstrated that you can make a Full-Stack web app with a minimal use of JavaScript, with only a couple functions on the front-end.

# Tech Summary

The project uses Flask, a python library, and HTMX, a Javascript Library. Flask is a web-application library that allows individuals to created a web application using Python.  Flask allows users to specify get requests and does the work to retrieve, access, and control the website. HTMX is a Hyper Media focused JavaScript library that allows individuals to create RESTFUL web applications that allow the HTML to shine. HTMX works by allowing the user to send various requests to the backend web server such as hx-get, hx-trigger, etc.

# Individual member notes
## Mike Kadoshnikov
MIKE WORDS!!!

## Jacob Tanner


# Conclusion

HTMX allows individuals to create a Full-Stack Web Application with a minimal use of Javascript, allowing for a HyperMedia focused site, as well as a backend of your choosing. The use of individual pages on the topnav was the best initiaitive (described below). The templates for various reused items worked really well and reduced redundancy. Within the project we needed access to store items, initially each page was using the HTMX Tab ability, but we found that it made retrieving individual items rather complicated and would present challenges if a user would ever want to share a product or if you refreshed the page as it would default to the home page. We would opt to restructure the CSS, as it was rather disorganized with the templates. Fetching the Footer and Header was an amazing attribute of HTMX that we would absolutely use again.

# References

YouTube. (2023). YouTube. Retrieved December 11, 2023, from https://www.youtube.com/watch?v=PWEl1ysbPAY&amp;t=111s. 

HTMX - high power tools for HTML. htmx - high power tools for html. (n.d.). https://htmx.org/ 

**NOTE: ChatGPT was used to get started with Flask, as well as helping with SQL Statements for Flask sqlalchemy. As we were unfamiliar with the Framework!**

Chatgpt. ChatGPT. (n.d.). https://openai.com/chatgpt 

