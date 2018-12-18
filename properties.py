from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):
    # create a window

    def __init__(self, app, thingy):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)
        self.set_default_size(500, 500)

        if thingy=="image":
                
            # create an image
            image = Gtk.Image()
            # set the content of the image as the file filename.png
            image.set_from_file("image.jpg")
            # rotating the image
            # image.set_angle(25)  #### Image does not have the set angle attribute.
            # add the image to the window
            self.add(image)
        elif thingy=="label":
            # create a label
            label = Gtk.Label()
            # set the text of the label
            label.set_text("Hello GNOME!")
            #tilting the label
            label.set_angle(25)
            #horizontal alignment of the text
            label.set_halign(Gtk.Align.CENTER)
            # label.set_halign(Gtk.Align.END)
            # add the label to the window
            print("The text of the label is as follows :",label.get_label())
            print("The angle of the label is as follows :",label.get_angle())
            # print("The  halin of the label is as follows :",label.get_halin())    ### This is not working ------
            self.add(label)

            # Instead of using getters and setters you can also get and set the properties with 
            # get_property("prop-name") and set_property("prop-name", value), respectively.

class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win1 = MyWindow(self,"image")
        win1.show_all()
        win2 = MyWindow(self,"label")
        win2.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)