from os.path import dirname, basename, isfile
import glob
import site
import os
import imp


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(root_dir)
    print root_dir
    site.addsitedir(root_dir)
    print "Launching Motuus!"
    packages = ["numpy", "pygame", "flask", "flask_socketio", "eventlet"]
    for p in packages:
        try:
            imp.find_module(p)
            print "Package Found: " + p
        except ImportError:
            print "ERROR! Package Not Found: ", p, "."
            return
    optional_packages = ["matplotlib", "panda3d"]
    for p in optional_packages:
        try:
            imp.find_module(p)
            print "Package Found: " + p
        except ImportError:
            print "WARNING! Package Not Found: ", p, ". Some features will not work."
            pip_message(p)
    from motuus.web.home import run
    run()

def pip_message(p):
    print "Install the missing package using the command:"
    print '    pip install " + p + "' (on Windows)"
    print '    sudo pip install " + p + "' (on Mac / Linux)"
    print "Before that, you might need to upgrade pip using 'pip install --upgrade pip'"



if __name__ == '__main__':
    main()
