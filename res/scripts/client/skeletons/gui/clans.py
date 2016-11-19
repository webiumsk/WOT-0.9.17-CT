# 2016.11.19 19:54:28 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/skeletons/gui/clans.py


class IClanController(object):

    def addListener(self, listener):
        raise NotImplementedError

    def removeListener(self, listener):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def invalidate(self):
        raise NotImplementedError

    def getClanDossier(self, clanDbID = None):
        raise NotImplementedError

    def resyncLogin(self, forceLogin = False):
        raise NotImplementedError

    def sendRequest(self, ctx, callback = None, allowDelay = None):
        raise NotImplementedError

    def getStateID(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def isAvailable(self):
        raise NotImplementedError

    def getWebRequester(self):
        raise NotImplementedError

    def getAccountProfile(self):
        raise NotImplementedError

    def getLimits(self):
        raise NotImplementedError

    def getClanDbID(self):
        raise NotImplementedError

    def changeState(self, state):
        raise NotImplementedError

    def onStateUpdated(self):
        raise NotImplementedError

    def isLoggedOn(self):
        raise NotImplementedError

    def updateClanCommonDataCache(self, cache):
        raise NotImplementedError

    def clearClanCommonDataCache(self):
        raise NotImplementedError

    def getClanCommonData(self, clanDbID):
        raise NotImplementedError

    def requestUsers(self, dbIDs, callback):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\skeletons\gui\clans.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:54:28 St�edn� Evropa (b�n� �as)