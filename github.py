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
    os.system("git add *")

    # commit and push to main branch
    os.system("git commit -m '{}' -a".format(commit_msg))
    os.system("git push")

    # push to gh-pages branch
    os.system("git subtree push --prefix {} origin gh-pages".format(site_obj.get_static_dir()))

    term_prompt_header = colored("[{}] ".format(site_obj.name), "cyan")
    print(term_prompt_header + "Dumped to Github Pages.")
