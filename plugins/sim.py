# by joaoppierri

from pyrogram.errors import BadRequest

from kannax import Message, kannax
from kannax.utils import get_file_id

@kannax.on_cmd("s", about={"header": "sim"})
async def w_(message: Message):
    out_str = f"sim
    await message.edit(out_str)
    
