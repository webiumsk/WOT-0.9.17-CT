# 2016.11.19 20:01:07 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/plat-mac/lib-scriptpackages/Terminal/Text_Suite.py
"""Suite Text Suite: A set of basic classes for text processing.
Level 1, version 1

Generated from /Applications/Utilities/Terminal.app
AETE/AEUT resource version 1/0, language 0, script 0
"""
import aetools
import MacOS
_code = '????'

class Text_Suite_Events:
    pass


class attachment(aetools.ComponentItem):
    """attachment - Represents an inline text attachment.  This class is used mainly for make commands. """
    want = 'atts'


class _Prop__3c_Inheritance_3e_(aetools.NProperty):
    """<Inheritance> - All of the properties of the superclass. """
    which = 'c@#^'
    want = 'ctxt'


class _Prop_file_name(aetools.NProperty):
    """file name - The path to the file for the attachment """
    which = 'atfn'
    want = 'utxt'


class attribute_run(aetools.ComponentItem):
    """attribute run - This subdivides the text into chunks that all have the same attributes. """
    want = 'catr'


class _Prop_color(aetools.NProperty):
    """color - The color of the first character. """
    which = 'colr'
    want = 'colr'


class _Prop_font(aetools.NProperty):
    """font - The name of the font of the first character. """
    which = 'font'
    want = 'utxt'


class _Prop_size(aetools.NProperty):
    """size - The size in points of the first character. """
    which = 'ptsz'
    want = 'long'


attribute_runs = attribute_run

class character(aetools.ComponentItem):
    """character - This subdivides the text into characters. """
    want = 'cha '


characters = character

class paragraph(aetools.ComponentItem):
    """paragraph - This subdivides the text into paragraphs. """
    want = 'cpar'


paragraphs = paragraph

class text(aetools.ComponentItem):
    """text - Rich (styled) text """
    want = 'ctxt'


class word(aetools.ComponentItem):
    """word - This subdivides the text into words. """
    want = 'cwor'


words = word
attachment._superclassnames = ['text']
attachment._privpropdict = {'_3c_Inheritance_3e_': _Prop__3c_Inheritance_3e_,
 'file_name': _Prop_file_name}
attachment._privelemdict = {'attribute_run': attribute_run,
 'character': character,
 'paragraph': paragraph,
 'word': word}
import Standard_Suite
attribute_run._superclassnames = ['item']
attribute_run._privpropdict = {'_3c_Inheritance_3e_': _Prop__3c_Inheritance_3e_,
 'color': _Prop_color,
 'font': _Prop_font,
 'size': _Prop_size}
attribute_run._privelemdict = {'attribute_run': attribute_run,
 'character': character,
 'paragraph': paragraph,
 'word': word}
character._superclassnames = ['item']
character._privpropdict = {'_3c_Inheritance_3e_': _Prop__3c_Inheritance_3e_,
 'color': _Prop_color,
 'font': _Prop_font,
 'size': _Prop_size}
character._privelemdict = {'attribute_run': attribute_run,
 'character': character,
 'paragraph': paragraph,
 'word': word}
paragraph._superclassnames = ['item']
paragraph._privpropdict = {'_3c_Inheritance_3e_': _Prop__3c_Inheritance_3e_,
 'color': _Prop_color,
 'font': _Prop_font,
 'size': _Prop_size}
paragraph._privelemdict = {'attribute_run': attribute_run,
 'character': character,
 'paragraph': paragraph,
 'word': word}
text._superclassnames = ['item']
text._privpropdict = {'_3c_Inheritance_3e_': _Prop__3c_Inheritance_3e_,
 'color': _Prop_color,
 'font': _Prop_font,
 'size': _Prop_size}
text._privelemdict = {'attribute_run': attribute_run,
 'character': character,
 'paragraph': paragraph,
 'word': word}
word._superclassnames = ['item']
word._privpropdict = {'_3c_Inheritance_3e_': _Prop__3c_Inheritance_3e_,
 'color': _Prop_color,
 'font': _Prop_font,
 'size': _Prop_size}
word._privelemdict = {'attribute_run': attribute_run,
 'character': character,
 'paragraph': paragraph,
 'word': word}
_classdeclarations = {'atts': attachment,
 'catr': attribute_run,
 'cha ': character,
 'cpar': paragraph,
 'ctxt': text,
 'cwor': word}
_propdeclarations = {'atfn': _Prop_file_name,
 'c@#^': _Prop__3c_Inheritance_3e_,
 'colr': _Prop_color,
 'font': _Prop_font,
 'ptsz': _Prop_size}
_compdeclarations = {}
_enumdeclarations = {}
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\Lib\plat-mac\lib-scriptpackages\Terminal\Text_Suite.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 20:01:08 St�edn� Evropa (b�n� �as)
