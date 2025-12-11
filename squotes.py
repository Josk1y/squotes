"""
    Модуль для заміни слів кімпінтяу/кимпинтяу
"""

from .. import loader, utils

@loader.tds
class KimpintiauMod(loader.Module):
    """Замінює 'кімпінтяу' на 'братишь'"""
    
    strings = {"name": "Kimpintiau"}

    @loader.watcher(out=True)
    async def watcher(self, message):
        # Перевіряємо, чи є текст у повідомленні
        if not message.text:
            return

        # Список слів-тригерів (можна додавати свої)
        triggers = ["кімпінтяу", "кимпинтяу"]

        # Приводимо текст до нижнього регістру і прибираємо зайві пробіли
        text = message.text.lower().strip()

        # Якщо текст співпадає з тригером
        if text in triggers:
            # Редагуємо повідомлення
            await message.edit("братишь")
