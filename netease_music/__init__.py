from urwid import *
from datetime import datetime

class CustomListWalker(SimpleFocusListWalker):
    def __getitem__(self, position):
        content = super(CustomListWalker, self).__getitem__(position)
        if self.focus != position:
            return AttrMap(Text(str(content)), "text", 'text_focus')
        else:
            return AttrMap(Text("> "+str(content)), "text", 'text_focus')


# class VimableBox(ListBox):

#     def keypress(self, size, )


def log(s):
    with open('log.log', 'a') as fp:
        fp.write("[{}]:".format(datetime.now())+str(s)+"\n")


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
        # self.current_list = CustomListWalker(["Song", "Song2", "Song3"])
        self.current_list = SimpleListWalker([AttrMap(Text(i), 'text', 'text_focus')
            for i in "This"])
        self.list_box = ListBox(self.current_list)
        self.layout = Frame(AttrMap(self.list_box, 'text'), footer=AttrMap(self.status, 'status'), focus_part="body")
        self.screen = raw_display.Screen()
        self.screen.set_terminal_properties(256)
        self.event_loop = MainLoop(self.layout, self.palette, screen=self.screen, unhandled_input=self.unhandled_input)

    def run(self):
        self.event_loop.run()

    def unhandled_input(self, key):
        if key in ('Q', 'q'):
            self.quit()
        if key in ('down', 'j'):
            self._next_item()
        if key in ('up', 'k'):
            self._prev_item()


    def _next_item(self):
        _, current = self.current_list.get_focus()
        next_item = self.current_list.get_next(current)[1]
        if not next_item:
            next_item = 0
        self.current_list.set_focus(next_item)

    def _prev_item(self):
        _, current = self.current_list.get_focus()
        prev_item = self.current_list.get_prev(current)[1]
        if prev_item == None:
            prev_item = self.current_list.positions()[-1]
        self.current_list.set_focus(prev_item)


    def quit(self):
        # do some stuff
        self.status.set_text('quiting...')
        raise ExitMainLoop()

app = Application()
