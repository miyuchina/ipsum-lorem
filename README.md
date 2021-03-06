# Ipsum Lorem

[The perfect static website generator is the one you write yourself.](https://schier.co/blog/2014/12/02/the-perfect-static-website-generator-is-the-one-you-write-yourself.html)

This project aims to build a Python-based static site generator, with focuses on expandability, full custom control and ease of use. The framework design has both web developers and blog writers in mind, but should completely separate code from blog posts. The goal is to deploy and start a blog on a server with as little hassle as possible.

## Usage

### Workflow to publish a new post

1. Under `posts/` , create a new Markdown file similar to the one below:

   ```
   title: Some Title
   author: Some Author
   date: 01-01-1971
   ---
   The first paragraph (which will be used as excerpt.)

   And some other contents. With an image below:

   ![dr.watson](assets/img/dr_watson.jpg)
   ```

   *Optional:* Run `python main.py local` to see if the result is what you want.

   *Optional:* Name the Markdown file `ignore-sample.md` to be ignored by the site generator.

2. Run `python main.py github` .

3. There is no Step 3.

### Workflow to create a new static page

1. In `page.py`, define a new class and tell the super `__init__` method its page type, e.g.:

   ```python
   class About(Page):
       def __init__(self):
           super().__init__.("about")
   ```

2. Create a template with the same name under `templates/` (e.g. `about.html`) and provide a CSS file for it (e.g. `about.css`).

3. In the `generate()` function in `dump.py`, create a new instance of your class and dump it using the default dump method, e.g.:

   ```python
   a = page.About()
   a.dump(env, b, dst)
   ```

4. There is no Step 4.

### General Usage

```sh
$ python main.py                         # display usage information
Usage: python main.py [github|local] <commit-msg>

$ python main.py init	                 # regenerate file structure
[Another Blog] This could remove all your content.
[Another Blog] Are you sure? yes/no: yes
[Another Blog] Done.

$ python main.py local                   # run on localhost:5000 using flask
[Another Blog] Generating static files...
[Another Blog] Done.
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

$ python main.py github some commit msg  # publish the blog to Github Pages
[Another Blog] Generating static files...
[Another Blog] Done.
# Some git information
[Another Blog] Dumped to Github Pages.

$ python main.py cleanup                 # remove static files
[Another Blog] Removing legacy static files...
[Another Blog] Done.
```

### config.json

This file contains the basic settings of your blog. Most of the variables are pretty straight forward:

- blog_name: the name of your blog. Terminal prompt headers `[Another Blog] Done.` will change with this.

- default_author: the name of the author to be displayed in the footer.

- baseurl: the base URL of your site.

- description: the description to be included in the footer.

- contact: the bio information of the author to be included in the footer.

- theme: the theme of your blog. For example, if you have a file structure like this:

  ```sh
  [...]
  ├── templates
  │   ├── css
  │   │   ├── default
  │   │   │   ├── about.css
  │   │   │   ├── index.css
  │   │   │   └── post.css
  │   │   └── fancy
  │   │       ├── about.css
  │   │       ├── index.css
  │   │       └── post.css
  [...]
  ```

  you can specify `"theme": "fancy"` and the generator will use the css files you have under `css/fancy/` .

- highlight_style: determines which code highlighting style to use, e.g. `"highlight_style": "atom-one-dark"` . For a list of styles, see [highlight.js](https://highlightjs.org/).

- posts_dir: specifies the post directory (which means you can name your posts folder whatever you want. Same below.)

- assets_dir: specifies the assets directory.

- styles_dir: specifies the styles directory.

- js_dir: specifies the JavaScript directory.

- templates_dir: specifies the templates directory.

- static_dir: specifies the static directory.

- ignore_posts: contains a list of REGEX patterns that can be used to match filenames of your Markdown files. These files will then be ignored by the generator.

### File Structure:

```sh
.
├── assets
│   ├── img
│   │   └── dr_watson.jpg
│   └── favicon.ico
├── posts
│   ├── sample0.md
│   ├── [...]
│   └── sample5.md
├── templates
│   ├── css
│   │   └── default
│   │       ├── about.css
│   │       ├── index.css
│   │       └── post.css
│   ├── js
│   │   └── default.js
│   ├── about.html
│   ├── index.html
│   ├── layout.html
│   └── post.html
├── config.json
├── blog.py
├── page.py
├── dump.py
├── github.py
├── server.py
└── main.py
```

## Speed Tests

Due to the nature of static sites, they are very fast once deployed and uploaded to the server. All the processing takes place, then, when we generate the html files locally. Although we haven't done any optimizations, both `markdown2` and `jinja2` are extremely fast packages. Here is a test running from a fresh clone, containing 6 posts:

```sh
$ rm -rf static
$ rm -rf __pycache__
$ rm *.pyc
$ time python main.py local
[Another Blog] Generating static files...
[Another Blog] Done.
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
^C python main.py local  0.27s user 0.04s system 15% cpu 1.987 total
```

 `python main.py github` is restricted by the `git push` speed.

If we only run `dump.py` (i.e. only generate static files):

```sh
$ time python dump.py
[Another Blog] Generating static files...
[Another Blog] Done.
python dump.py  0.18s user 0.02s system 93% cpu 0.222 total
```

If we generate 100 posts:

```sh
$ time python main.py local
[Another Blog] Generating static files...
[Another Blog] Done.
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
^C python main.py local  1.24s user 0.07s system 6% cpu 19.517 total
```
