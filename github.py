# Python packages
import os

def to_gh_pages(commit_msg):
    """
    Commit and push all files to main branch and gh-pages.

    Args:
        commit_msg: the commit message.
    """
    # make sure all files are added
    os.system("git add *")

    # commit and push to main branch
    os.system("git commit -m '{}' -a".format(commit_msg))
    os.system("git push")

    # push to gh-pages branch
    os.system("git subtree push --prefix static origin gh-pages")

    print("Dumped to Github Pages.")
