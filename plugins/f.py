""" enjoy memes """

# All rights reserved.

import asyncio
import os
import random
import requests
import wget
from cowpy import cow

from kannax import Message, kannax

from kannax import Message, kannax



  @kannax.on_cmd("f", about={"header": "f"})
  async def payf(event):
    paytext = message.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 6,
        paytext * 6,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
    )
    await message.edit(pay)