import http.client
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

# Сам парсер по заданным датам

def parse(con, start_date, end_date):
    con.request("GET", f"/stats/teams/ftu?startDate={start_date}&endDate={end_date}&rankingFilter=Top60", headers=headers)
    response = con.getresponse()
    txt = response.read()

    # За несколько шагов вытаскиваем все числа из таблицы списком

    soup = BeautifulSoup(txt, 'html.parser')
    body = soup.body
    data = body.find("table", {"class": "stats-table player-ratings-table ftu gtSmartphone-only"})
    numbers = data.find_all("td", {"class": "center"})
    values = []
    for number in numbers:
        loc_l = str(number).find('>') + 1
        if '%' in str(number):
            loc_r = str(number).find('%')
        else:
            loc_r = str(number).find('</')
        value = float(str(number)[loc_l:loc_r])
        values.append(value)

    # И собираем список обратно в таблицу

    table = pd.DataFrame(np.array(values).reshape((-1, 8)), columns=['winrate', 'opening_kills', 'multikills', '5v4', '4v5', 'trades', 'grenades_damage', 'flash_assists'])

    return table

# Параметры для обмана hltv.org. Вероятно, избыточные, но сайт очень не хотел делиться данными

cks = """MatchFilter={%22active%22:false%2C%22live%22:false%2C%22stars%22:1%2C%22lan%22:false%2C%22teams%22:[]}; CookieConsent={stamp:%27F1OzkgyyUBYGSnH4eynOYXGnSTuFGk2ZObl9M+RHeHMdBzw+GmUShQ==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1740843405787%2Cregion:%27de%27}; _ga=GA1.1.1719185820.1740843407; _fbp=fb.1.1740843407363.754041748268795954; _sharedid=06eabc7b-b102-455f-a3b5-0f21c2735208; _sharedid_cst=zix7LPQsHA%3D%3D; _lr_env_src_ats=false; __cf_bm=IiXIexBJa1BzH5MZethy__TOg.RfYj0kjnwhxU4O.yE-1740848155-1.0.1.1-4lNmN4v9AIcTfcFpwRayZuMc.0QiwtbNBSSH_86lamxfIYKgjpQVBBc7kkV1lkpyBBqi4BbLXVSGGPrSJCBXlX7RCzeXpyyN9LE3XKboeZw; cf_clearance=L_Q10JFBQ8GWWsDlM9hAJ.f6Hc53wRLiiVfsPWViC_Y-1740848156-1.2.1.1-elICz2bUzedNHmRncii1G7xYLrJ_lZE0_DYzc2RUwv1uTOOBqwfAfSAGUS9a_xcfHn.TJIukP45LvwllNQsbnyQtH4TRR0dkYGVWVRqi9KUnNpWLmg7zrdSGdHJpfqjALKzW2Xc2OiNZx3oNLQq.ycqld97TVDl5op2qr9KNsstv4mnwwJ9.bdAKOhCw2RAgEI0YbZ1H7La._AuiTFiWXkGw9fxsK47RGnw7aOayiQyCvUBaa4ZBQpRkp3tDIyQcJcc.HIjQrLrZgTWOZodvg2R48.UiL8aHPE_tnHLXHU6nfHi_qSE6ZPTH2_yl3.dxkIv0kP8d7cS9ghw4U7fXEADFou4_1EF14RsZWdFvQvPwXrcpBcjNvJkYkFLZKyXzVcYLbh4OtqmPSLcpG4jV_Gb2QD4wMAxwYIPWrRgSsMk; _lr_retry_request=true; dicbo_id=%7B%22dicbo_fetch%22%3A1740848157340%7D; _ga_525WEYQTV9=GS1.1.1740848156.3.1.1740848220.0.0.0; cto_bundle=lA2kn19mJTJCMkFqYjlOS25iJTJGWnl2R3Y1SnFTVkNZa3pwUXJua2xteXc0MWVvUWR1eUJSM2YlMkJRRWZkR1Q3cHg2aHdNUDFQUGI0JTJCbk1RMnJEZWU5R1pwaVFhQSUyRjFKdG53SXIlMkZObWRTTW5wRG1YRDBuZ09lTyUyRjVUN2ZlMXBEdE9sa3VYbWdtQWlOM1dEJTJGcHV5eUdyanNlNWlQdDJRJTNEJTNE; cto_bidid=zszJO194WFRPWGFzcktzZkQ5YmxtJTJGbkYxTjRkb1FWb2NBaTJhZFU0dnM2Y2x1M3BhaW5uVGlEampXaTZpZXU4NXNUS3BKTElOc1dJWjdKZkh5TGNlJTJCUVRXbGpnNHVhZmt1VGs1eEc1VHNhOTQybzglM0Q; __gads=ID=992cbfab2859d0b9:T=1740845375:RT=1740848221:S=ALNI_MbdCEUEwEWWFte_yHbDP7Hxn-RdlA; __gpi=UID=0000104a0846ea1d:T=1740845375:RT=1740848221:S=ALNI_MYjbDhu2sdgOt1OTa891sGjFQTR6g; __eoi=ID=05cebf1d3dd17c4d:T=1740845376:RT=1740848221:S=AA-AfjZpiRNEYTnf0hz3K1bI1Dc-"""
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'Accept-Encoding': 'utf8',
           'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
           'Cache-Control': 'max-age=0',
           'Cookie': cks,
           'Priority': 'u=0, i',
           'Sec-Ch-Ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
           'Sec-Ch-Ua-Mobile': '?0',
           'Sec-Ch-Ua-Platform': '"Windows"',
           'Sec-Fetch-Dest': 'document',
           'Sec-Fetch-Mode': 'navigate',
           'Sec-Fetch-Site': 'none',
           'Sec-Fetch-User': '?1',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

host = 'www.hltv.org'
con = http.client.HTTPSConnection(host)

general = pd.DataFrame(columns=['winrate', 'opening_kills', 'multikills', '5v4', '4v5', 'trades', 'grenades_damage', 'flash_assists'])
days = {1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31}

# Задаём нужные годы и получаем общую таблицу

for year in range(2017, 2025):
    for month in range(1, 13):
        parsed = parse(con, f'{year}-{str(month).zfill(2)}-01', f'{year}-{str(month).zfill(2)}-{days[month]}')

        general = pd.concat([general, parsed], ignore_index=True)

general.to_csv('dataset.csv', index=False)

print(general)