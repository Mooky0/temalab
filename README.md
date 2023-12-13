# Forrásfálok Témalaboratórium beszámolóhoz

Készítette: Tóth Gábor \
E-mail cím: tothgabor2003@gmail.com

## Téma címe: 	Horizontális autoskálázás Kubernetes klaszterben 

### Feladat 

Egy Kubernetes klaszterben futó web alapú egyszerű alkalmazás terheléstesztelése és az így felhasznált erőforrások mérése. A mérések alapján az alkalmazás automatikus horizontális skálázása, és fölöslegesen foglalt erőforrások felszabadítása. Továbbá a gyűjtött metrikák megjelenítése egy másik, weben keresztül elérhető felületen.

### Fájlok

| Név 	                        | Leírás 	                            |
|-----	                        |--------	                            |
|forras_1/performance-test.js   |A terhelésteszt konfigurációja         |
|rc_hpa.yaml                    |A HPA manifest fájlja                  |
|rc_image/Dockerfile            |A konténer image leírója               |
|rc_image/index.html            |A szerver által megjelenített oldal    |
|rc_image/server.py             |A szerver programja                    |
|resource-consumer.yaml         |A szerver manifest fájlja              |

A teljes munka a [temalab.pdf](temalab.pdf) fájban található.