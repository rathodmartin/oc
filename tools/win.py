#! /usr/bin/python

import pygtk
pygtk.require("2.0")
import gtk

class Base:
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.show()
		self.window.connect("destroy", self.destroy)
		
	def destroy(self, widget, data=None):
		print "You clicked the close button."
		gtk.main_quit()
	
	def main(self):
		gtk.main()
		
if __name__ == "__main__":
	base = Base()
	base.main()
	