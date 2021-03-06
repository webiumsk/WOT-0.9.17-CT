# 2016.11.19 19:48:29 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/clubs/comparators.py
from collections import namedtuple
from debug_utils import LOG_DEBUG, LOG_CURRENT_EXCEPTION
from gui.clubs.interfaces import IClubValueComparator

class SimpleTypeComparator(namedtuple('SimpleTypeComparator', ['fieldName', 'eventName', 'changedArgsGetterName']), IClubValueComparator):

    def __call__(self, subscription, oldClub, newClub):
        try:
            if cmp(getattr(oldClub.getDescriptor(), self.fieldName), getattr(newClub.getDescriptor(), self.fieldName)):
                subscription.notify(self.eventName, getattr(newClub, self.changedArgsGetterName)())
        except:
            LOG_CURRENT_EXCEPTION()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\clubs\comparators.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:48:29 St�edn� Evropa (b�n� �as)
