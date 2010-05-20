byteprint
=========

A publishing platform built on top of django

There are so many blogging/publishing systems on the web today (especially in the django community), most of which revolve around the idea that the 'article' is the most important piece of content - the lowest common denominator. byteprint challenges that idea by arguing that the individual pieces of content themselves (the videos, the code snipets, the twitter streams, etc.) are first class citizens, and should be treated as such. A WYSIWYG editor is not enough to create and edit this kind of content, and the common approach of dropping in 'inline' content to represent these things makes for a pretty ugly melting pot of content.

In byteprint, every 'scrap' of content is stored separately, and can be organised into piles which become the pages and articles of your website. Each scrap has its own editor, and its own unique way of presenting itself, exposing CSS classes for you to begin styling them independently. Commonly used pieces of code, such as YouTube video embeds, Disqus comments modules and Twitter API calls, can all be hidden away inside scrap blueprints, meaning you only need to enter the fields that matter when embedding content into your site.

Installation
------------

First, please ensure you have all the dependencies (python_dependencies.txt). This includes django 1.2 and PIL.

*Quickstart*

1. Navigate to the `/byteprint` directory in your terminal and enter following the command:
    
    python manage.py runserver

3. Visit `http://127.0.0.1:8000` in your web browser.
4. Enter your site details.

That's it! You can now visit your site, or log into the admin site to start publishing. For now, you're just using SQLite as your database backend, so for a more permanent solution, you'll want to provide connection details to a real database. This can be done by editing `/byteprint/bp/database.py`. Instructions are provided in the file.

More advanced settings can be changed inside `/byteprint/bp/settings.py`, but I suggest you leave these alone unless you have experience working with django/python.

Publishing Articles/Pages
-------------------------

To create a new article in the admin site, just enter a name for it and submit the form. You'll be taken into the first 'scrap' of the article, which by default is a WYSIWYG editor. If you access the article again from the main Articles page (use the left hand nav to get there), you can then start adding and rearranging scraps to build up your article. Click the edit button (which looks like a yellow note with a pencil) to edit any scrap. Currently, you can enable or disable the rendering of any scrap by clicking the 'eye' icon on the left of the scrap in 'pile' view. [NOTE: this format will change in the near future, joining both 'views' of the article into a single editing page] All articles and pages begin as drafts, so you'll have to manually publish them to see them on your site. To do this, hover over the article on the main article section, and click 'quick edit'. You then need to check the 'Publish' box, and save. Then have a look on your site!

Global Site Scrap Piles
-----------------------

Common site 'widgets', such as Recent Articles lists, and Pages' lists are all handled in exactly the same way as articles - they're scraps, and you can enable 'piles' of them anywhere in your site by placing a single tag in your Theme's template. [Note: the Theme system is still in development - have a look at the `byteprint/bp/themes` folder to see a rudimentary concept].

Scrap Blueprints (For Developers)
---------------------------------

All scraps are based on a single Python class which defines what fields you'd like to capture, and how you'd like that information to be presented. Have a look in `/byteprint/bp/core/scraps/blueprints` to see the core set that byteprint comes with for writing content. Blueprints have access to the entire framework, plus any extensions you write. The possibilities are endless. The framework currently supports a basic set of blueprints, but I encourage you to experiment and make your own. Have a look at the `extensions` folder to see how you can write your own scrap blueprints. To activate one, just drop the plugin into the `byteprint/bp/plugins` directory and restrt your server. I look forward to seeing what you come up with - my head is bursting with ideas for scraps, and I know you'll feel inspired too once you see how easy it is.

Thanks
------

Like a lot of open source software, byteprint doesn't reinvent the wheel where it doesn't need to. Some of the functionality has already been implemented by many other great minds in the django/python community, and fit in nicely with this type of project. I've listed all the people who have indirectly contributed to byteprint in the credits.txt file, but I'd also like to take the opportunity to thank them here.

Although the interface for the site and admin look a bit shinier than most projects in their infancy, this is only becuase I get distracted by the look & feel rather than knuckling down and making it feature complete. byteprint is still under heavy development, but it exists prematurely here on github because I want you to be a part of that process.
