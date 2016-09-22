from os.path import dirname, basename, isfile
import glob
import site
import os
import imp


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    print root_dir
    site.addsitedir(root_dir)
    print "Launching Motuus!"
    from motuus.web.home import run
    packages = ["numpy", "pygame", "flask", "flask_socketio"]
    for p in packages:
        try:
            imp.find_module(p)
            print "Package Found: " + p
        except ImportError:
            print "ERROR! Package Not Found: ", p, ". Please install the missing package"
            return
    optional_packages = ["matplotlib", "panda3d"]
    for p in optional_packages:
        try:
            imp.find_module(p)
            print "Package Found: " + p
        except ImportError:
            print "WARNING! Package Not Found: ", p, ". Some features will not work."
    run()


if __name__ == '__main__':
    main()