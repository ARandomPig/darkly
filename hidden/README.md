# Finding the Hidden Flag

## How We Found It
First we went throught basic analysis of the website and thought of `.robots.txt`.

`Dissallow: /.hidden`

We wrote a script that crawled through the website’s `.hidden` directory. It checked every subdirectory and looked for each README file, examining the byte of its content. When that byte deviated from the expected pattern, we knew we’d found the flag!

## Utility of It
For this project, there wasn’t any real-world utility, it was just a roleplay exercise for school to learn about web crawling and threading.

## How Can We Patch It
The easiest fix is to restrict public access to sensitive files. Don’t place secret files in directories that are directly accessible from the web.
