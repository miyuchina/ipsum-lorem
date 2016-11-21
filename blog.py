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

        self._posts_dirs = conf["posts_dirs"]
        self._styles_dirs = conf["styles_dirs"]
        self._js_dirs = conf["js_dirs"]
        self._templates_dirs = conf["templates_dirs"]

        # ignore files with these patterns
        self._ignore_posts = [re.compile(pattern) for pattern in conf["ignore_posts"]]

    def get_posts_dirs(self): return self._posts_dirs
    def get_styles_dirs(self): return self._styles_dirs
    def get_js_dirs(self): return self._js_dirs
    def get_templates_dirs(self): return self._templates_dirs
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
