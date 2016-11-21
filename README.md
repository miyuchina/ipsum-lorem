# Final Project Proposal

[The perfect static website generator is the one you write yourself.](https://schier.co/blog/2014/12/02/the-perfect-static-website-generator-is-the-one-you-write-yourself.html)

This project aims to build a Python-based static site generator, with focuses on expandability, full custom control and ease of use. The framework design has both web developers and blog writers in mind, but should completely separate code from blog posts. The goal is to deploy and start a blog on a server with as little hassle as possible.

## Data Plan
*Not applicable.*

## Implementation Plan
This project will be a Python mock-up of existing static site generators, such as [Jekyll](https://jekyllrb.com), [Hugo](https://gohugo.io), etc., but will start from scratch. References to existing products are limited to studying their features and functionalities, without looking at their design or implementation.

The final product will include one set of default HTML and CSS theme, with a set of bare-bone templates written in Jinja2, but will otherwise be implemented in Python. Relevant skills include:

- Using class and inheritance to create different `Page` objects and support further expandability;
- Using regular expressions to parse YAML-style front matters in Markdown files;
- Using `json` package to parse site-wide preferences in `config.json`;
- Implementing an HTTP server using Python packages.

### External Libraries

- [markdown2](https://github.com/trentm/python-markdown2)
- [Jinja2](http://jinja.pocoo.org)
- [watchdog](https://pypi.python.org/pypi/watchdog)

### Milestones
- Support parsing blog posts written in Markdown;
- Support Jinja2 template language; basic framework implementation;
- Support side-wide configurations in `config.json`;
- Generate `index.html` with proper "read more" buttons, search and tag functionality;
- Support default code highlighting, comment section and bootstrap; provide a default theme;
- Support local deployment and basic server functionalities;
- Monitor file changes and auto-regenerate static files;
- Support GitHub Pages.


## Deliverables
- `server.py`

# Final Project Report
*What you have achieved/learned*

*What open questions remain*

## Instructions to run the code

(*Incomplete.*)

```sh
$ ./server.py deploy
$ ./server.py serve 8080
```

Current structure:

```
.
├── assets
│   └── images
├── content
│   ├── posts
│   │   ├── sample1.md
│   │   └── sample2.md
│   └── index.html
├── layouts
│   ├── css
│   │   └── default.css
│   ├── js
│   │   └── default.js
│   └── templates
│       ├── index.html
│       ├── layout.html
│       └── post.html
├── static
│   └── posts
│   │   ├── 10-21-2011 - Sample Post 1.html
│   │   └── 11-11-1991 - An Exhibit of Markdown.html
│   └── index.html
├── blog.py
├── config.json
├── page.py
└── server.py
```

