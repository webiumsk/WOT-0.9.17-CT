# 2016.11.19 19:52:21 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/managers/PopoverManager.py
from debug_utils import LOG_ERROR
from gui.Scaleform.framework import g_entitiesFactories
from gui.Scaleform.framework.entities.abstract.PopoverManagerMeta import PopoverManagerMeta
from gui.shared.events import HidePopoverEvent

class PopoverManager(PopoverManagerMeta):

    def __init__(self, scope):
        super(PopoverManager, self).__init__()
        self.__scope = scope
        self.addListener(HidePopoverEvent.POPOVER_DESTROYED, self.__handlerDestroyPopover)

    def requestShowPopover(self, alias, data):
        event = g_entitiesFactories.makeShowPopoverEvent(alias, {'data': data})
        if event is not None:
            self.fireEvent(event, scope=self.__scope)
        else:
            LOG_ERROR('Event of opening popover can not be created', alias)
        return

    def requestHidePopover(self):
        self.fireEvent(HidePopoverEvent(HidePopoverEvent.HIDE_POPOVER))

    def destroy(self):
        self.removeListener(HidePopoverEvent.POPOVER_DESTROYED, self.__handlerDestroyPopover)
        super(PopoverManager, self).destroy()

    def __handlerDestroyPopover(self, _):
        self.as_onPopoverDestroyS()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\managers\PopoverManager.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:52:21 St�edn� Evropa (b�n� �as)
