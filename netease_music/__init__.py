from urwid import *

class CustomListWalker(ListWalker):
    def __init__(self, data):
        self.data = data
        self.focus = 0

    def __getitem__(self, position):
        if position < 15:
            return Text(str(position))
        else:
            raise KeyError
    def next_position(self, position):
        return position + 1

    def prev_position(self, position):
        if position >= 0:
            return position - 1
        else:
            raise IndexError

    def set_focus(self, position):
        if 0 <= position < 15:
            self.focus = positon
        self._modified()


class Application():

    palette = [
        ('status', '', '', '', "g42", ''),
        ('text', 'white', '', '', '', '')
    ]

    def __init__(self):
        self.status = Text('♫  ♪ ♫  ♪  Play ksdjflkasjd;flja;sl')
        # TODO using attrmap subclass to change color
        # TODO control this by cli config
        self.current_list = CustomListWalker([1, 2,3,4,5,6])
        self.layout = Frame(AttrMap(ListBox(self.current_list), 'text'), footer=AttrMap(self.status, 'status'))
        self.screen = raw_display.Screen()
        self.screen.set_terminal_properties(256)
        self.event_loop = MainLoop(self.layout, self.palette, screen=self.screen, unhandled_input=self.unhandled_input)

    def run(self):
        self.event_loop.run()

    def unhandled_input(self, key):
        if key in ('Q', 'q'):
            self.quit()

    def quit(self):
        # do some stuff
        self.status.set_text('quiting...')
        raise ExitMainLoop()

app = Application()
