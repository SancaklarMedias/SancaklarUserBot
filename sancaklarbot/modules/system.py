# Copyright (C) 2020-2021 TeamDerUntergang <https://github.com/TeamDerUntergang>
#
# This file is part of TeamDerUntergang project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from ast import Add, BinOp, BitXor, Div, Mult, Num, Pow, Sub, UnaryOp, USub, parse
from datetime import datetime
from getpass import getuser
from operator import add, mul, neg, pow, sub, truediv, xor
from shutil import which

from pyrogram.raw.functions.help import GetNearestDc
from Sancaklarbot import ALIVE_MSG, BOT_VERSION, CHANNEL, HELP, HOSTNAME, USER
from Sancaklarbot.modules.ecem import ecem
from SancaklarMedias.core import (
    edit,
    extract_args,
    get_translation,
    reply,
    reply_doc,
    Sancaklarify,
    send_log,
)

# ================= CONSTANT =================
CUSTOM_MSG = ALIVE_MSG or f"`{get_translation('SancaklarAlive')}`"
# ============================================


@Sancaklarify(pattern='^.neofetch$')
def neofetch(message):
    try:
        from subprocess import PIPE, Popen

        process = Popen(
            ['neofetch', f'HOSTNAME={HOSTNAME}', f'USER={USER}', '--stdout'],
            stdout=PIPE,
            stderr=PIPE,
        )
        result, _ = process.communicate()
        edit(message, f'`{result.decode()}`')
    except BaseException:
        edit(message, f'`{get_translation("neofetchNotFound")}`')


@Sancaklarify(pattern='^.botver$')
def bot_version(message):
    if which('git'):
        from subprocess import PIPE, Popen

        changes = Popen(
            ['git', 'rev-list', '--all', '--count'],
            stdout=PIPE,
            stderr=PIPE,
            universal_newlines=True,
        )
        result, _ = changes.communicate()

        edit(
            message,
            get_translation(
                'SancaklarShowBotVersion',
                ['**', '`', CHANNEL, BOT_VERSION, result],
            ),
            preview=False,
        )
    else:
        edit(message, f'`{get_translation("SancaklarGitNotFound")}`')


@Sancaklarify(pattern='^.ping$')
def ping(message):
    start = datetime.now()
    edit(message, '**Pong!**')
    finish = datetime.now()
    time = (finish - start).microseconds / 1000
    edit(message, f'**Pong!**\n`{time}ms`')


@Sancaklarify(pattern='^.alive$')
def alive(message):
    if CUSTOM_MSG.lower() == 'ecem':
        ecem(message)
        return
    edit(message, f'{CUSTOM_MSG}')


@Sancaklarify(pattern='^.echo')
def test_echo(message):
    args = extract_args(message)
    if len(args) > 0:
        message.delete()
        reply(message, args)
    else:
        edit(message, f'`{get_translation("echoHelp")}`')


@Sancaklarify(pattern='^.dc$', compat=False)
def data_center(client, message):
    result = client.send(GetNearestDc())

    edit(
        message,
        get_translation(
            'SancaklarNearestDC',
            ['**', '`', result.country, result.nearest_dc, result.this_dc],
        ),
    )


@Sancaklarify(pattern='^.term')
def terminal(message):
    command = extract_args(message)

    if len(command) < 1:
        edit(message, f'`{get_translation("termUsage")}`')
        return

    curruser = getuser()
    try:
        from os import geteuid

        uid = geteuid()
    except ImportError:
        uid = 0

    if not command:
        edit(message, f'`{get_translation("termHelp")}`')
        return

    result = get_translation("termNoResult")
    try:
        from SancaklarMedias.core.misc import __status_out__
        _, result = __status_out__(command)
    except BaseException as e:
        pass

    if len(result) > 4096:
        output = open('output.txt', 'w+')
        output.write(result)
        output.close()
        reply_doc(
            message,
            'output.txt',
            caption=f'`{get_translation("outputTooLarge")}`',
            delete_after_send=True,
        )
        return

    edit(message, f'`{curruser}:~{"#" if uid == 0 else "$"} {command}\n{result}`')

    send_log(get_translation('termLog', [command]))


@Sancaklarify(pattern='^.eval')
def eval(message):
    args = extract_args(message)
    if len(args) < 1:
        edit(message, f'`{get_translation("evalUsage")}`')
        return

    try:
        evaluation = safe_eval(args)
        if evaluation:
            if isinstance(evaluation, str):
                if len(evaluation) >= 4096:
                    file = open('output.txt', 'w+')
                    file.write(evaluation)
                    file.close()
                    reply_doc(
                        message,
                        'output.txt',
                        caption=f'`{get_translation("outputTooLarge")}`',
                        delete_after_send=True,
                    )
                    return
                edit(
                    message,
                    get_translation('SancaklarQuery', ['**', '`', args, evaluation]),
                )
        else:
            edit(
                message,
                get_translation(
                    'SancaklarQuery', ['**', '`', args, get_translation('SancaklarErrorResult')]
                ),
            )
    except Exception as err:
        edit(message, get_translation('SancaklarQuery', ['**', '`', args, str(err)]))

    send_log(get_translation('evalLog', [args]))


operators = {
    Add: add,
    Sub: sub,
    Mult: mul,
    Div: truediv,
    Pow: pow,
    BitXor: xor,
    USub: neg,
}


def safe_eval(expr):
    expr = expr.lower().replace('x', '*').replace(' ', '')
    return str(_eval(parse(expr, mode='eval').body))


def _eval(node):
    if isinstance(node, Num):
        return node.n
    elif isinstance(node, BinOp):
        return operators[type(node.op)](_eval(node.left), _eval(node.right))
    elif isinstance(node, UnaryOp):
        return operators[type(node.op)](_eval(node.operand))
    else:
        raise TypeError(f'`{get_translation("safeEval")}`')


HELP.update({'system': get_translation('systemInfo')})
