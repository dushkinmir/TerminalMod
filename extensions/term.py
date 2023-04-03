import subprocess
from base.mod_ext import ModuleExtension
from base.module import command, allowed_for
from pyrogram.types import Message

class TermCmd(ModuleExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.command = self.S["term"]["command"]
        self.output1 = self.S["term"]["output"]
        self.err = self.S["err"]
        self.no_args = self.S["no_args"]

    @allowed_for("owner")
    @command("term")
    async def term_cmd(self, _, message: Message):
        """Module for executing a term command"""
        # Получаем аргументы команды
        args = message.text.split()

        # Если не указаны аргументы, выводим сообщение об ошибке
        if len(args) < 2:
            await message.reply(self.no_args)
            return

        # Собираем команду, которую нужно выполнить в оболочке
        cmd = " ".join(args[1:])

        # Выполняем команду в оболочке и получаем ее вывод
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            # Если возникла ошибка, выводим ее текст
            await message.reply(f"{self.command}\n<code>{' '.join(args[1:])}</code>\n\n{self.err} <code>{e.output}</code>")
            return

        # Выводим результат выполнения команды в нужном формате
        await message.reply(f"{self.command}\n<code>{' '.join(args[1:])}</code>\n\n{self.output1}\n<code>{output}</code>")
