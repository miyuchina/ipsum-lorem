import os
import blog, page
from jinja2 import Environment, FileSystemLoader

def generate():
    """
    Generate all static pages.
    """

    def dump(page_obj, static_dir):
        """
        Select the correct dump method base on page type.

        Args:
            page_obj: a page object.
            static_dir: the output directory.
        """
        if page_obj.get_page_type() == "index":
            dump_index(page_obj, static_dir)
        elif page_obj.get_page_type() == "post":
            dump_post(page_obj, static_dir)

    def dump_index(env, site_obj, included_posts, static_dir):
        """
        Generate static pages for index.

        Args:
            env: the template environment.
            site_obj: a site object.
            included_posts: a list of included posts.
            static_dir: the output directory.
        """
        template = env.get_template('index.html')

        with open(static_dir + "index.html", "w+") as f:
            f.write(template.render(site=site_obj, posts=included_posts))

    def dump_post(env, site_obj, post_obj, static_dir):
        """
        Generate static pages for posts.

        Args:
            env: the template environment.
            site_obj: a site object.
            post_obj: a page object with page_type = "post".
            static_dir: the output directory.
        """
        template = env.get_template('post.html')

        static_name = "{} - {}.html".format(post_obj.get_date(), post_obj.get_title())
        with open(static_dir + static_name, "w+") as f:
            f.write(template.render(site=site_obj, post=post_obj))

    # Create Blog, Environment and Post objects.
    i = page.Index()
    s = blog.Blog()
    env = Environment(loader=FileSystemLoader(s.get_templates_dirs()))

    included_posts = []

    # Generate all posts.
    for post_dir in s.get_posts_dirs(): # Look under all post directories.
        for md_file in os.listdir(post_dir): # Iteratre over all post files.
            if s.check_included(os.path.basename(md_file)):
                p = page.Post()
                p.load(post_dir + md_file)
                dump_post(env, s, p, "./static/posts/")
                included_posts.append(p)

    # Generate index.
    dump_index(env, s, included_posts, "./static/posts/")


def serve():
    pass

if __name__ == "__main__":
    generate()
    serve()
