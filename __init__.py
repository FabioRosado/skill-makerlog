from opsdroid.skill import Skill
from opsdroid.matchers import match_regex

import logging
import aiohttp
import json

_LOGGER = logging.getLogger(__name__)


class MakerLog(Skill):

    @match_regex(r'(add|completed) task - (.*)')
    async def add_task(self, message):
        """Add to do task to log on makerlog."""
        status = message.regex.group(1)
        task = message.regex.group(2)

        payload = {'content': task, 'done': False}

        if status == 'completed':
            payload['done'] = True

        async with aiohttp.ClientSession() as session:

            request = await session.post(self.config['webhook'],
                                         data=payload)

            if request.status == 201:
                await message.respond("Added to do task "
                                      "'{}' to makerlog".format(task))
            else:
                _LOGGER.warning("Unable to add to do task to makerlog.")
                _LOGGER.debug(request)
