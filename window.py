from gi.repository import Gtk
import sys


class MyApplication(Gtk.Application):

    def do_activate(self):
        # create a Gtk Window belonging to the application itself
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

# create and run the application, exit with the value returned by
# running the program
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)