# 2016.11.19 19:49:10 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/random/pre_queue/ctx.py
from constants import QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx
from gui.shared.utils.decorators import ReprInjector

@ReprInjector.withParent(('getVehicleInventoryID', 'vInvID'), ('getGamePlayMask', 'gamePlayMask'), ('getWaitingID', 'waitingID'))

class RandomQueueCtx(QueueCtx):
    """
    Enqueue random request context
    """

    def __init__(self, vInventoryID, arenaTypeID = 0, gamePlayMask = 0, waitingID = ''):
        super(RandomQueueCtx, self).__init__(entityType=QUEUE_TYPE.RANDOMS, waitingID=waitingID)
        self.__vInventoryID = vInventoryID
        self.__arenaTypeID = arenaTypeID
        self.__gamePlayMask = gamePlayMask

    def getVehicleInventoryID(self):
        """
        Gets selected vehicle inventory ID
        """
        return self.__vInventoryID

    def getDemoArenaTypeID(self):
        """
        Gets map arena type ID
        """
        return self.__arenaTypeID

    def getGamePlayMask(self):
        """
        Gets selected mode mask
        """
        return self.__gamePlayMask
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\entities\random\pre_queue\ctx.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:49:10 St�edn� Evropa (b�n� �as)
