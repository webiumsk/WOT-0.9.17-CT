# 2016.11.19 19:55:38 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/dossiers2/custom/clan_layout.py
from dossiers2.common.DossierBlockBuilders import *
_rareAchievementsBlockBuilder = ListBlockBuilder('rareAchievements', 'I', {})
clanDossierLayout = (_rareAchievementsBlockBuilder,)
CLAN_DOSSIER_LIST_BLOCKS = [ b.name for b in clanDossierLayout if type(b) == ListBlockBuilder ]
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\dossiers2\custom\clan_layout.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:55:38 St�edn� Evropa (b�n� �as)
