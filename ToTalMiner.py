from asyncio import sleep
from .. import loader, utils
import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions, TelegramClient, errors
from ..inline.types import InlineCall
import inspect
import re
import logging

# meta developer: большая часть кода @kepperok добавления и улучшения @tot_882
@loader.tds
class ToTalMiner(loader.Module):
    strings = {
        "name": "ToTalMiner",
        "kt": "\n✉️ Белый:",
        "rkt": "\n🧧 Талесман:",
        "k": "\n📦 Каробка:",
        "rk": "\n🗳 Платок:",
        "mif": "\n⚫️ Чорный камен:",
        "kr": "\n💎 Бриллиант:",
        "dk": "\n🎲 Кубик рубик:",
        "ssp": "\n👜 Сумчка:",
        "pse": "\n💼 Порфель с денег:",
        "zv": "\n🌌 Звëзды:",
        "plasma": "\nФейверк🎆:"
    }
    def __init__(self):
        super().__init__()
        self.mining = False
        self.messages_sent = 0
        self.kt = 0
        self.rkt = 0
        self.k = 0
        self.rk = 0
        self.mif = 0
        self.dk = 0
        self.kr = 0
        self.ss = 0
        self.ps = 0
        self.zv = 0
        self.plasma = 0

    async def client_ready(self, client, db):
        self.bb = False
        s = self.get('dly')
        if s is None:
            self.set('dly', 1.0)
        s = self.get('mm')
        if s is None:
            self.set('mm', False)
        s = self.get('ag')
        if s is None:
            self.set('ag', False)
        s = self.get('as')
        if s is None:
            self.set('as', False)
        s = self.get('fw')
        if s is None:
            self.set('fw', False)
        if self.get("cases") == None:
            self.set("cases", {
                "kt": True,
                "rkt": True,
                "k": True,
                "rk": True,
                "mif": True,
                "kr": True,
                "dk": True,
                "zv": True,
                "ssp": True,
                "pse": True,
                "plasma": True
            })
        if self.get("kol_cases") == None:
            self.set("kol_cases", {
                "kt": 0,
                "rkt": 0,
                "k": 0,
                "rk": 0,
                "mif": 0,
                "kr": 0,
                "dk": 0,
                "zv": 0,
                "ssp": 0,
                "pse": 0,
                "plasma": 0,
                "clicks": 0
            })
        await self.continue_mining()

    @loader.watcher()
    async def watcher(self, message):
        a = self.get("kol_cases")
        if hasattr(message, 'from_id') and hasattr(message, 'chat_id') and message.from_id == 7168860714 and message.chat_id == 7168860714 and "Руда на уровень" in message.raw_text:
            a["clicks"] += 1
            self.set("kol_cases", a)
            
        if hasattr(message, 'from_id') and hasattr(message, 'chat_id') and message.from_id == 7168860714 and message.chat_id == 7168860714 and "Найден" in message.raw_text:
            if "✉" in message.raw_text and "Конверт" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])
                
                a["kt"] += colvo
                self.set("kol_cases", a)
            if "🧧" in message.raw_text and "Редкий Конверт" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])
                
                a["rkt"] += colvo
                self.set("kol_cases", a)

            if "📦" in message.raw_text and "Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["k"] += colvo
                self.set("kol_cases", a)

            if "🗳" in message.raw_text and "Редкий Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["rk"] += colvo
                self.set("kol_cases", a)

            if "🕋" in message.raw_text and "Мифический Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["mif"] += colvo
                self.set("kol_cases", a)

            if "Портфель" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["pse"] += colvo
                self.set("kol_cases", a)

            if "Сумка" in message.raw_text:    
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["ssp"] += colvo
                self.set("kol_cases", a)

            if "💎" in message.raw_text and "Кристальный Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["kr"] += colvo
                self.set("kol_cases", a)

            if "🎲" in message.raw_text and "Дайс Кейс" in message.raw_text:
                colpt = r"\d+"
                search = re.search(colpt, message.raw_text)
                colvo = int(search[0])

                a["dk"] += colvo
                self.set("kol_cases", a)

            if "💫" in message.raw_text:
                a["zv"] += 1
                self.set("kol_cases", a)

        if hasattr(message, 'from_id') and message.from_id == 7168860714 and message.chat_id == 7168860714 and "Плазма +" in message.raw_text:
            plpt = r"\d+"
            search = re.search(plpt, message.raw_text)
            colvo = int(search[0])
            
            a["plasma"] += colvo
            self.set("kol_cases", a)

    @loader.command()
    async def mmm(self, message):
        '''- Включить/выключить копание'''
        self.set('mm', not self.get('mm'))
        if self.get('mm'):
            await self.client.send_message(message.chat_id, "<b>⚡Коп вкл⚡")
            await message.delete()
            self.set("kol_cases", {
                "kt": 0,
                "rkt": 0,
                "k": 0,
                "rk": 0,
                "mif": 0,
                "kr": 0,
                "dk": 0,
                "zv": 0,
                "ssp": 0,
                "pse": 0,
                "plasma": 0,
                "clicks": 0
            })
            await self.continue_mining()
        else:
            cases_text=""
            a = self.get("cases")
            b = self.get("kol_cases")
            for i in a:
                if a[i]:
                    cases_text += self.strings(i)+" "+str(b[i])
            await self.client.send_message(message.chat_id, f"<b>☣️Слово богу что дали одохнут ☣️\n📨 я копал для этой хуйни аж: {b['clicks']}\n🠗за всë этот время когда я был его рабыня, я выкопал аж  🠗\n{cases_text}</b>")
            await message.delete()
            

    async def continue_mining(self):
        while self.get('mm'):
            await self.client.send_message("@mine_evo_gold_bot", 'коп')
            await asyncio.sleep(self.get('dly'))
    async def process_mining_result(self, result_text):
        pass

    @loader.command()
    async def emdly(self, message: Message):
        '''- Установить задержку копания [значение]'''
        args = utils.get_args_split_by(message, " ")
        cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
        if args:
            cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
        else:
            await utils.answer(message, f'❌ <b>Ошибка | {cmd}</b>\nУкажите значение, которое хотите установить')
            return
        if len(args) > 1:
            await utils.answer(message, f'❌ <b>Ошибка | {cmd}</b>\nВы указали больше одного аргумента')
            return

        zz = args[0]
        try:
            zz = float(zz)
            self.set('dly', zz)

            clicks = [100, 1000, 10000, 100000]
            times_required = [click * zz for click in clicks]

            response_text = f'✅ <b>Успешно!</b>\n<i>Задержка копания изменена на {zz} секунд</i>\n\n🕒 <b>Таким темпом:</b>\n'
            for click, time_required in zip(clicks, times_required):
                response_text += f'👉 {click} копаний за: <b>{self.format_time(time_required)}</b>⛏\n'

            await utils.answer(message, response_text)

        except ValueError:
            await utils.answer(message, f'❌ <b>Ошибка | {cmd}</b>\nУкажите число в значении!')

    def format_time(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return f'{int(days)} дней, {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд'

    @loader.command()
    async def emcfg(self,message):
        '''- Конфиг модуля MevoMiner'''
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        if self.get('mm'):
            dpm = 'Включено'
        else:
            dpm = 'Выключено'
        
        await self.inline.form(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n⛏ <b>Статус копания:</b> <i>{dpm}</i>\n<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}",
            message=message,
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка копания ',
                        'callback' : self.mdlym,
                    },
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.idd,
                    },
                ],
                [
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def mdlym(self,call:InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        if self.get('mm'):
            dpm = 'Включено'
        else:
            dpm = 'Выключено'
        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n⛏ <b>Статус копания:</b> <i>{dpm}</i>\n<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}\n\n<i><emoji document_id=5452069934089641166>❓</emoji> Чтобы изменить задержку копания напишите:\n</i><code>.emdly [задержка]</code>",
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка копания ',
                        'callback' : self.mdlym,
                    },
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.idd,
                    },
                ],
                [
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def iback(self,call:InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        if self.get('mm'):
            dpm = 'Включено'
        else:
            dpm = 'Выключено'

        await call.edit(
            text=f"<emoji document_id=5981043230160981261>⏱</emoji> <b>Задержка копания:</b> <code>{self.get('dly')}</code>\n⛏ <b>Статус копания:</b> <i>{dpm}</i>\n<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}",
            reply_markup=[
                [
                    {
                        'text' : '⏱ Задержка копания ',
                        'callback' : self.mdlym,
                    },
                    {
                        'text' : '➕ Дополнительные параметры',
                        'callback' : self.idd,
                    },
                ],
                [
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def idd(self,call:InlineCall):
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Выкл/не выкл копание во время убийства босса',
                        'callback' : self.ibs
                    },
                ],
                [
                    {
                        'text' : 'Копание после убийства босса',
                        'callback' : self.ibg,
                    },
                ],
                [
                    {
                        'text' : 'Копание после FloodWait',
                        'callback' : self.ifs,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.iback,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def ibg(self,call:InlineCall):
        self.set('ag', not self.get('ag'))
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Выкл/не выкл копание во время убийства босса',
                        'callback' : self.ibs
                    },
                ],
                [
                    {
                        'text' : 'Копание после убийства босса',
                        'callback' : self.ibg,
                    },
                ],
                [
                    {
                        'text' : 'Копание после FloodWait',
                        'callback' : self.ifs,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.iback,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def ibs(self,call:InlineCall):
        self.set('as', not self.get('as'))
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Выкл/не выкл копание во время убийства босса',
                        'callback' : self.ibs
                    },
                ],
                [
                    {
                        'text' : 'Копание после убийства босса',
                        'callback' : self.ibg,
                    },
                ],
                [
                    {
                        'text' : 'Копание после FloodWait',
                        'callback' : self.ifs,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.iback,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
    async def ifs(self,call:InlineCall):
        self.set('fw', not self.get('fw'))
        if self.get('ag'):
            dpg = ' ▫️ <i>Включать копание после убийства босса</i>\n'
        else:
            dpg = ''
        
        if self.get('as'):
            dps = ' ▫️ <i>Выключать копание во время убийства босса</i>\n'
        else:
            dps = ''
        
        if self.get('fw'):
            dpf = ' ▫️ <i>Включать копание после FloodWait</i>\n'
        else: 
            dpf = ''
        
        await call.edit(
            text=f'<b>➕ Дополнительные параметры:</b>\n{dps}{dpg}{dpf}',
            reply_markup=[
                [
                    {
                        'text' : 'Выкл/не выкл копание во время убийства босса',
                        'callback' : self.ibs
                    },
                ],
                [
                    {
                        'text' : 'Копание после убийства босса',
                        'callback' : self.ibg,
                    },
                ],
                [
                    {
                        'text' : 'Копание после FloodWait',
                        'callback' : self.ifs,
                    },
                ],
                [
                    {
                        'text' : '🔙 Назад',
                        'callback' : self.iback,
                    },
                    {
                        'text' : '🔻 Закрыть',
                        'action' : 'close'
                    }
                ]
            ]
        )
         