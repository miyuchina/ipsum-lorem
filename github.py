import os

def to_gh_pages(commit_msg):
    """
    """
    os.system("git commit -m '{}' -a".format(commit_msg))
    os.system("git push")
    os.system("git subtree push --prefix static origin gh-pages")
    
    print("Dumped to Github Pages.")
