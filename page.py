# Python packages
import re, os

# External packages
import markdown2

class Page:
    """
    Base class for page objects.
    """
    def __init__(self, page_type):
        """
        Args:
            page_type: the type of page.
        """
        self._page_type = page_type

    # Accessor method
    def get_page_type(self): return self._page_type

    def dump(self, env, site_obj, dst):
        template = env.get_template(self.get_page_type() + ".html")
        style = "css/{}.css".format(self.get_page_type())
        baseurl = get_baseurl(site_obj, dst)

        os.makedirs(site_obj.get_static_dir(), exist_ok=True)
        with open("{}{}.html".format(site_obj.get_static_dir(),
                                     self.get_page_type()), "w+") as f:
            f.write(template.render(site=site_obj,
                                    style=style,
                                    baseurl=baseurl))

class Index(Page):
    """
    A subclass of Page with page_type = "index".
    """
    def __init__(self):
        # self._page_type = "index"
        super().__init__("index")

    def dump(self, env, site_obj, included_posts, dst):
        """
        Generate static pages for index.

        Args:
            env: the template environment.
            site_obj: a site object.
            included_posts: a list of included posts.
            dst: serve locally or on Github Pages.
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
                                    baseurl=baseurl))

class Post(Page):
    """
    A subclass of Page with page_type = "post".
    """
    def __init__(self):
        super().__init__("post")
        self._title = ""
        self._author = ""
        self._date = ""
        self._content = ""
        self._excerpt = ""
        self._static_path = ""

    def load(self, md_file):
        """
        Populate a Post instance with contents of the md_file.

        Args:
            md_file: the path to the markdown file.
        """
        self._title, self._author, self._date, self._content, self._excerpt = parse(md_file)
        month, _, year = self._date.split("-")
        self._static_path = "posts/{}/{}/{}".format(year, month, self._title)

    # Accessor methods
    def get_title(self): return self._title
    def get_author(self): return self._author
    def get_content(self): return self._content
    def get_date(self): return self._date
    def get_excerpt(self): return self._excerpt
    def get_static_path(self): return self._static_path

    def dump(self, env, site_obj, dst):
        template = env.get_template('post.html')
        style = "css/post.css"
        static_path = site_obj.get_static_dir() + self.get_static_path()
        baseurl = get_baseurl(site_obj, dst)

        os.makedirs(os.path.dirname(static_path), exist_ok=True)
        with open(static_path + ".html", "w+") as f:
            f.write(template.render(site=site_obj,
                                    post=self,
                                    style=style,
                                    baseurl=baseurl))

    # provide a way to sort posts according to publication date
    def getKey(self):
        month, day, year = self._date.split("-")
        return "{}-{}-{}".format(year, month, day)

class About(Page):
    """
    A subclass of Page with page_type = "about".
    """
    def __init__(self):
        super().__init__("about")

def get_baseurl(site_obj, dst):
    return site_obj.baseurl if dst == "github" else "//localhost:5000/"

def parse(md_file):
    """
    Parse the header information and content from the markdown file.

    Args:
        md_file: the path to markdown file.
    """
    frontmatter = {}

    with open(md_file) as fin:
        # Bad practice. Fix this if possible.
        md = "".join(fin)

        # Match the frontmatter.
        REGEX = re.compile("(.+?)-{3}", re.DOTALL)
        lines = re.match(REGEX, md).group(1).splitlines()

        # Store the frontmatter.
        for line in lines:
            key, value = line.split(": ")
            frontmatter[key] = value

        # Match the content.
        REGEX = re.compile("-{3}\n(.*)$", re.DOTALL)

        # Store the content and excerpt.
        content = re.search(REGEX, md).group(1)
        excerpt = re.match("(.*)\n", content).group(1)

        # Parse the content and excerpt.
        content = markdown2.markdown(content)
        excerpt = markdown2.markdown(excerpt)

    title = frontmatter.get("title", "Untitled")
    author = frontmatter.get("author", "Anonymous")
    date = frontmatter.get("date", "01-01-1970")

    return title, author, date, content, excerpt
