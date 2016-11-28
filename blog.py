import re, json

class Blog:
    """
    The Blog class to read config file and store site-wide variables.
    """
    def __init__(self, config_file="./config.json"):
        # Read config file.
        with open(config_file, "r") as fin:
            conf = json.load(fin)

        # Site-wide variables.
        self.name = conf["blog_name"]
        self.default_author = conf["default_author"]
        self.baseurl = conf["baseurl"]

        self._posts_dir = conf["posts_dir"]
        self._assets_dir = conf["assets_dir"]
        self._theme_dir = conf["styles_dir"] + conf["theme"] + "/"
        self._js_dir = conf["js_dir"]
        self._templates_dir = conf["templates_dir"]
        self._static_dir = conf["static_dir"]

        # ignore files with these patterns
        self._ignore_posts = [re.compile(pattern) for pattern in conf["ignore_posts"]]

    def get_posts_dir(self): return self._posts_dir
    def get_assets_dir(self): return self._assets_dir
    def get_theme_dir(self): return self._theme_dir
    def get_js_dir(self): return self._js_dir
    def get_templates_dir(self): return self._templates_dir
    def get_static_dir(self): return self._static_dir
    def get_ignore_posts(self): return self._ignore_posts

    def check_included(self, filename):
        """
        """
        if not filename.endswith(".md"):
            return False

        for REGEX in self.get_ignore_posts():
            if re.match(REGEX, filename):
                return False
        return True
