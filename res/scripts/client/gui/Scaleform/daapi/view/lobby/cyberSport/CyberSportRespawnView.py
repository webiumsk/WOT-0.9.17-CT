# 2016.11.19 19:50:13 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/cyberSport/CyberSportRespawnView.py
from constants import PREBATTLE_TYPE
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.CyberSportRespawnViewMeta import CyberSportRespawnViewMeta
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES
from gui.prb_control.entities.base.unit.listener import IUnitListener
from gui.shared.utils.functions import getArenaGeomentryName
from messenger.ext import channel_num_gen
from messenger.gui import events_dispatcher
from messenger.gui.Scaleform.view.lobby import MESSENGER_VIEW_ALIAS

class CyberSportRespawnView(CyberSportRespawnViewMeta, LobbySubView, IUnitListener):
    __background_alpha__ = 1.0
    MAP_BG_SOURCE = '../maps/icons/map/screen/%s.dds'

    def __init__(self, ctx = None):
        CyberSportRespawnViewMeta.__init__(self)
        LobbySubView.__init__(self)
        self.currentState = ''

    def onUnitRejoin(self):
        if not self.prbEntity.getFlags().isInIdle():
            self.__clearState()

    def onUnitFlagsChanged(self, flags, timeLeft):
        if self.prbEntity.hasLockedState():
            if flags.isInQueue() or flags.isInArena():
                self.currentState = CYBER_SPORT_ALIASES.AUTO_SEARCH_ENEMY_RESPAWN_STATE
            elif flags.isInPreArena():
                self.__clearState()
            else:
                LOG_ERROR('View for modal state is not resolved', flags)
            self.__initState(timeLeft=timeLeft)
        else:
            self.__clearState()

    def onUnitPlayerStateChanged(self, pInfo):
        if self.prbEntity.getFlags().isInIdle():
            self.__initState()

    def onUnitExtraChanged(self, extra):
        extra = self.prbEntity.getExtra()
        self.__swapTeamsInMinimap(extra.isBaseDefence)

    def _populate(self):
        super(CyberSportRespawnView, self)._populate()
        self.startPrbListening()
        extra = self.prbEntity.getExtra()
        if extra is not None:
            geometryName = getArenaGeomentryName(extra.mapID)
            self.as_setMapBGS(self.MAP_BG_SOURCE % geometryName)
            self.__swapTeamsInMinimap(extra.isBaseDefence)
        else:
            LOG_ERROR('No extra data was give for club unit: ', self.prbEntity.getUnit())
        return

    def _dispose(self):
        self.stopPrbListening()
        super(CyberSportRespawnView, self)._dispose()

    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT:
            events_dispatcher.rqActivateChannel(self.getClientID(), viewPy)
            return
        super(CyberSportRespawnViewMeta, self)._onRegisterFlashComponent(viewPy, alias)

    def _onUnregisterFlashComponent(self, viewPy, alias):
        if alias == MESSENGER_VIEW_ALIAS.CHANNEL_COMPONENT:
            events_dispatcher.rqDeactivateChannel(self.getClientID())
        super(CyberSportRespawnViewMeta, self)._onUnregisterFlashComponent(viewPy, alias)

    def getPrbType(self):
        return PREBATTLE_TYPE.UNIT

    def getClientID(self):
        return channel_num_gen.getClientID4Prebattle(self.getPrbType())

    def __initState(self, timeLeft = 0, acceptDelta = 0):
        model = None
        if self.currentState == CYBER_SPORT_ALIASES.AUTO_SEARCH_ENEMY_RESPAWN_STATE:
            model = self.__createAutoUpdateModel(self.currentState, timeLeft, '', [])
        if model is not None:
            self.as_changeAutoSearchStateS(model)
        return

    def __clearState(self):
        self.currentState = ''
        self.as_hideAutoSearchS()

    def __createAutoUpdateModel(self, state, countDownSeconds, ctxMessage, playersReadiness):
        permissions = self.prbEntity.getPermissions(unitIdx=self.prbEntity.getUnitIdx())
        model = {'state': state,
         'countDownSeconds': countDownSeconds,
         'contextMessage': ctxMessage,
         'playersReadiness': playersReadiness,
         'canInvokeAutoSearch': permissions.canInvokeAutoSearch(),
         'canInvokeBattleQueue': permissions.canStopBattleQueue()}
        return model

    def __swapTeamsInMinimap(self, isDefence):
        if VIEW_ALIAS.MINIMAP_LOBBY in self.components:
            self.components[VIEW_ALIAS.MINIMAP_LOBBY].swapTeams(1 if isDefence else 2)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\lobby\cyberSport\CyberSportRespawnView.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:50:13 St�edn� Evropa (b�n� �as)
