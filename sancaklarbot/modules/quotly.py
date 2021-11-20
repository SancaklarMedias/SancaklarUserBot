# Copyright (C) 2020-2021 SancaklarMedias <https://github.com/SancaklarMedias>
#
# This file is part of SancaklarMedias project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from time import sleep

from pyrogram.errors import YouBlockedUser
from sancaklarbot import HELP
from sancaklarmedias.core import PyroConversation, edit, get_translation, sancaklarify


@sancaklarify(pattern='^.q$', compat=False)
def quotly(client, message):
    reply = message.reply_to_message
    if reply and (reply.text or reply.photo or reply.sticker):
        edit(message, f'`{get_translation("makeQuote")}`')
    else:
        edit(message, f'`{get_translation("replyMessage")}`')
        return

    sleep(1)
    chat = 'QuotLyBot'

    with PyroConversation(client, chat) as conv:
        response = None
        try:
            conv.forward_msg(reply)
            response = conv.recv_msg()
        except YouBlockedUser:
            edit(message, get_translation('unblockChat', ['**', '`', chat]))
            return
        except Exception:

            if not response:
                edit(message, f'`{get_translation("answerFromBot")}`')
                return

        response.forward(message.chat.id)

    message.delete()


HELP.update({'quotly': get_translation('quotlyInfo')})
