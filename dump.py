# Python packages
import os, shutil

# User-defined packages
import blog, page

# External packages
from jinja2 import Environment, FileSystemLoader
from termcolor import colored

def get_term_prompt_header(site_obj):
    return colored("[{}] ".format(site_obj.name), "cyan")

def get_baseurl(site_obj, dst):
    return site_obj.baseurl if dst == "github" else "//localhost:5000/"

def init():
    b = blog.Blog()

    print(get_term_prompt_header(b) + "This could remove all your content.")
    confirmation = input(get_term_prompt_header(b) + "Are you sure? yes/no: ")

    if confirmation == "no":
        print(get_term_prompt_header(b) + "Action canceled by user.")

    elif confirmation == "yes":
        shutil.rmtree(b.get_static_dir(), ignore_errors=True)
        shutil.rmtree(b.get_assets_dir(), ignore_errors=True)
        shutil.rmtree(b.get_posts_dir(), ignore_errors=True)

        os.makedirs(b.get_assets_dir())
        os.makedirs(b.get_posts_dir())

        print(get_term_prompt_header(b) + "Done.")

    else:
        print(get_term_prompt_header(b) + "Invalid input. Exiting.")

def dump_index(env, site_obj, included_posts, dst):
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
    assets_path = "assets/"

    baseurl = get_baseurl(site_obj, dst)

    os.makedirs(site_obj.get_static_dir(), exist_ok=True)
    with open(site_obj.get_static_dir() + "index.html", "w+") as f:
        f.write(template.render(site=site_obj,
                                posts=included_posts,
                                style=index_style,
                                favicon_dir=assets_path + "favicon.ico",
                                img_dir=assets_path + "img",
                                baseurl=baseurl))

def dump_post(env, site_obj, post_obj, dst):
    """
    Generate static pages for posts.

    Args:
        env: the template environment.
        site_obj: a site object.
        post_obj: a page object with page_type = "post".
        static_dir: the output directory.
    """
    template = env.get_template('post.html')
    post_style = "css/post.css"
    static_path = site_obj.get_static_dir() + post_obj.get_static_path()
    assets_path = "assets/"

    baseurl = get_baseurl(site_obj, dst)

    os.makedirs(os.path.dirname(static_path), exist_ok=True)
    with open(static_path + ".html", "w+") as f:
        f.write(template.render(site=site_obj,
                                post=post_obj,
                                style=post_style,
                                favicon_dir=assets_path + "favicon.ico",
                                img_dir=assets_path + "img",
                                baseurl=baseurl))

def dump_css(site_obj):
    """
    Copy all the css files to the static folder.

    Args:
        site_obj: provides access to site-wide variables.
    """
    css_static_dir = site_obj.get_static_dir() + "css/"
    os.makedirs(css_static_dir, exist_ok=True)

    for css_file in os.listdir(site_obj.get_theme_dir()):
        shutil.copy(site_obj.get_theme_dir() + css_file, css_static_dir)

def dump_assets(site_obj):
    """
    Copy all the assets to the static folder.

    Args:
        site_obj: provides access to site-wide variables.
    """
    src = site_obj.get_assets_dir()
    dst = site_obj.get_static_dir() + "assets/"

    # Remove previously cached assets
    if os.path.exists(dst):
        shutil.rmtree(dst)

    # Copy to static folder
    shutil.copytree(src, dst)

def dump_about(env, site_obj, dst):
    """
    Generate the static about page.

    Args:
        site_obj: provides access to site-wide variables.
    """
    template = env.get_template('about.html')
    about_style = "css/about.css"
    assets_path = "assets/"

    baseurl = site_obj.baseurl if dst == "github" else "//localhost:5000/"

    os.makedirs(site_obj.get_static_dir(), exist_ok=True)
    with open(site_obj.get_static_dir() + "about.html", "w+") as f:
        f.write(template.render(site=site_obj,
                                style=about_style,
                                favicon_dir=assets_path + "favicon.ico",
                                baseurl=baseurl))


def generate(dst):
    """
    Generate all static pages.
    """
    # Create Blog, Environment and Post objects.
    i = page.Index()
    b = blog.Blog()
    env = Environment(loader=FileSystemLoader(b.get_templates_dir()))

    print(get_term_prompt_header(b) + "Generating static files...")

    included_posts = []

    # Generate all posts.
    for md_file in os.listdir(b.get_posts_dir()):
        if b.check_included(os.path.basename(md_file)):
            p = page.Post()
            p.load(b.get_posts_dir() + md_file)
            dump_post(env, b, p, dst)
            included_posts.append(p)

    # Generate index.
    included_posts = sorted(included_posts, key=page.Post.getKey, reverse=True)
    dump_index(env, b, included_posts, dst)

    # Generate about.
    dump_about(env, b, dst)

    # Generate css.
    dump_css(b)

    # Generate assets.
    dump_assets(b)

    print(get_term_prompt_header(b) + "Done.")

    # allow site_obj to pass through
    return b

def cleanup():
    b = blog.Blog()

    print(get_term_prompt_header(b) + "Removing legacy static files...")

    shutil.rmtree(b.get_static_dir())
    os.makedirs(b.get_static_dir())
    
    print(get_term_prompt_header(b) + "Done.")

if __name__ == "__main__":
    generate("github")
