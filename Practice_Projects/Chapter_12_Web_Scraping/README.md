## command_line_emailer.py

The code is copied from https://github.com/thomaskellough/Automate-The-Boring-Stuff/blob/master/Practice-Projects/Ch%2011%20-%20Command%20Line%20Emailer.py with a few exceptions.

Here the driver for Chrome 116: https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/win64/chromedriver-win64.zip, remember to do `chrome://version` in order to see the version of your browser and install the EXACT same version of the driver. 

First of all, I changed the deprecated method `find_element_by_id` to `find_element` with it's respective parameter as you can see in the file I provided (See documentation relating Selenium 4.3.0). Second and MOST IMPORTANT this code does not work. Why?

Well, `mail.google.com` does not allow to use directly automated software such as Selenium. Nor does Facebook or Twitter if you wanted to make an additional program. You would have to do it another way, the first step is probably consulting their API's.

## 2048.py

Code copied from: https://github.com/s0mnaths/Automate-the-Boring-Stuff-with-Python-Solutions, very recommended repository. I just updated the deprecated method. 

## link_verification.py
If you clicked on the link within the HTML source code, and it worked as expected without returning a 404 error, but your program reported a 404 error for the same link, there could be a few reasons for this discrepancy:

1. Timing or Network Issues: It's possible that when your program attempted to access the link, there was a temporary network issue or a delay in the response from the server, leading to a false 404 error. Clicking on the link manually later may have resulted in a successful connection.

2. Redirects: Some websites use URL redirects, where a link initially points to one URL but is automatically redirected to another. Your program might have encountered the initial URL, which could return a 404 error, while clicking manually led you to the final destination URL, which works.

3. JavaScript: If the webpage uses JavaScript to dynamically load content or manage links, your program may not be able to simulate this behavior correctly. Manual clicking can execute JavaScript actions that resolve the link differently.

4. Authentication: Some web pages require user authentication to access certain content or links. If your program doesn't handle authentication, it may receive 404 errors for links that require login credentials. Manual access could bypass this requirement if you're already logged in.

To address these issues, you might consider enhancing your program to handle redirects, delays, and JavaScript execution, and ensure it can handle any necessary authentication if applicable. Additionally, check if the program follows the same sequence of actions as manual clicking, such as submitting forms or navigating through multiple pages to reach a link's destination.
