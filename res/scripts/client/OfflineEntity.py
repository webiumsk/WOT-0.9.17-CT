# 2016.11.19 19:47:07 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/OfflineEntity.py
import BigWorld

class OfflineEntity(BigWorld.Entity):

    def __init__(self):
        pass

    def prerequisites(self):
        return []

    def onEnterWorld(self, prereqs):
        pass

    def onLeaveWorld(self):
        pass

    def collideSegment(self, startPoint, endPoint, skipGun = False):
        pass


class PlayerOfflineEntity(BigWorld.Entity):

    def __init__(self):
        pass

    def prerequisites(self):
        return []

    def onEnterWorld(self, prereqs):
        pass

    def onLeaveWorld(self):
        pass

    def handleKeyEvent(self, event):
        return False
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\OfflineEntity.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:47:07 St�edn� Evropa (b�n� �as)
