# WordPress Markdown Package for BBEdit #

A set of scripts, text filters, and clippings for writing and posting WordPress blog entries in Markdown from within BBEdit.

## Resources ##

These are a set of helper scripts that are called by the user-facing scripts, text filters, and clippings.

**bbstdin** (Shell script)  
A utility script that converts BBEdit text into `stdin` for piping to other scripts.

* Fuller description: [This blog post][11].
* External requirement: None.
* Needs editing: No.

**get-post** (Python script)  
Retrieve the header and text of the specified blog post and return it in `stdout`.

* Fuller description: [This blog post][9].
* External requirement: You must have a Keychain entry with a name set to the URL of the blog's `xmlrpc.php` file, an account set to the blog's username, and a password set to the blog's password.
* Non-standard libraries: [`pytz`][2], [`keyring`][3]
* Needs editing: The `url` and `user` variables must be personalized to the blog's `xmlrpc.php` URL and username. The `myTZ` variable must be set to the blog's time zone.

**recent-posts** (Python script)  
Return a list of recent posts with post number and title for each.

* Fuller description: [This blog post][9].
* External requirement: You must have a Keychain entry with a name set to the URL of the blog's `xmlrpc.php` file, an account set to the blog's username, and a password set to the blog's password.
* Non-standard libraries: [`keyring`][3]
* Needs editing: The `url` and `user` variables must be personalized to the blog's `xmlrpc.php` URL and username.

**nextreflink** (Python script)  
Scan text for numbered Markdown reference-style links and return the next ont in the series.

* Fuller description: [This blog post][11].
* External requirement: None.
* Non-standard libraries: None.
* Needs editing: No.

**getreflink** (Python script)  
Scan text for Markdown reference-style links, display them in a dialog box, and return the one chosen by the user.

* Fuller description: [This blog post][9].
* External requirement: The [CocoaDialog application][10].
* Non-standard libraries: None.
* Needs editing: No.

**glucky** (Ruby script)  
Return URL of Google's "I'm Feeling Lucky" link for the given text.

* Fuller description: [This blog post][13].
* External requirement: None.
* Non-standard libraries: None.
* Needs editing: No.

**prepend-language** (Perl script)  
Determine a script's language from its shebang line (if present) and return the script with that language prepended to it.

* Fuller description: [This blog post][4].
* External requirement: None.
* Non-standard libraries: None.
* Needs editing: No.

**flickroriginal** (Python script)  
Return an `<img>` link to the Original image file shown on the Flickr page in the frontmost Safari tab.

* Fuller description: The library is described in [this post][14].
* External requirement: None.
* Non-standard libraries: [`currentflickr`][15].
* Needs editing: No, but Flickr API credentials the `currentflickr` library it's based on will need to be changed.

**flickr640** (Python script)  
Return an `<img>` link to the Medium 640 image file shown on the Flickr page in the frontmost Safari tab.

* Fuller description: The library is described in [this post][14].
* External requirement: None.
* Non-standard libraries: [`currentflickr`][15].
* Needs editing: No, but Flickr API credentials the `currentflickr` library it's based on will need to be changed.

**flickr800** (Python script)  
Return an `<img>` link to the Medium 800 image file shown on the Flickr page in the frontmost Safari tab.

* Fuller description: The library is described in [this post][14].
* External requirement: None.
* Non-standard libraries: [`currentflickr`][15].
* Needs editing: No, but Flickr API credentials the `currentflickr` library it's based on will need to be changed.

**flickr1024** (Python script)  
Return an `<img>` link to the Large image file shown on the Flickr page in the frontmost Safari tab.

* Fuller description: The library is described in [this post][14].
* External requirement: None.
* Non-standard libraries: [`currentflickr`][15].
* Needs editing: No, but Flickr API credentials the `currentflickr` library it's based on will need to be changed.


## Text Filters ##

**Publish Post.py** (Python script)  
Takes the current window or selection and publishes it.

* Fuller description: [This blog post][1].
* External requirement: You must have a Keychain entry with a name set to the URL of the blog's `xmlrpc.php` file, an account set to the blog's username, and a password set to the blog's password.
* Non-standard libraries: [`pytz`][2], [`keyring`][3]
* Needs editing: The `url` and `user` variables must be personalized to the blog's `xmlrpc.php` URL and username. The `myTZ` variable must be set to the blog's time zone.

**Line-Numbered Source Code.textfactory** (BBEdit text factory)  
Takes the selected lines, numbers the lines, indents it so Markdown will format it as source code, and prepends a language description if there's a `#!` line.

* Fuller description: [The text factory][4], [the JavaScript function for formatting line numbers][5], and [the syntax highlighting JavaScript library][6].
* External requirement: The JavaScript described above.
* Needs editing: Yes, you'll probably have to reset the Unix filter in the fourth step of the factory to the `prepend-language` script in the package's `Resources` folder. The connection to that script often gets broken when I move the package.

**Tabs to Markdown Table.pl** (Perl script)  
Takes a set of lines with tab-separated values and turns it into a MultiMarkdown-style table. Most useful when copying a table from a spreadsheet into a Markdown file.

* Fuller description: [This blog post][7].
* External requirement: None.
* Non-standard libraries: None.
* Needs editing: No.

**Normalize Table.py** (Python script)  
Takes a MultiMarkdown-style table with ragged column separators and aligns them. Intended to be used with a non-proportional font.

* Fuller description: [This blog post][7].
* External requirements: None.
* Non-standard libraries: None.
* Needs editing: No.

**Tidy Markdown Reference Links.py** (Python script)  
Renumbers and reorders Markdown reference links in a post.

* Fuller description: [This blog post][8].
* External requirements: None.
* Non-standard libraries: None.
* Needs editing: No.
* Warning: Doesn't work if the post contains sections of Markdown source code with example reference links.

## Scripts ##

**Get Recent Post** (AppleScript)  
Presents a list of the 15 most recent blog posts. Creates a new window with the selected post. Uses the `get-post` and `recent-posts` helper scripts.

* Fuller description: [This blog post][9].
* External requirements: Same Keychain entries as the Publish Post text filter and the [CocoaDialog application][10].
* Needs editing: No.

**New Reference Link** (AppleScript)  
Creates a new Markdown reference-style link, defaulting to the URL of the frontmost tab of Safari. Uses the `nextreflink` helper script.

* Fuller description: [This blog post][11].
* External requirements: None.
* Needs editing: No.

**Old Reference Link** (AppleScript)  
Creates a Markdown reference-style link to a URL already in the document. Uses the `getreflink` helper script.

* Fuller description: [This blog post][12].
* External requirements: The [CocoaDialog application][10].
* Needs editing: No.

**Google Lucky Link** (AppleScript)  
Creates a Markdown reference style link to the "I'm Feeling Lucky" hit on the selected text. Uses the `glucky` helper script.

* Fuller description: [This blog post][13].
* External requirements: None.
* Needs editing: No.

## Clippings ##

These are kept in a Blogging subgroup and are tied to Markdown files.

**Post header**  
Inserts a post template with fill-in spots for the title, keywords, and body. The publication date is given an initial value of two hours from the time the clipping is inserted.

**Flickr original image**  
Inserts an `<img>` link for the Original image file shown on the Flickr page in the frontmost Safari tab. Uses the `flickroriginal` helper script.

**Flickr 640 image**  
Inserts an `<img>` link for the Medium 640 image file shown on the Flickr page in the frontmost Safari tab. Uses the `flickr640` helper script.

**Flickr 800 image**  
Inserts an `<img>` link for the Medium 800 image file shown on the Flickr page in the frontmost Safari tab. Uses the `flickr800` helper script.

**Flickr 1024 image**  
Inserts an `<img>` link for the Large image file shown on the Flickr page in the frontmost Safari tab. Uses the `flickr1024` helper script.









[1]: http://www.leancrew.com/all-this/2013/08/scripts-for-wordpress-and-bbedit/
[2]: http://pytz.sourceforge.net/
[3]: https://pypi.python.org/pypi/keyring
[4]: http://www.leancrew.com/all-this/2013/01/a-line-numbering-text-factory-for-bbedit/
[5]: http://www.leancrew.com/all-this/2007/12/source-code-line-numbers-and-javascript/
[6]: http://www.leancrew.com/all-this/2010/12/new-syntax-highlighting-for-markdown/
[7]: http://www.leancrew.com/all-this/2012/11/markdown-table-scripts-for-bbedit/
[8]: http://www.leancrew.com/all-this/2012/09/tidying-markdown-reference-links/
[9]: http://www.leancrew.com/all-this/2013/08/scripts-for-wordpress-and-bbedit-part-2/
[10]: http://mstratman.github.io/cocoadialog/
[11]: http://www.leancrew.com/all-this/2012/08/markdown-reference-links-in-bbedit/
[12]: http://www.leancrew.com/all-this/2012/08/more-markdown-reference-links-in-bbedit/
[13]: http://www.leancrew.com/all-this/2013/01/google-lucky-links-in-bbedit/
[14]: http://www.leancrew.com/all-this/2011/08/more-flickr-api-stuff/
[15]: https://github.com/drdrang/flickr-stuff
