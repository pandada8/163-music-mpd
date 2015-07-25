from urwid import *

class CustomListWalker(SimpleFocusListWalker):

    def __getitem__(self, position):
        content = super(CustomListWalker, self).__getitem__(position)
        if self.focus != position:
            return AttrMap(Text(str(content)), "text", 'text_focus')
        else:
            return AttrMap(Text("> "+str(content)), "text", 'text_focus')


class Application():

    palette = [
        ('status', '', '', '', "g42", ''),
        ('text', 'light gray', '', '', '', ''),
        ('text_focus', "white, bold", 'black', )
    ]

    def __init__(self):
        self.status = Text('♫  ♪ ♫  ♪  Play ksdjflkasjd;flja;sl')
        # TODO using attrmap subclass to change color
        # TODO control this by cli config
        self.current_list = CustomListWalker(["Song", "Song2", "Song3"])
        self.layout = Frame(AttrMap(ListBox(self.current_list), 'text'), footer=AttrMap(self.status, 'status'), )
        self.screen = raw_display.Screen()
        self.screen.set_terminal_properties(256)
        self.event_loop = MainLoop(ListBox(self.current_list), self.palette, screen=self.screen, unhandled_input=self.unhandled_input)

    def run(self):
        self.event_loop.run()

    def unhandled_input(self, key):
        if key in ('Q', 'q'):
            self.quit()
        if key in ('down', 'j'):
            self._next_item()

    def _next_item(self):
        # self.current_list.positions
        self.current_list.set_focus()

    def quit(self):
        # do some stuff
        self.status.set_text('quiting...')
        raise ExitMainLoop()

app = Application()
