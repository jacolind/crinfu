## files and folders

The following files and folders are in use:

1. library.py
1. import.py
1. import-check.py
1. functions.py
1. naming-conventions-objects.md
1. transform.py
1. transform-check.py
1. bandwitdh.py
1. plot.py
1. table.py
1. output/


Every file begin with a short description of what it does.

Output is saved to "output/" folder and the very important plots are saved into "/output/vip/".

The file "naming-conventions-objects.md" describes what convention are followed for creating objects.


## how to understand the code

Read every file in the list above, and read them in that order. The most crucial files are "import.py", "functions.py" and "transform.py".

"bandwitdh.py" is used for creating a bandwitdh rebalanced portfolio with 95% legacy assets and 5% digital assets.

Reading "plot.py" takes the most time, but it is straight forward to understand the plots if you understand how the data was imported and transformed.

A tip to get up to speed extra quickly is to only read the text after `##` which are my way in python of doing a heading. reading only these first will be like getting to know the structure of the code and learn _what_ is done before reading the details and learning _how_ it is done.

Lastly, there is a file called `coins2_20180523_2103.html`. This data analysis was produced during april and march, and splitting it up into .py files was neccessary to make hakan, simon and others to use the code in the future. The current files are robust, whereas in that .html file the code is a bit all over the place. nonetheless, reading the .html can give some insights into how the code is done. If you feel after having read import.py, functions.py, transform.py that you do not understand it, then the html file can be useful.

## todo

the file `TODO.md` contain an up to date todo list for the project.

in the files you can search for "todo" and find what needs to be worked on. these are often smaller things to be fixed. 
