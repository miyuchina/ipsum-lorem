# Python packages
import re, json

class Blog:
    """
    Read config file and store site-wide variables.
    """
    def __init__(self, config_file="./config.json"):
        """
        When initializing a Blog instance, populate it with settings in the
        config file.

        In case of KeyError (user not providing settings in config.json),
        revert to default settings provided below.

        Args:
            config_file: specify the path to config file.
        """
        # Read config file.
        with open(config_file, "r") as fin:
            conf = json.load(fin)

        # Public variables
        self.name = conf.get("blog_name", "Another Blog")
        self.default_author = conf.get("default_author", "Anonymous")
        self.baseurl = conf.get("baseurl", "localhost:5000/")
        self.description = conf.get("description", "Some description.")
        self.contact = conf.get("contact", "Your contact information.")
        self.highlight_style = conf.get("highlight_style", "default")

        # Private variables
        self._posts_dir = conf.get("posts_dir", "posts/")
        self._assets_dir = conf.get("assets_dir", "assets/")
        self._theme_dir = (conf.get("styles_dir", "templates/css/")
                           + conf.get("theme", "default") + "/")
        self._js_dir = conf.get("js_dir", "templates/js/")
        self._templates_dir = conf.get("templates_dir", "templates/")
        self._static_dir = conf.get("static_dir", "static/")

        # ignore files with these patterns
        self._ignore_posts = [re.compile(pattern) for pattern
                              in conf.get("ignore_posts", ["ignore"])]

    # Accessor methods
    def get_posts_dir(self): return self._posts_dir
    def get_assets_dir(self): return self._assets_dir
    def get_theme_dir(self): return self._theme_dir
    def get_js_dir(self): return self._js_dir
    def get_templates_dir(self): return self._templates_dir
    def get_static_dir(self): return self._static_dir
    def get_ignore_posts(self): return self._ignore_posts

    def check_included(self, filename):
        """
        Check if a post should be included on the index page.

        Args:
            filename: the path to the markdown file.
        """
        # exclude non-markdown files
        if not filename.endswith(".md"):
            return False

        # exclude patterns specified in ignore_posts
        for REGEX in self.get_ignore_posts():
            if re.match(REGEX, filename):
                return False

        # passed all the tests, include this post
        return True
