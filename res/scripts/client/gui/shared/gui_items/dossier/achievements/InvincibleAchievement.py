# 2016.11.19 19:52:49 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/InvincibleAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SeriesAchievement

class InvincibleAchievement(SeriesAchievement):

    def __init__(self, dossier, value = None):
        super(InvincibleAchievement, self).__init__('invincible', _AB.SINGLE, dossier, value)

    def _getCounterRecordNames(self):
        return ((_AB.TOTAL, 'invincibleSeries'), (_AB.TOTAL, 'maxInvincibleSeries'))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\InvincibleAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:52:50 St�edn� Evropa (b�n� �as)
