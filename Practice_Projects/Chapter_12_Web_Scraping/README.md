With respect to the `command_line_emailer.py` the code is copied from https://github.com/thomaskellough/Automate-The-Boring-Stuff/blob/master/Practice-Projects/Ch%2011%20-%20Command%20Line%20Emailer.py with a few exceptions.

First of all, I changed the deprecated method `find_element_by_id` to `find_element` with it's respective parameter as you can see in the file I provided. Second and MOST IMPORTANT this code does not work. Why?

Well, `mail.google.com` does not allow to use directly automated software such as Selenium. Nor does Facebook or Twitter if you wanted to make an additional program. You would have to do it another way, the first step is probably consulting their API's.  
