import subprocess
from base.mod_ext import ModuleExtension
from base.module import command, allowed_for
from pyrogram.types import Message

class EvalCmd(ModuleExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.command = self.S["eval"]["code"]
        self.output1 = self.S["eval"]["result"]
        self.err = self.S["err"]
        self.no_args = self.S["no_args"]

    @allowed_for("owner")
    @command("eval")
    async def eval_cmd(self, _, message: Message):
        await message.reply("нет")
        # # Получаем аргументы команды
        # args = message.text.split()

        # # Если не указаны аргументы, выводим сообщение об ошибке
        # if len(args) < 2:
        #     await message.reply(self.no_args)
        #     return

        # # Получаем код, который нужно выполнить
        # code = " ".join(args[1:])

        # # Проверяем, что код начинается с тройных кавычек
        # if not code.startswith('"""'):
        #     code = '"""' + code

        # # Проверяем, что код заканчивается тройными кавычками
        # if not code.endswith('"""'):
        #     code += '"""'

        # # Выполняем код и получаем результат
        # try:
        #     result = eval(code)
        # except Exception as e:
        #     # Если возникла ошибка, выводим ее текст
        #     await message.reply(f"{self.command}\n<code>{code}</code>\n\n{self.err} <code>{e}</code>")
        #     return

        # # Выводим результат выполнения кода в нужном формате
        # await message.reply(f"{self.command}\n<code>{code}</code>\n\n{self.output1}\n<code>{result}</code>")
