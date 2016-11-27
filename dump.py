# Python packages
import os, shutil
import http.server, socketserver

# User-defined packages
import blog, page

# External packages
from jinja2 import Environment, FileSystemLoader


def dump_index(env, site_obj, included_posts):
    """
    Generate static pages for index.

    Args:
        env: the template environment.
        site_obj: a site object.
        included_posts: a list of included posts.
        static_dir: the output directory.
    """
    template = env.get_template('index.html')
    index_style = "css/index.css"

    with open(site_obj.get_static_dir() + "index.html", "w+") as f:
        f.write(template.render(site=site_obj, posts=included_posts, style=index_style))

def dump_post(env, site_obj, post_obj):
    """
    Generate static pages for posts.

    Args:
        env: the template environment.
        site_obj: a site object.
        post_obj: a page object with page_type = "post".
        static_dir: the output directory.
    """
    template = env.get_template('post.html')
    post_style = "../../../css/post.css"
    static_path = site_obj.get_static_dir() + post_obj.get_static_path()

    os.makedirs(os.path.dirname(static_path), exist_ok=True)
    with open(static_path + ".html", "w+") as f:
        f.write(template.render(site=site_obj, post=post_obj, style=post_style))

def dump_css(env, site_obj):
    css_static_dir = site_obj.get_static_dir() + "css/"

    for css_file in os.listdir(site_obj.get_theme_dir()):
        shutil.copy(site_obj.get_theme_dir() + css_file, css_static_dir)


def generate():
    """
    Generate all static pages.
    """
    # Create Blog, Environment and Post objects.
    i = page.Index()
    b = blog.Blog()
    env = Environment(loader=FileSystemLoader(b.get_templates_dir()))

    included_posts = []

    # Generate all posts.
    for md_file in os.listdir(b.get_posts_dir()):
        if b.check_included(os.path.basename(md_file)):
            p = page.Post()
            p.load(b.get_posts_dir() + md_file)
            dump_post(env, b, p)
            included_posts.append(p)

    # Generate index.
    dump_index(env, b, included_posts)

    # Generate css.
    dump_css(env, b)

if __name__ == "__main__":
    generate()
