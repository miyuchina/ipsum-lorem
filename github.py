import os

def to_gh_pages():
    """
    """
    os.system("git subtree push --prefix static origin gh-pages")
    
    print("Dumped to Github Pages.")
