# System packages
import os, sys

# User-defined
import dump, github, server

def usage():
    print("Usage: python main.py [github|local] <commit-msg>")

if __name__ == "__main__":
    if len(sys.argv) < 2 or (sys.argv[1] == "github" and len(sys.argv) < 3):
        usage()
    else:
        if sys.argv[1] == "github":
            dump.generate(sys.argv[1])
            github.to_gh_pages(" ".join(sys.argv[2:]))
        elif sys.argv[1] == "local":
            dump.generate(sys.argv[1])
            server.app.run()
        else:
            usage()
