# Python packages
import os

# External packages
from termcolor import colored

def to_gh_pages(commit_msg, site_obj):
    """
    Commit and push all files to main branch and gh-pages.

    Args:
        commit_msg: the commit message.
    """
    # make sure all files are added
    os.system("git add --quiet *")

    # commit and push to main branch
    os.system("git commit -m '{}' -a --quiet".format(commit_msg))
    os.system("git push --quiet")

    # push to gh-pages branch
    os.system("git subtree push --prefix static origin gh-pages --quiet")

    term_prompt_header = colored("[{}] ".format(site_obj.name), "cyan")
    print(term_prompt_header + "Dumped to Github Pages.")
