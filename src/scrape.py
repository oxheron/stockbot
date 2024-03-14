import asyncio
import time
from pyppeteer import launch

from dotenv import load_dotenv
import os

password = os.getenv("PASSWORD")

async def get_attrib(element, page, attrib):
    return await page.evaluate("element => element.getAttribute('" + attrib + "')", element);

async def get_blurred_text(element, page):
    text_element = await element.querySelector('div[class="w-full"]');
    return await get_attrib(text_element, page, "blurred-text");

async def extract_element_info(element, page):
    symbol = await element.querySelector('td[style="width: 110px; left: 0px;"]');
    phase = await element.querySelector('td[style="width: 260px;"]');
    date = await element.querySelectorAll('td[style="width: 180px;"]');
    return [await get_blurred_text(symbol, page), await get_blurred_text(phase, page), await get_blurred_text(date[2], page)];

async def scroll(page):
    await page.evaluate('window.scrollTo(0, document.body.scrollHeight)');

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setViewport({"width":1920, "height":1080})
    await page.goto('https://www.biopharmcatalyst.com/account/login')
    await page.type('input[type=email]', 'Micahmylesogden@gmail.com', delay=104);
    await page.type('input[type=password]', password, delay=98);
    await page.click('button[type=submit]');
    await page.waitForNavigation();

    await page.goto('https://www.biopharmcatalyst.com/calendars/historical-catalyst-calendar');

    input("Press Enter to continue...")

    file = open("phase3.csv", "w");

    last_element_count = 0
    while True:
        elements = await page.querySelector('tbody[role="rowgroup"][class="p-datatable-tbody"]');
        elements_list = await elements.querySelectorAll('tr[role="row"]')
        for i in range(last_element_count, len(elements_list)):
            data = await extract_element_info(elements_list[i], page)
            file.write(data[0]);
            file.write(", ");
            file.write(data[1]);
            file.write(", ");
            file.write(data[2]);
            file.write(", \n");
            
        if len(elements_list) >= 1920:
            break
        print(len(elements_list))
        last_element_count = len(elements_list)
        await scroll(page)

    file.close()

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

