# Motuus

#### *A movement enhancement python framework..*

Motuus is an open-source python framework that allows you to easily link motion capture data from a mobile device (smartphone, tablet, ...) with media events.

Motuus is currently in it's initial stage: it is not stable nor tested and it is distributed as is.

Motuus is distributed under [GPLv3] license.
## Install Motuus on Windows

First, **install** [python 2.7] (the framework might work on python 3, but it's never been tested). Be shure that the PYTHON_PATH is correctly configured by opening a command-line (*cmd.exe*) and typing 'python'. You should see something like :
```sh
c:\Users\Admin\Documents> python
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[MSC v.13.14.8.2 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
If you see an error, please follow these [instructions](https://docs.python.org/2.7/using/windows.html#excursus-setting-environment-variables)

Then, [download] !(or [clone] if you know how to use git) and unzip the latest version of Motuus.

No further installation is needed. Any missing packages will be installed the first time you run the application.

## Install Motuus on Mac / Linux:

On most Mac computers and probably on every Linux ones, [python 2.7] is already installed (the framework might work on python 3, but it's never been tested). To confirm it, please open the *terminal* and type 'python'. You should see something like:
```sh
jane@mylinux ~ $ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

If you see an error, please follow these [instructions](https://docs.python.org/2.7/using/mac.html#excursus-setting-environment-variables)

Then, [download] (or [clone] if you know how to use git) and unzip the latest version of Motuus.

No further installation is needed. Any missing packages will be installed the first time you run the application.

## Running Motuus
##### IMPORTANT:
**The first time you run Motuus, the python package pip will be upgraded and the program will attempt to install any missing dependency. This may break other working python programs that rely to older version of those dependencies. Please be sure that you understand this. If you are not using python for anything else but Motuus, there should be no risk.**

After you've followed the instructions above, open the command-line (on Windows, **as administrator**) or the terminal (on Mac/Linux)

Go to the same folder where you've unzipped Motuus by typing 'cd' followed by the folder full path. For instance
```sh
cd c:\Users\Admin\Documents\Motuus
```
Now type 'python main.py' (on Windows) or 'sudo python main.py' (on Mac - you may need to enter your password). You should see something like:
```sh
jane@mylinux ~ $ python main.py
You are about to launch motuus...

The following python packages are needed for the program to run:
 -  numpy
 -  pygame
 -  flask
 -  flask_socketio
 -  eventlet
 -  matplotlib
 -  panda3d

If any of this packages is missing, it will be automatically installed

Press ENTER to continue or CTRL+C to exit.
 . Package Found: numpy
 . Package Found: pygame
...
 . Package Found: panda3d

The current root folder is: /media/data/admin/code/motuus
Motuus will try to execute 'color_directions.py'
IMPORTANT: connect to motuus web server at http://192.168.1.8:5000
Turn off motuus by selecting this window and pressing CTRL+C twice
(7263) wsgi starting up on http://0.0.0.0:5000
```
As stated above, if any essential package is missing, it will be installed during the first run. If the installation fails the program will stop.

If a non essential package installation fails (for instance panda3d, which is only used for 3d object visualization) a warning will be displayed, but the program will still run unless you are trying to use a feature which needs the missing package to work.
## Connecting a mobile device
The information displayed on the terminal when you start Motuus includes a line that tells you which player is running
```sh
Motuus will try to execute 'color_directions.py'
```
and the local IP of your computer
```sh
IMPORTANT: connect to motuus web server at http://192.168.1.8:5000
```
If you open the displayed address ('http://192.168.1.8:5000' in the example above) from a mobile device that's connected to the same network as your computer, you will see a page with two buttons, a number field and several sensor readings which change rapidly.

**If none of the values on the page is changing**, you should try to open the page with another browser. Chrome and Mozilla should work fine. If the issue persists, you might be using a device that does not have any sensor.

To start transmitting the sensor data to Motuus, just press 'STREAM'. The button will turn green and your player will start to process the data.

To stop, just press the button again.

If you have any issue, try refreshing the page on the browser. If the issue persists, please stop motuus by pressing CTRL+C while the terminal (or command-line) window is focused. Forced stop is sometimes needed.

## Bugs
If you find a **bug** or an issue, or you'd like to see some feature that's currently not included, please report it [here].

[GPLv3]: <http://choosealicense.com/licenses/gpl-3.0/#>
[here]: <https://github.com/Vysybyl/motuus/issues>
[python 2.7]: <https://www.python.org/downloads/windows/>
[download]: <https://github.com/Vysybyl/motuus/archive/master.zip>
[clone]:<https://github.com/Vysybyl/motuus.git>
