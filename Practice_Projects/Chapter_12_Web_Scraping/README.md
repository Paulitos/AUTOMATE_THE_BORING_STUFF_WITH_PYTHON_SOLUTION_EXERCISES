With respect to the `command_line_emailer.py` the code is copied from https://github.com/thomaskellough/Automate-The-Boring-Stuff/blob/master/Practice-Projects/Ch%2011%20-%20Command%20Line%20Emailer.py with a few exceptions.

Here the driver for Chrome 116: https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/win64/chromedriver-win64.zip, remember to do `chrome://version` in order to see the version of your browser and install the EXACT same version of the driver. 

First of all, I changed the deprecated method `find_element_by_id` to `find_element` with it's respective parameter as you can see in the file I provided (See documentation relating Selenium 4.3.0). Second and MOST IMPORTANT this code does not work. Why?

Well, `mail.google.com` does not allow to use directly automated software such as Selenium. Nor does Facebook or Twitter if you wanted to make an additional program. You would have to do it another way, the first step is probably consulting their API's.  
