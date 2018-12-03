Writeup 14 - Web II
=====

Name: Lauren Kosub
Section: 0102

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Lauren Kosub

## Assignment 10 Writeup

### Part 1 (70 Pts)
After examining the source code and playing around with the website, I noticed
that item pages were queried via the url, mainly
    cornerstoneairline.co:8080/item?id=<ID>, where id is meant to be 0,1,or 2.
I saw this as a means of providing input to the website, aka my way in. After 
further trying to change the inputs to id to see what would happen, I found 
that the webpage crashed when provided single quotations ('). This made me 
realize that the input to id was encased with single quotes. I translated the
url request to a SQL query below:
    SELECT * FROM table WHERE id='<ID>'
In an attempt to display every thing from the table, I substituted 1' or '1'='1
as shown below. I made sure to account for the opening and closing single quotes
provided.
    SELECT * FROM table WHERE id=' <1' OR '1'='1> '
I then translated this back to a url to get
    http://cornerstoneairlines.co:8080/item?id=1' or '1'='1
This url yieled a page with all of the table's information, and with it there
was a flag!
    CMSC38R-{y0U-are_the_5ql_n1nja}



### Part 2 (30 Pts)
Level 1: Hello world of XSS
    input: <script>alert()</script>
    
    The objective was to inject a script to pup up a JavaScript alert() in the
    frame below, so I used <script> tag to call alert().

Level 2: Persistence is key
    input:  <img src='image.gif' onerror='alert()'>
    
    The objective of this level was to use a post to exectute alert(). I noticed
    that the first example post had coloring and after further investigation
    I found that it was JavaScript in the target code. Since the posts were 
    treated as Javascript, I decided to try and attach an image to my post, as
    any normal user would do, but I used onerror to say that if the image could
    not be attached (i.e. if it didn't exist), I would call alert().

Level 3: That sinking feeling
    url input: https://xss-game.appspot.com/level3/frame#default=<img src='image.gif' onerror='alert()'>

    The objective of this level was to execute alert() using the address in the
    URL bar since you can't enter the payload anywhere in the application. After
    looking at the target code, I noticed that you could inject the command using
    window.location.hash (with your input being num). I looked up xxs injection 
    in hash and found that this volunerability is known as DOM based XXS. From 
    this I learned that I needed to use #default= to set a default when no
    number is entered. I simply put the default as my input from level 2 and it 
    worked.

Level 4: Context Matters
    input: 1}}'); alert('{{

    After looking at the source code, I noticed that thetimer is called using
    the method startTimer where the input is the user input. Therefore, I knew 
    that since the format was "startTimer('{{ timer }}');" I could give the 
    timer a time, close the function, then execute the alert() function 
    following the startTimer function just by escaping data.

    
Level 5: Breaking Protocol
    url input: https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert()
    
    After inspecting the target code and going through the different pages of 
    the website, I discovered that on the signup page, there is an oportunity 
    to input a value for next. Looking back at the source code, looking 
    specifically for how next is used, I found the line:
        <a href="{{ next }}">Next >></a>
    "{{ next }}" was also in confirm.html, and confirm is the default input to
    next, so I knew by changing confirm to javascript:alert(), I could execute
    the alert command.

Level 6: Follow the Rabbit
    url input: https://xss-game.appspot.com/level6/frame#HTTPs://google.com/jsapi?callback=alert    

    The objective is to make the application request an external file which will
    cause it to execute an alert(). After looking at the target code and playing
    around with changing the url after the #, I found that the site uploaded a
    page; however, they did not allow http(s) pages. However, the check for http(s)
    was case sensitive so hTtp(s) was accepted; therefore I could use 
    HTTPs://google.com/jsapi?callback=alert, which is just a webpage that calls
    the command you assign callback to.

