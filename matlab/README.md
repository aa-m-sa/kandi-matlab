# Kandin Matlab-koodit


* Matlab-yhteensopivaa Octave-koodia: SA-algoritmin toteutus

## Koodista

Projektin rakenne on seuraava:

### Algoritmi

* `annealing.m` perusversio SA-algoritmin toteutuksesta: funktio

### Apufunktiot jne

* `createdataimage.m` luo simuloitu testidata (annetuin paremetrein). vastaa
tutkielman tekstin 'simuloitu aineisto' mallia

* `circle.m` generoi kuvamatriisin jossa ympyrä / ympyröitä (kuten tutkielman
tekstissä kuvailtu)

* `convolution.m` kuvamallin konvoluutio (ts. pienempi konvoluutiomatriisi),
energiafunktiota varten

* `addnoise.m` palauttaa parametrina annetusta kuvasta version johon lisätty
tasajakautunutta kohinaa

* TODO: hintafunktiot, jäähdytysskenaariot

### Testit

* `testscript.m` sekalaista testausta

* `testannealing.m`, `testannealing2.m`, jne. hieman hienompia
testiskriptejä algoritmin toiminnan kokeilemiseen (luodaan erilaisia sarjoja
testidataa, kokeillaan SA:ta niihin, printtaa kuvia)

* `testcircle.m` kokeillaan että `circle.m` toimii piirtämällä erilaisia
ympyröitä (nykyinen versio yrittää piirtää torusympyröitä jotka eivät toimi)

* `testcircletime.m` aja `time octave testcircletime.m` -> vertaile kuinka
nopeasti ympyrämatriisit luodaan eri `circle.m` toteutuksilla

### Muuta

* `energyplotter.m` plottaa energiafunktion arvoja eri paremetreilla

## Annealing-skenaariot

* `annealing.m` -> SA algo-funktio

* `runannealing.m` -> funktio tyypilliseen SA:n ajamiseen (tallentaa datat, jotain alustavia kuvia)

* `runannealingbasicf.m, run_all2.m` etc -> käyttävät runannealing.m eri testidata-filujen ajamiseen

* skenaariolle yhteiset testidatat kansiossa `testdata-shared`
    * sarja valmiiksi generoituja testikuvia
    * testikuvat jne. kansiossa `testdata-images`
    * eri annealing-versioita (= skenaariot) voidaan kokeilla samalle testidatalle ->
    periaatteessa vertailukelpoisuus
    * eri testidatat yms tarpeellinen generoidaan skripteillä `preparetestdata.m` jne

* skriptit kaikkien samaan dataan liittyvien skenaarioiden ajamiseksi nimetty
`runall.m` tjsp

## Muuta

* kansio `analyzetools` : toistaiseksi järjestelemättömiä skriptejä tulosten tutkimiseksi

