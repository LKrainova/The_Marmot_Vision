import json

data_for_search = [
    {
        "query": "самсунг",
        "title": "Смартфон Samsung Galaxy S25 Ultra 5G 12/256GB Titanium Gray",
        "url": "https://megamarket.ru/catalog/details/smartfon-samsung-galaxy-s25-ultra-5g-12-256gb-titanium-gray-100073744126/",
        "description": "Отличный телефон, у меня версия на эксинос, все летает. Очень яркий экран, приятный дизайн, вес небольшой. \nЦвет Marble Grey очень красивый, однако, если носить в чехле, то видно не будет. Прозрачный чехол дешевит телефон",
        "url_photo": "https://main-cdn.sbermegamarket.ru/big2/hlr-system/436/352/496/226/169/100066351023b1.jpg"
    },
    {
        "query": "HUAWEI Watch Fit 2",
        "title": "Смарт-часы HUAWEI Watch Fit 2 Classic Edition лунный белый",
        "url": "https://megamarket.ru/catalog/details/smart-chasy-huawei-watch-fit-2-classic-edition-lunnyy-belyy-100034672650_79712/",
        "description": "количества калорий; количества шагов; продолжительности сна; сердечного ритма; уровня кислорода в крови; физической активности",
        "url_photo": "https://main-cdn.sbermegamarket.ru/big2/hlr-system/-12/064/048/188/121/938/100034672650b0.jpg"
    },
    {
        "query": "HUAWEI Watch Fit 2",
        "title": "Умная колонка Яндекс Новая Станция Мини (с часами) Black (YNDX-00020K)",
        "url": "https://megamarket.ru/catalog/details/umnaya-kolonka-yandeks-novaya-stanciya-mini-s-chasami-black-yndx-00020k-100029400053/",
        "description": "Одним из главных плюсов умной колонки Яндекс Новая Станция Мини является ее функциональность. \nОна поддерживает голосовое управление, что делает ее очень удобной в использовании. \nВы можете просить колонку включить музыку, регулировать громкость, задавать вопросы, заказывать такси, узнавать новости и многое другое, просто используя свой голос. \nЭто особенно удобно, когда вам заняты руками или вы находитесь на некотором расстоянии от колонки.",
        "url_photo": "https://main-cdn.sbermegamarket.ru/big2/hlr-system/166/672/987/211/262/015/100029400053b2.jpg"
    },
    {
        "query": "insta 360 x4",
        "title": "Смарт-часы Huawei Watch 4 Pro серый (55020BXM)",
        "url": "https://megamarket.ru/catalog/details/smart-chasy-huawei-watch-4-pro-seryy-55020bxm-600022971270/",
        "description": "Смарт-часы HUAWEI WATCH 4 Pro LTE SE Grey предоставляют широкий набор функций, \nнаправленных на мониторинг здоровья и улучшение удобства пользования смартфоном. \nОсновные характеристики и возможности устройства включают:",
        "url_photo": "https://main-cdn.sbermegamarket.ru/big2/hlr-system/978/424/544/121/217/17/600022971270b0.jpg"
    },
    {
        "query": "гречка в пакетиках",
        "title": "Крупа гречневая PROSTO в варочных пакетиках, 8 порций, 500 г",
        "url": "https://megamarket.ru/catalog/details/krupa-grechnevaya-prosto-yadrica-kalibrovannaya-v-paketikah-8x625-g-100023360997_13079/#?related_search=%D0%B3%D1%80%D0%B5%D1%87%D0%BA%D0%B0%20%D0%B2%20%D0%BF%D0%B0%D0%BA%D0%B5%D1%82%D0%B8%D0%BA%D0%B0%D1%85",
        "description": "Крупа гречневая ядрица быстроразваривающаяся, калиброванная. Сорт высший. \nМожет содержать следы глютена",
        "url_photo": "https://main-cdn.sbermegamarket.ru/big2/hlr-system/-10/777/660/881/122/250/100023360997b0.jpg"
    },
    {
        "query": "choco pie",
        "title": "Пирожное choco pie Lotte 336 г",
        "url": "https://megamarket.ru/catalog/details/pirozhnoe-choco-pie-lotte-336-g-100023631696/",
        "description": "мука пшеничная хлебопекарная в/с, сахар-песок, вода питьевая, \nглюкозный сироп (патока крахмальная высокоосахаренная), жир кондитерский, масло растительное, какао-порошок",
        "url_photo": "https://main-cdn.sbermegamarket.ru/big2/hlr-system/151/401/150/113/011/10/100023631696b0.jpg"
    },
    {
        "query":
        "title":
        "url":
        "description":
        "url_photo":
    },
    {
        "query":
        "title":
        "url":
        "description":
        "url_photo":
    },
    {
        "query":
        "title":
        "url":
        "description":
        "url_photo":
    },
    {
        "query":
        "title":
        "url":
        "description":
        "url_photo":
    },
    {
        "query":
        "title":
        "url":
        "description":
        "url_photo":
    },
    {
        "query":
        "title":
        "url":
        "description":
        "url_photo":
    },
    {
        "query":
        "title":
        "url":
        "description":
        "url_photo":
    },
    {
        "query":
        "title":
        "url":
        "description":
        "url_photo":
    },
]










import json

# Sample dataset
data = [
    {
        "query":
        "title":
        "url":
        "description":
        "url_photo":
    },
    {
        "query": "Samsung Galaxy S23 price",
        "title": "Samsung Galaxy S23 - Best Prices",
        "url": "https://example.com/galaxy-s23",
        "description": "Latest Samsung Galaxy S23 with great discounts.",
        "url_photo": "https://example.com/galaxy-s23.jpg"
    }
]

# Save to a JSON file
with open("dataset.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4, ensure_ascii=False)

print("JSON file created successfully!")