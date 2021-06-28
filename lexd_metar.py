import asyncio
import requests
from dotenv import load_dotenv
import os

"""
THIS FILE IS LICENSED UNDER THE MOZILLA PUBLIC LICENSE 2.0
https://github.com/lexd283/lexd_metar.py/blob/main/LICENSE
BY USING THIS, YOU ARE FOLLOWING THE LICENSE.

Thank you for using lexd_metar.py!
This was a side-project, because honestly, I was bored lol
This can give you the METAR for the airport of your choice.

If you have any problems, message me on discord.
Discord: big bus man#8780

KNOWN BUGS: https://github.com/lexd283/lexd_metar.py#known-bugs
"""

load_dotenv()
secret = os.getenv("API_KEY")

async def main():
    lexd = input('ICAO or IATA: ')
    os.system('cls')
    headers = {'Authorization': secret}
    ok = requests.get(f'https://avwx.rest/api/metar/{lexd}?airport=true&reporting=true&format=json', headers=headers)
    joe = ok.json()
    if "error" in joe:
        return print(f'{lexd} is not supported, or there was an error fetching information.')
    print(f'lexd_metar.py\nSTATION: {lexd.upper()}\nRAW REPORT: {joe["raw"]}\nTIME OF OBSERVATION: {joe["time"]["repr"]} ({joe["time"]["dt"]})\nWIND: {joe["wind_direction"]["value"]}°@{joe["wind_speed"]["value"]}{joe["units"]["wind_speed"]}\nDEWPOINT: {joe["dewpoint"]["value"]}\nTEMPERATURE: {joe["temperature"]["value"]}')
    results = [x['repr'] for x in joe['clouds']]
    x = 0
    new_results = []
    if results:
        print('CLOUD LAYERS:')
        for result in results:
            x = x + 1
            print(f'Layer {x} - {result}')



asyncio.run(main())
