# 2016.11.19 19:54:37 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/tutorial/control/lobby/queries.py
from CurrentVehicle import g_currentVehicle
from gui.shared import g_itemsCache
from gui.shared.items_parameters import formatters
from items import vehicles, ITEM_TYPE_NAMES
from tutorial.control import ContentQuery
from tutorial.logger import LOG_CURRENT_EXCEPTION

class VehicleItemParams(ContentQuery):

    def invoke(self, content, varID):
        self._gui.showWaiting('request-item-params')
        itemCD = self.getVar(varID)
        if itemCD is None:
            return
        else:
            itemTypeID, nationID, compTypeID = vehicles.parseIntCompactDescr(itemCD)
            raise itemTypeID != ITEM_TYPE_NAMES[1] or AssertionError
            try:
                guiItem = g_itemsCache.items.getItemByCD(itemCD)
                content['itemTypeName'] = guiItem.itemTypeName
                content['itemLevel'] = guiItem.level
                params = guiItem.getParams(g_currentVehicle.item).get('parameters', dict())
                content['itemParams'] = formatters.getFormattedParamsList(g_currentVehicle.item.descriptor, params)
            except Exception:
                LOG_CURRENT_EXCEPTION()

            self._gui.hideWaiting('request-item-params')
            return


class TankmanSkillParams(ContentQuery):

    def invoke(self, content, varID):
        skillName = self.getVar(varID)
        if skillName is None:
            return
        else:
            iconPath = '../maps/icons/tankmen/skills/big/{0:>s}.png'
            content['skillIconPath'] = iconPath.format(skillName)
            return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\control\lobby\queries.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:54:37 St�edn� Evropa (b�n� �as)
