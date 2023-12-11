# HTMX Website (Group 39)

Group Members:

Mike Kadoshnikov

Jacob Tanner


Links:

Mike Kadoshnikov: http://csci331.cs.montana.edu:3061/


Presentation: https://github.com/jtann5/HTMX/blob/main/Presentation/HTMX.pptx

# Running Instructions
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

# Objectives

Our objective was to leverage HTMX to design and implement a custom web application, featuring tab functionalities and utilizing HTMX features such as hx-confirmation, hx-get, and hx-target. Our goal was to create a functional website, demonstrating the versatility and effectiveness of HTMX in enhancing user interactions within web applications. We also demonstrated that you can make a Full-Stack web app with a minimal use of JavaScript, with only a couple functions on the front-end.

# Features
Tabs - Used to changed page content without refreshing URL.

Confirm Button - Can be used for extra function on back end using HTMX.

Store - Uses HTMX to return products, as well as using HTMX for the Search.

Product Page - Uses a template returned by HTMX and populated with an SQL query and flask.

Product Not Found - Uses HTMX to return content.

# Tech Summary

# Individual member notes

# Conclusion

# References


https://htmx.org/


https://chat.openai.com/

