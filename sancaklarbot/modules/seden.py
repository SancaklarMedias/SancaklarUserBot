# Copyright (C) 2020-2021 SancaklarMedias <https://github.com/SancaklarMedias>
#
# This file is part of SancaklarMedias project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from collections import OrderedDict

from sancaklarbot import HELP
from sancaklarmedias.core import edit, extract_args, get_translation, reply, sancaklarify


@sancaklarify(pattern='^.sancaklar')
def sancaklar(message):
    sancaklar = extract_args(message).lower()
    cmds = OrderedDict(sorted(HELP.items()))
    if len(sancaklar) > 0:
        if sancaklar in cmds:
            edit(message, str(cmds[sancaklar]))
        else:
            edit(message, f'**{get_translation("sancaklarUsage")}**')
    else:
        edit(message, get_translation('sancaklarUsage2', ['**', '`']))
        metin = f'{get_translation("sancaklarShowLoadedModules", ["**", "`", len(cmds)])}\n'
        for item in cmds:
            metin += f'• `{item}`\n'
        reply(message, metin)
