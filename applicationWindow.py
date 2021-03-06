from gi.repository import Gtk
import sys

# a Gtk ApplicationWindow


class MyWindow(Gtk.ApplicationWindow):
    # constructor: the title is "Welcome to GNOME" and the window belongs
    # to the application app

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)


class MyApplication(Gtk.Application):
    # constructor of the Gtk Application

    def __init__(self):
        Gtk.Application.__init__(self)

    # create and activate a MyWindow, with self (the MyApplication) as
    # application the window belongs to.
    # Note that the function in C activate() becomes do_activate() in Python
    def do_activate(self):

        #------create a Gtk Window belonging to the application itself----
        window = Gtk.Window(application=self)
        # set the title
        window.set_title("Welcome to GNOME")
        # show the window
        window.set_default_size(500, 400)
        # set_position(Gtk.WindowPosition.CENTER) centers the window. 
        # Other options are Gtk.WindowPosition.NONE, Gtk.WindowPosition.MOUSE, 
        # Gtk.WindowPosition.CENTER_ALWAYS, Gtk.WindowPosition.CENTER_ON_PARENT.
        window.set_position(Gtk.WindowPosition.CENTER_ON_PARENT)
        window.show_all()  

        #----------------Creating application window----------------------

        win = MyWindow(self)
        # show the window and all its content
        # this line could go in the constructor of MyWindow as well
        win.show_all()
        # set_position and set_default_size could be used with application window also
    # start up the application
    # Note that the function in C startup() becomes do_startup() in Python
    def do_startup(self):
        Gtk.Application.do_startup(self)

# create and run the application, exit with the value returned by
# running the program
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)