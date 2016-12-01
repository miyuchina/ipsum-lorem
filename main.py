# Python packages
import os, sys, shutil

# User-defined packages
import dump, github, server

def usage():
    print("Usage: python main.py [github|local] <commit-msg>")

if __name__ == "__main__":
    # the command needs at least 2 args; if using github, 3 is needed
    if len(sys.argv) < 2 or (sys.argv[1] == "github" and len(sys.argv) < 3):
        usage()
    elif sys.argv[1] == "init":
        dump.init()
    elif sys.argv[1] == "cleanup":
        # remove all static files and create a new static folder
        dump.cleanup()

    else:
        # generate static files
        site_obj = dump.generate(sys.argv[1])

        if sys.argv[1] == "github":
            # push to github
            github.to_gh_pages(" ".join(sys.argv[2:]), site_obj)

        elif sys.argv[1] == "local":
            # run the flask app locally
            app = server.create_app(site_obj)
            app.run()

        # only allow the two flags above
        else:
            usage()
