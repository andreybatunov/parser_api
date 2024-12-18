#########################################
### Строительный двор (пагинации нет) ###
#########################################

URL_SDVOR = "https://www.sdvor.com/moscow/category/krovlja-i-fasad-9050"
PRODUCT_TAG_SDVOR = {"tag": "div", "class_name": "product"}
PRODUCT_NAME_TAG_SDVOR = {"tag": "a", "class_name": "product-name"}
PRODUCT_PRICE_TAG_SDVOR = {"tag": "span", "class_name": "main"}
PAGES_SDVOR = {}


SDVOR_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "qrator_jsid=1729514747.185.StdffyEJKF27qRjQ-78kj82vl0sbigoo1mt16e1kp042md6ai; ASP.NET_SessionId=quf3mnbgh2wv50wxhoi4pfsr; hpuid=02238c8386cc19ef8dffb9d0b7425a1d; SRV_HAYAS=node01; UtcTos=-300; _gcl_au=1.1.439828285.1729514675; _ym_uid=1729514675821061146; _ym_d=1729514675; _ga=GA1.1.915096271.1729514675; flocktory-uuid=6245582c-48d2-4386-8320-d68c23e0d71e-2; _ym_visorc=w; _ym_isad=2; tmr_lvid=6ef528f6930eb94ab7dcd4f186fd39c9; tmr_lvidTS=1729514676716; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; ssaid=3b0413f0-8faa-11ef-986a-03944c7a57cf; domain_sid=u9W9rXtTgLyLDwt1Mho1N%3A1729514676995; mindboxDeviceUUID=9543b01f-7254-4990-97ff-5e7e75a66bce; directCrm-session=%7B%22deviceGuid%22%3A%229543b01f-7254-4990-97ff-5e7e75a66bce%22%7D; popCity=1; adrdel=1729514691889; adrcid=A2G7oGDk08RpmquaIUDQB4w; acs_3=%7B%22hash%22%3A%225c916bd2c1ace501cfd5%22%2C%22nextSyncTime%22%3A1729601091969%2C%22syncLog%22%3A%7B%22224%22%3A1729514691969%2C%221228%22%3A1729514691969%2C%221230%22%3A1729514691969%7D%7D; __tld__=null; tmr_detect=0%7C1729514694001; _ga_KXLLKH0F95=GS1.1.1729514675.1.1.1729514910.59.0.0",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "sec-ch-ua": 'Google Chrome;v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
}


##################################
### Henderson (пагинация есть) ###
##################################

URL_HENDERSON = "https://henderson.ru/catalog/shirts/"
PRODUCT_TAG_HENDERSON = {"tag": "div", "class_name": "card-product__info"}
PRODUCT_NAME_TAG_HENDERSON = {"tag": "a", "class_name": "card-product__name-link"}
PRODUCT_PRICE_TAG_HENDERSON = {"tag": "div", "class_name": "card-product__price"}
PAGES_HENDERSON = {"tag": "a", "class_name": "pagination-page"}
SHORT_URL_HENDERSON = "https://henderson.ru/"


HENDERSON_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "henderson.ru",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}


COOKIES = {
    "_gcl_au": "1.1.439828285.1729514675",
    "_ym_uid": "1729514675821061146",
    "_ym_d": "1729514675",
    "_ga": "GA1.1.915096271.1729514675",
    "flocktory-uuid": "6245582c-48d2-4386-8320-d68c23e0d71e-2",
    "tmr_lvid": "6ef528f6930eb94ab7dcd4f186fd39c9",
    "tmr_lvidTS": "1729514676716",
    "popmechanic_sbjs_migrations": "popmechanic_1418474375998=1|||1471519752600=1|||1471519752605=1",
    "ssaid": "3b0413f0-8faa-11ef-986a-03944c7a57cf",
    "adrcid": "A2G7oGDk08RpmquaIUDQB4w",
    "qrator_jsr": "1734541473.573.pQ03SHbUqEgoH7rU-ltqn2ceec9ijbgbld58jpe3kuansos91-00",
    "qrator_jsid": "1734541473.573.pQ03SHbUqEgoH7rU-mf84t42b4mc32s5me3bjm3v63cgrqsa8",
    "ASP.NET_SessionId": "mu0pklzbpabrnbxryxdxouom",
    "hpuid": "aaaf9bffd240fd0bf1e5a86b9b1a8f5a",
    "SRV_HAYAS": "node03",
    "UtcTos": "-300",
    "_ym_visorc": "b",
    "acs_3": "{\"hash\":\"768a608b20ce960ff29026da95a81203ec583ad1\",\"nextSyncTime\":1734627794989,\"syncLog\":{\"224\":1734541394989,\"1228\":1734541394989,\"1230\":1734541394989}}",
    "adrdel": "1734541395121",
    "_ym_isad": "2",
    "popCity": "1",
    "domain_sid": "u9W9rXtTgLyLDwt1Mho1N:1734541397161",
    "_ga_KXLLKH0F95": "GS1.1.1734541394.4.1.1734541526.18.0.0",
    "mindboxDeviceUUID": "9543b01f-7254-4990-97ff-5e7e75a66bce",
    "directCrm-session": "{\"deviceGuid\":\"9543b01f-7254-4990-97ff-5e7e75a66bce\"}",
    "__tld__": "null",
    "tmr_detect": "0|1734541528642"
}
