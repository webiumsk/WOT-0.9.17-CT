# 2016.11.19 19:59:25 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/idlelib/WidgetRedirector.py
from Tkinter import *

class WidgetRedirector:
    """Support for redirecting arbitrary widget subcommands.
    
    Some Tk operations don't normally pass through Tkinter.  For example, if a
    character is inserted into a Text widget by pressing a key, a default Tk
    binding to the widget's 'insert' operation is activated, and the Tk library
    processes the insert without calling back into Tkinter.
    
    Although a binding to <Key> could be made via Tkinter, what we really want
    to do is to hook the Tk 'insert' operation itself.
    
    When a widget is instantiated, a Tcl command is created whose name is the
    same as the pathname widget._w.  This command is used to invoke the various
    widget operations, e.g. insert (for a Text widget). We are going to hook
    this command and provide a facility ('register') to intercept the widget
    operation.
    
    In IDLE, the function being registered provides access to the top of a
    Percolator chain.  At the bottom of the chain is a call to the original
    Tk widget operation.
    
    """

    def __init__(self, widget):
        self._operations = {}
        self.widget = widget
        self.tk = tk = widget.tk
        w = widget._w
        self.orig = w + '_orig'
        tk.call('rename', w, self.orig)
        tk.createcommand(w, self.dispatch)

    def __repr__(self):
        return 'WidgetRedirector(%s<%s>)' % (self.widget.__class__.__name__, self.widget._w)

    def close(self):
        for operation in list(self._operations):
            self.unregister(operation)

        widget = self.widget
        del self.widget
        orig = self.orig
        del self.orig
        tk = widget.tk
        w = widget._w
        tk.deletecommand(w)
        tk.call('rename', orig, w)

    def register(self, operation, function):
        self._operations[operation] = function
        setattr(self.widget, operation, function)
        return OriginalCommand(self, operation)

    def unregister(self, operation):
        if operation in self._operations:
            function = self._operations[operation]
            del self._operations[operation]
            if hasattr(self.widget, operation):
                delattr(self.widget, operation)
            return function
        else:
            return None
            return None

    def dispatch(self, operation, *args):
        """Callback from Tcl which runs when the widget is referenced.
        
        If an operation has been registered in self._operations, apply the
        associated function to the args passed into Tcl. Otherwise, pass the
        operation through to Tk via the original Tcl function.
        
        Note that if a registered function is called, the operation is not
        passed through to Tk.  Apply the function returned by self.register()
        to *args to accomplish that.  For an example, see ColorDelegator.py.
        
        """
        m = self._operations.get(operation)
        try:
            if m:
                return m(*args)
            return self.tk.call((self.orig, operation) + args)
        except TclError:
            return ''


class OriginalCommand:

    def __init__(self, redir, operation):
        self.redir = redir
        self.operation = operation
        self.tk = redir.tk
        self.orig = redir.orig
        self.tk_call = self.tk.call
        self.orig_and_operation = (self.orig, self.operation)

    def __repr__(self):
        return 'OriginalCommand(%r, %r)' % (self.redir, self.operation)

    def __call__(self, *args):
        return self.tk_call(self.orig_and_operation + args)


def main():
    global previous_tcl_fcn
    root = Tk()
    root.wm_protocol('WM_DELETE_WINDOW', root.quit)
    text = Text()
    text.pack()
    text.focus_set()
    redir = WidgetRedirector(text)

    def my_insert(*args):
        print 'insert', args
        previous_tcl_fcn(*args)

    previous_tcl_fcn = redir.register('insert', my_insert)
    root.mainloop()
    redir.unregister('insert')
    redir.close()
    root.mainloop()
    root.destroy()


if __name__ == '__main__':
    main()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\Lib\idlelib\WidgetRedirector.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:59:25 St�edn� Evropa (b�n� �as)
