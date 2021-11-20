# Copyright (C) 2020-2021 TeamDerUntergang <https://github.com/TeamDerUntergang>
#
# This file is part of TeamDerUntergang project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from time import sleep

from Sancaklarbot import HELP, LOGS
from SancaklarMedias.core import edit, extract_args, get_translation, Sancaklarify, send_log


def chat_init():
    try:
        global sql
        from importlib import import_module

        sql = import_module('SancaklarMedias.sql.keep_read_sql')
    except Exception as e:
        sql = None
        LOGS.warn(get_translation('chatSqlLog'))
        raise e


chat_init()


@Sancaklarify(pattern='^.unmutechat$')
def unmutechat(message):
    try:
        from SancaklarMedias.sql.keep_read_sql import unkread
    except BaseException:
        edit(message, f'`{get_translation("nonSqlMode")}`')
        return
    status = unkread(str(message.chat.id))
    if status:
        edit(message, f'`{get_translation("chatUnmuted")}`')
    else:
        edit(message, f'`{get_translation("chatAlreadyUnmuted")}`')
    sleep(2)
    message.delete()


@Sancaklarify(pattern='^.mutechat$')
def mutechat(message):
    try:
        from SancaklarMedias.sql.keep_read_sql import kread
    except BaseException:
        edit(message, f'`{get_translation("nonSqlMode")}`')
        return
    status = kread(str(message.chat.id))
    if status:
        edit(message, f'`{get_translation("chatMuted")}`')
    else:
        edit(message, f'`{get_translation("chatAlreadyMuted")}`')
    sleep(2)
    message.delete()

    send_log(get_translation('chatLog', [message.chat.id]))


@Sancaklarify(incoming=True, compat=False)
def keep_read(client, message):
    if message.from_user and message.from_user.is_self:
        message.continue_propagation()

    try:
        from SancaklarMedias.sql.keep_read_sql import is_kread
    except BaseException:
        return

    if is_muted(message.chat.id):
        client.read_history(message.chat.id)

    message.continue_propagation()


@Sancaklarify(pattern='^.call')
def call_notes(message):
    try:
        from Sancaklarbot.modules.notes import get_note
        from Sancaklarbot.modules.snips import get_snip
    except BaseException:
        edit(message, f'`{get_translation("nonSqlMode")}`')
        return

    args = extract_args(message)
    if args.startswith('#'):
        get_note(message)
    elif args.startswith('$'):
        get_snip(message)
    else:
        edit(message, f"`{get_translation('wrongCommand')}`")


def is_muted(chat_id):
    try:
        from SancaklarMedias.sql.keep_read_sql import is_kread
    except BaseException:
        return False

    kread = is_kread()
    if kread:
        for i in kread:
            if i.groupid == str(chat_id):
                return True

    return False


HELP.update({'chat': get_translation('chatInfo')})
HELP.update({'call': get_translation('callInfo')})