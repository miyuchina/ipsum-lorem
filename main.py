# System packages
import os, sys

# User-defined
import dump, github, server

def usage():
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    else:
        if sys.argv[1] == "github":
            github.to_gh_pages()
        elif sys.argv[1] == "local":
            server.app.run()
