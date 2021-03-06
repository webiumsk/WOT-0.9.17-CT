# 2016.11.19 19:59:53 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_dict.py
"""Fixer for dict methods.

d.keys() -> list(d.keys())
d.items() -> list(d.items())
d.values() -> list(d.values())

d.iterkeys() -> iter(d.keys())
d.iteritems() -> iter(d.items())
d.itervalues() -> iter(d.values())

d.viewkeys() -> d.keys()
d.viewitems() -> d.items()
d.viewvalues() -> d.values()

Except in certain very specific contexts: the iter() can be dropped
when the context is list(), sorted(), iter() or for...in; the list()
can be dropped when the context is list() or sorted() (but not iter()
or for...in!). Special contexts that apply to both: list(), sorted(), tuple()
set(), any(), all(), sum().

Note: iter(d.keys()) could be written as iter(d) but since the
original d.iterkeys() was also redundant we don't fix this.  And there
are (rare) contexts where it makes a difference (e.g. when passing it
as an argument to a function that introspects the argument).
"""
from .. import pytree
from .. import patcomp
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, LParen, RParen, ArgList, Dot
from .. import fixer_util
iter_exempt = fixer_util.consuming_calls | set(['iter'])

class FixDict(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< head=any+\n         trailer< '.' method=('keys'|'items'|'values'|\n                              'iterkeys'|'iteritems'|'itervalues'|\n                              'viewkeys'|'viewitems'|'viewvalues') >\n         parens=trailer< '(' ')' >\n         tail=any*\n    >\n    "

    def transform(self, node, results):
        head = results['head']
        method = results['method'][0]
        tail = results['tail']
        syms = self.syms
        method_name = method.value
        isiter = method_name.startswith(u'iter')
        isview = method_name.startswith(u'view')
        if isiter or isview:
            method_name = method_name[4:]
        if not method_name in (u'keys', u'items', u'values'):
            raise AssertionError(repr(method))
            head = [ n.clone() for n in head ]
            tail = [ n.clone() for n in tail ]
            special = not tail and self.in_special_context(node, isiter)
            args = head + [pytree.Node(syms.trailer, [Dot(), Name(method_name, prefix=method.prefix)]), results['parens'].clone()]
            new = pytree.Node(syms.power, args)
            if not (special or isview):
                new.prefix = u''
                new = Call(Name(u'iter' if isiter else u'list'), [new])
            new = tail and pytree.Node(syms.power, [new] + tail)
        new.prefix = node.prefix
        return new

    P1 = "power< func=NAME trailer< '(' node=any ')' > any* >"
    p1 = patcomp.compile_pattern(P1)
    P2 = "for_stmt< 'for' any 'in' node=any ':' any* >\n            | comp_for< 'for' any 'in' node=any any* >\n         "
    p2 = patcomp.compile_pattern(P2)

    def in_special_context(self, node, isiter):
        if node.parent is None:
            return False
        results = {}
        if node.parent.parent is not None and self.p1.match(node.parent.parent, results):
            if results['node'] is node:
                if isiter:
                    return results['func'].value in iter_exempt
                return results['func'].value in fixer_util.consuming_calls
        if not isiter:
            return False
        else:
            return self.p2.match(node.parent, results) and results['node'] is node
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\Lib\lib2to3\fixes\fix_dict.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:59:53 St�edn� Evropa (b�n� �as)
