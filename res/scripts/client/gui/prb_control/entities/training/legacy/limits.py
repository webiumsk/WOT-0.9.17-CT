# 2016.11.19 19:49:13 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/prb_control/entities/training/legacy/limits.py
from constants import PREBATTLE_ACCOUNT_STATE, PREBATTLE_TYPE
from gui.prb_control.entities.base.limits import AbstractTeamIsValid, LimitsCollection, VehicleIsValid, TeamNoPlayersInBattle, TeamIsValid
from gui.shared import g_itemsCache
from items import vehicles

class ObserverInTeamIsValid(AbstractTeamIsValid):
    """
    Observer's team limits
    """

    def check(self, rosters, team, teamLimits):
        accountsInfo = self._getAccountsInfo(rosters, team)
        if len(accountsInfo) < teamLimits['minCount']:
            return (False, 'limit/minCount')
        if self.__isAllObservers(accountsInfo):
            return (False, 'observers')
        return (True, '')

    @classmethod
    def __isAllObservers(cls, accountsInfo):
        """
        Checks are all players in team observers
        Args:
            accountsInfo: players accounts info
        """
        if not len(accountsInfo):
            return False
        for accInfo in accountsInfo.itervalues():
            if not accInfo['state'] & PREBATTLE_ACCOUNT_STATE.READY:
                continue
            if 'vehTypeCompDescr' not in accInfo or 'vehLevel' not in accInfo:
                vehDescr = vehicles.VehicleDescr(compactDescr=accInfo['vehCompDescr'])
                vehTypeCompDescr = vehDescr.type.compactDescr
            else:
                vehTypeCompDescr = accInfo['vehTypeCompDescr']
            if not g_itemsCache.items.getItemByCD(vehTypeCompDescr).isObserver:
                return False

        return True


class TrainingLimits(LimitsCollection):
    """
    Training limits class
    """

    def __init__(self, entity):
        super(TrainingLimits, self).__init__(entity, (VehicleIsValid(),), (TeamNoPlayersInBattle(PREBATTLE_TYPE.TRAINING), TeamIsValid(), ObserverInTeamIsValid()))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\entities\training\legacy\limits.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:49:13 St�edn� Evropa (b�n� �as)
