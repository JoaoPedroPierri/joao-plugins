# by joaoppierri

from userge import Message, userge

@userge.on_cmd("k|K", about={"header": "risada curta"}, allow_via_bot=False)
async def k_(message: Message):
    out_str =f"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
    await message.edit(out_str)

@userge.on_cmd("kkk|KKK", about={"header": "risada  longa"}, allow_via_bot=False)
async def kkk_(message: Message):
    out_str = f"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
    await message.edit(out_str)
