# 2016.11.19 19:51:18 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CyberSportRespawnFormMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyRoomView import BaseRallyRoomView

class CyberSportRespawnFormMeta(BaseRallyRoomView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyRoomView
    """

    def as_updateEnemyStatusS(self, statusID, enemyStatusLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEnemyStatus(statusID, enemyStatusLabel)

    def as_setTeamNameS(self, name):
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamName(name)

    def as_setTeamEmblemS(self, teamEmblemId):
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamEmblem(teamEmblemId)

    def as_setArenaTypeIdS(self, mapName, arenaTypeID):
        if self._isDAAPIInited():
            return self.flashObject.as_setArenaTypeId(mapName, arenaTypeID)

    def as_timerUpdateS(self, timeLeft):
        if self._isDAAPIInited():
            return self.flashObject.as_timerUpdate(timeLeft)

    def as_statusUpdateS(self, status, level, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_statusUpdate(status, level, tooltip)

    def as_setTotalLabelS(self, hasTotalLevelError, totalLevelLabel, totalLevel):
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalLabel(hasTotalLevelError, totalLevelLabel, totalLevel)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\CyberSportRespawnFormMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:18 St�edn� Evropa (b�n� �as)
