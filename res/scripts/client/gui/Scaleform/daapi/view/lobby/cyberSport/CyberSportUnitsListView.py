# 2016.11.19 19:50:13 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/cyberSport/CyberSportUnitsListView.py
from functools import partial
from UnitBase import UNIT_BROWSER_TYPE
from adisp import process
from constants import PREBATTLE_TYPE
from gui.Scaleform.daapi.view.lobby.rally.rally_dps import ManualSearchDataProvider
from gui.Scaleform.daapi.view.meta.CyberSportUnitsListMeta import CyberSportUnitsListMeta
from gui.Scaleform.genConsts.CYBER_SPORT_ALIASES import CYBER_SPORT_ALIASES
from gui.Scaleform.locale.CYBERSPORT import CYBERSPORT
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.clubs import events_dispatcher as club_events
from gui.clubs.club_helpers import ClubListener
from gui.clubs.settings import getLadderChevron64x64, CLIENT_CLUB_STATE
from gui.prb_control.settings import REQUEST_TYPE
from gui.shared import events
from gui.shared.formatters import text_styles
from gui.shared.view_helpers import ClubEmblemsHelper, CooldownHelper
from helpers import int2roman
from helpers.i18n import makeString as _ms

class CyberSportUnitsListView(CyberSportUnitsListMeta, ClubListener, ClubEmblemsHelper):

    def __init__(self):
        super(CyberSportUnitsListView, self).__init__()
        self._unitTypeFlags = UNIT_BROWSER_TYPE.ALL
        self._cooldown = CooldownHelper(self.getCoolDownRequests(), self._onCooldownHandle, events.CoolDownEvent.PREBATTLE)
        self.__currentEmblem = None
        return

    def getPyDataProvider(self):
        return ManualSearchDataProvider()

    def getCoolDownRequests(self):
        return [REQUEST_TYPE.UNITS_LIST]

    def setTeamFilters(self, showOnlyStatic):
        self._unitTypeFlags = UNIT_BROWSER_TYPE.RATED_CLUBS if showOnlyStatic else UNIT_BROWSER_TYPE.ALL
        self.__recenterList()

    def loadPrevious(self):
        listReq = self.prbEntity.getBrowser()
        if listReq:
            listReq.request(req=REQUEST_TYPE.UNITS_NAV_LEFT)

    def loadNext(self):
        listReq = self.prbEntity.getBrowser()
        if listReq:
            listReq.request(req=REQUEST_TYPE.UNITS_NAV_RIGHT)

    def refreshTeams(self):
        listReq = self.prbEntity.getBrowser()
        if listReq:
            listReq.request(req=REQUEST_TYPE.UNITS_REFRESH)

    def getRallyDetails(self, index):
        if index != self._searchDP.selectedRallyIndex:
            self.__currentEmblem = None
        cfdUnitID, vo = self._searchDP.getRally(index)
        listReq = self.prbEntity.getBrowser()
        if listReq:
            listReq.setSelectedID(cfdUnitID)
        self.__setDetailsData(cfdUnitID, vo)
        return

    def showRallyProfile(self, clubDBID):
        club_events.showClubProfile(clubDBID)

    def onPrbEntitySwitching(self):
        browser = self.prbEntity.getBrowser()
        if browser:
            browser.stop()

    def _populate(self):
        super(CyberSportUnitsListView, self)._populate()
        self._cooldown.start()
        self.prbEntity.getBrowser().start(self.__onUnitsListUpdated)
        self.as_setSearchResultTextS(_ms(CYBERSPORT.WINDOW_UNITLISTVIEW_FOUNDTEAMS), '', self.__getFiltersData())
        headerDescription = CYBERSPORT.WINDOW_UNITLISTVIEW_DESCRIPTION
        headerTitle = CYBERSPORT.WINDOW_UNITLISTVIEW_TITLE
        self.as_setHeaderS({'title': headerTitle,
         'description': headerDescription,
         'createBtnLabel': CYBERSPORT.WINDOW_UNITLISTVIEW_CREATE_BTN,
         'createBtnTooltip': None,
         'createBtnEnabled': True,
         'columnHeaders': self.__getColumnHeaders()})
        return

    def _dispose(self):
        self._cooldown.stop()
        self._cooldown = None
        super(CyberSportUnitsListView, self)._dispose()
        return

    def _onUserActionReceived(self, _, user):
        self.__updateView(user)

    def _doEnableNavButtons(self, isEnabled):
        self.as_updateNavigationBlockS({'previousVisible': True,
         'previousEnabled': isEnabled,
         'nextVisible': True,
         'nextEnabled': isEnabled,
         'icon': RES_ICONS.MAPS_ICONS_STATISTIC_RATING24})

    def _onCooldownHandle(self, isInCooldown):
        self._doEnableNavButtons(not isInCooldown)

    def __getColumnHeaders(self):
        return [self.__createHedader('', 54, RES_ICONS.MAPS_ICONS_LIBRARY_CYBERSPORT_LADDERICON),
         self.__createHedader('', 58, RES_ICONS.MAPS_ICONS_STATISTIC_RATING24),
         self.__createHedader(CYBERSPORT.WINDOW_UNIT_UNITLISTVIEW_COMMANDER, 152),
         self.__createHedader(CYBERSPORT.WINDOW_UNIT_UNITLISTVIEW_DESCRIPTION, 220),
         self.__createHedader(CYBERSPORT.WINDOW_UNIT_UNITLISTVIEW_PLAYERS, 76)]

    def __createHedader(self, label, buttonWidth, iconSource = None):
        return {'label': label,
         'buttonWidth': buttonWidth,
         'iconSource': iconSource,
         'enabled': False}

    def __updateVehicleLabel(self):
        settings = self.prbEntity.getRosterSettings()
        self._updateVehiclesLabel(int2roman(settings.getMinLevel()), int2roman(settings.getMaxLevel()))

    def __getFiltersData(self):
        return {'isSelected': self._unitTypeFlags == UNIT_BROWSER_TYPE.RATED_CLUBS,
         'icon': RES_ICONS.MAPS_ICONS_LIBRARY_CYBERSPORT_RANKEDICON,
         'label': _ms(CYBERSPORT.WINDOW_UNITLISTVIEW_FOUNDTEAMS_FILTERTEXT)}

    def __onUnitsListUpdated(self, selectedID, isFullUpdate, isReqInCoolDown, units):
        if isFullUpdate:
            selectedIdx = self._searchDP.rebuildList(selectedID, units)
            self._doEnableNavButtons(not isReqInCoolDown)
        else:
            selectedIdx = self._searchDP.updateList(selectedID, units)
        if selectedIdx is not None:
            self.as_selectByIndexS(selectedIdx)
        return

    def __setDetailsData(self, unitID, vo):
        _, unit = self.prbEntity.getUnit(unitID)
        if unit is not None and unit.isClub():
            self.__setDetails(unitID, vo, unit.getExtra())
        else:
            self.__setDetails(unitID, vo)
        return

    def __setDetails(self, unitID, vo, clubExtraData = None):
        if clubExtraData is not None:
            linkage = CYBER_SPORT_ALIASES.COMMNAD_DETAILS_LINKAGE_JOIN_TO_STATIC_AS_LEGIONARY
            icon = None
            name = clubExtraData.clubName
            clubID = clubExtraData.clubDBID
            division = clubExtraData.divisionID
            description = vo['description']
            if self.__currentEmblem is None:
                self.requestClubEmblem64x64(clubID, clubExtraData.getEmblem64x64(), partial(self.__onClubEmblem64x64Received, unitID))
            else:
                icon = self.__currentEmblem
            buttonLabel = CYBERSPORT.WINDOW_UNITLISTVIEW_ENTERBTN_LEGIONARY
            buttonInfo = CYBERSPORT.WINDOW_UNITLISTVIEW_ENTERTEXT_LEGIONARY
            buttonTooltip = TOOLTIPS.CYBERSPORT_UNITLIST_JOINTOSTATICASLEGIONARY
            if self.clubsState.getStateID() == CLIENT_CLUB_STATE.HAS_CLUB and self.clubsState.getClubDbID() == clubID:
                buttonLabel = CYBERSPORT.WINDOW_UNITLISTVIEW_ENTERBTN_MEMBER
                buttonInfo = CYBERSPORT.WINDOW_UNITLISTVIEW_ENTERTEXT_MEMBER
                buttonTooltip = None
            vo.update({'joinBtnLabel': buttonLabel,
             'joinInfo': text_styles.standard(_ms(buttonInfo)),
             'joinBtnTooltip': buttonTooltip,
             'rallyInfo': {'icon': icon,
                           'name': text_styles.highTitle(name),
                           'profileBtnLabel': CYBERSPORT.RALLYINFO_PROFILEBTN_LABEL,
                           'profileBtnTooltip': TOOLTIPS.RALLYINFO_PROFILEBTN,
                           'description': text_styles.main(description),
                           'ladderIcon': getLadderChevron64x64(division),
                           'id': clubID,
                           'showLadder': True}})
            self.as_setDetailsS({'viewLinkage': linkage,
             'data': vo})
        else:
            linkage = CYBER_SPORT_ALIASES.COMMNAD_DETAILS_LINKAGE_JOIN_TO_NONSTATIC
            self.as_setDetailsS({'viewLinkage': linkage,
             'data': vo})
        self.__updateVehicleLabel()
        return

    def __refreshDetails(self, idx):
        cfdUnitID, vo = self._searchDP.getRally(idx)
        self.__setDetailsData(cfdUnitID, vo)

    def __updateView(self, user):
        self._searchDP.updateListItem(user.getID())
        self.__refreshDetails(self._searchDP.selectedRallyIndex)

    def __recenterList(self):
        listReq = self.prbEntity.getBrowser()
        if listReq:
            listReq.request(req=REQUEST_TYPE.UNITS_RECENTER, unitTypeFlags=self._unitTypeFlags)

    def __onClubEmblem64x64Received(self, cfdUnitID, clubDbID, emblem):
        selectedCfdUnitID, _ = self._searchDP.getRally(self._searchDP.selectedRallyIndex)
        if emblem and cfdUnitID == selectedCfdUnitID:
            self.__currentEmblem = self.getMemoryTexturePath(emblem)
            self.as_updateRallyIconS(self.__currentEmblem)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\lobby\cyberSport\CyberSportUnitsListView.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:50:13 St�edn� Evropa (b�n� �as)
