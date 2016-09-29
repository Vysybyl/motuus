from os.path import dirname, basename, isfile, abspath
import site
import imp
import socket
import fcntl
import struct

def main():
    root_dir = dirname(abspath(__file__))
    root_dir = dirname(root_dir)
    site.addsitedir(root_dir)
    print "You are about to launch motuus..."
    print ""
    print "The following python packages are needed for the program to run:"
    packages = ["numpy", "pygame", "flask", "flask_socketio", "eventlet"]
    optional_packages = ["matplotlib", "panda3d"]
    for p in packages + optional_packages:
        print " - ", p
    print ""
    print "If any of this packages is missing, it will be automatically installed"
    print ""
    raw_input("Press ENTER to continue or CTRL+C to exit.")
    for p in packages:
        try:
            imp.find_module(p)
            print " . Package Found: " + p
            print ""
        except ImportError:
            print " . ERROR! Package Not Found: ", p, "."
            if not pip_try_install(p):
                return

    for p in optional_packages:
        try:
            imp.find_module(p)
            print " . Package Found: " + p
            print ""
        except ImportError:
            print " . WARNING! Package Not Found: ", p, "."
            pip_try_install(p, required=False)
    from motuus.web.home import run
    from motuus.globals import ROOT_FOLDER, PLAYER_SCRIPT
    print "The current root folder is:", ROOT_FOLDER
    print "Motuus will try to execute '" + PLAYER_SCRIPT + ".py'"
    print ""
    print "IMPORTANT: connect to motuus web server at http://" + get_ip_address() + ":5000"
    print ""
    print "Turn off motuus by selecting this window and pressing CTRL+C twice"
    print ""
    run()

def pip_try_install(p, required=True):
    print ""
    print "Trying to upgrade pip... (if needed)"
    try:
        import pip
        pip.main(['install', '--upgrade', 'pip'])
    except Exception:
        print " . ERROR! pip upgrade failed!"
        print "Try to run the program with admin rights:"
        print "    ON WINDOWS: open the command line as admin"
        print "    ON MAC: use 'sudo python main.py'"
        print ""
        print "If that doesn't work, you may need to install pip manually"
        return False
    print ""
    print "Trying to install ", p
    try:
        pip.main(['install', p])
    except Exception:
        print p, " installation failed!"
        if not required:
            print "motuus will still run but some features may not work"
        print ""
        print "Try to run the program with admin rights:"
        print "    ON WINDOWS: open the command line as admin and use 'python main.py'"
        print "    ON MAC / LINUX: use 'sudo python main.py'"
        print ""
        print "If that doesn't work, you may need to install " + p + " manually:"
        print "    ON WINDOWS: open the command line as admin and use 'python -m pip install " + p + "'"
        print "    ON MAC / LINUX: 'sudo pip install " + p + "'"
        return False
    return True

def get_ip_address():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip




if __name__ == '__main__':
    main()
