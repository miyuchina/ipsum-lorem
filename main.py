# Python packages
import os, sys

# User-defined packages
import dump, github, server

def usage():
    print("Usage: python main.py [github|local] <commit-msg>")

if __name__ == "__main__":
    # the command needs at least 2 args; if using github, 3 is needed
    if len(sys.argv) < 2 or (sys.argv[1] == "github" and len(sys.argv) < 3):
        usage()
    else:
        if sys.argv[1] == "github":
            # generate static files
            b = dump.generate(sys.argv[1])
            # push to github
            github.to_gh_pages(" ".join(sys.argv[2:]), b)

        elif sys.argv[1] == "local":
            # generate static files
            site_obj = dump.generate(sys.argv[1])
            # run the flask app locally
            app = server.create_app(site_obj)
            app.run()

        # only allow the two flags above
        else:
            usage()
