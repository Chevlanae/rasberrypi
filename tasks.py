import asyncio
from gpiozero import OutputDevice
from gpiozero.pins import mock


async def power_loop(relay=OutputDevice(1, pin_factory=mock.MockFactory()), timeOn=60, timeOff=60, id=""):
    '''Infinite loop that turns a relay on and off at the provided intervals'''

    try:
        while True:

            relay.on()
            print(id + " on...")

            await asyncio.sleep(timeOn)

            relay.off()
            print(id + " off...")

            await asyncio.sleep(timeOff)

    except asyncio.CancelledError:
        print(id + " loop cancelled...")
        relay.off()
