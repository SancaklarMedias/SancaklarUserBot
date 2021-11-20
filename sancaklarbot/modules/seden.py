# Copyright (C) 2020-2021 TeamDerUntergang <https://github.com/TeamDerUntergang>
#
# This file is part of TeamDerUntergang project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from collections import OrderedDict

from Sancaklarbot import HELP
from SancaklarMedias.core import edit, extract_args, get_translation, reply, Sancaklarify


@Sancaklarify(pattern='^.Sancaklar')
def Sancaklar(message):
    Sancaklar = extract_args(message).lower()
    cmds = OrderedDict(sorted(HELP.items()))
    if len(Sancaklar) > 0:
        if Sancaklar in cmds:
            edit(message, str(cmds[Sancaklar]))
        else:
            edit(message, f'**{get_translation("SancaklarUsage")}**')
    else:
        edit(message, get_translation('SancaklarUsage2', ['**', '`']))
        metin = f'{get_translation("SancaklarShowLoadedModules", ["**", "`", len(cmds)])}\n'
        for item in cmds:
            metin += f'• `{item}`\n'
        reply(message, metin)
