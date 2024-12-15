import sys
import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, Gdk, GLib
from gtts import gTTS
import wikipedia



UI_FILE = "/home/fran/Documentos/textoavoz.ui"


class GUI:
    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)

        self.builder.connect_signals(self)
        window = self.builder.get_object('window1')

        window.show_all()


    def on_window1_destroy(self, window):
        Gtk.main_quit()

    
    def on_button1_clicked(self, button):
        cajadetexto = self.builder.get_object("entry1")
        palabra = cajadetexto.get_text()
        wikipedia.set_lang("es")
        res= wikipedia.summary(palabra, sentences=1)  
        tts = gTTS(res, lang="es", slow=False)
        tts.save('palabra.mp3')
        os.system('mpg123 palabra.mp3')

def main():
    app = GUI()
    Gtk.main()


if __name__ == "__main__":
    sys.exit(main())
