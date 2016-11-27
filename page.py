import re, os
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

    def get_page_type(self): return self._page_type

class Index(Page):
    """
    A subclass of Page with page_type = "index".
    """
    def __init__(self):
        super().__init__("index")

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
        self._static_path = ""

    def load(self, md_file):
        self._title, self._author, self._date, self._content = parse(md_file)
        month, _, year = self._date.split("-")
        self._static_path = "posts/{}/{}/{}".format(year, month, self._title)

    def get_title(self): return self._title
    def get_author(self): return self._author
    def get_content(self): return self._content
    def get_date(self): return self._date
    def get_static_path(self): return self._static_path

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

        # Store the content.
        content = markdown2.markdown(re.search(REGEX, md).group(1))

    title = frontmatter["title"]
    author = frontmatter["author"]
    date = frontmatter["date"]

    return title, author, date, content
