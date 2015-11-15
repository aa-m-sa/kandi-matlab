# Kandin koodit

* Muutos 2015-11-15: Siirretty snapshot omaan repoonsa.

* Matlab-yhteensopivaa Octave-koodia: SA-algoritmin toteutus

* Kommentit ja koodi englanniksi (koodarin pinttynyt tapa: lähdekoodi on aina
englanniksi); selvitä pitäisikö sen olla suomeksi jos (kun) se laittaa
liitteenä kandintutkielmaan?

## Koodista

Projektin rakenne on seuraava:

### Algoritmi

* `annealing.m` perusversio SA-algoritmin toteutuksesta

### Apufunktiot jne

* `createdataimage.m` luo simuloitu testidata (annetuin paremetrein). vastaa
tutkielman tekstin 'simuloitu aineisto' mallia

* `circle.m` generoi kuvamatriisin jossa ympyrä / ympyröitä (kuten tutkielman
tekstissä kuvailtu)

* `convolution.m` kuvamallin konvoluutio (ts. pienempi konvoluutiomatriisi),
energiafunktiota varten

* `addnoise.m` palauttaa parametrina annetusta kuvasta version johon lisätty
tasajakautunutta kohinaa

### Testit

* `testscript.m` sekalaista testausta

* `testannealing.m`, `testannealing2.m`, jne. hieman formaalimpia
testiskriptejä algoritmin toiminnan kokeilemiseen (luodaan erilaisia sarjoja
testidataa, kokeillaan SA:ta niihin, printtaa kuvia)

* `testcircle.m` kokeillaan että `circle.m` toimii piirtämällä erilaisia
ympyröitä (nykyinen versio yrittää piirtää torusympyröitä jotka eivät toimi)

* `testcircletime.m` aja `time octave testcircletime.m` -> vertaile kuinka
nopeasti ympyrämatriisit luodaan eri `circle.m` toteutuksilla

### Muuta

* `energyplotter.m` plottaa energiafunktion arvoja eri paremetreilla

## Formaalit testiskenaariot

* perusbranch `matlab`

* jokaiselle skenaarion valmistelulle (`annealing.m`:n muokkaus) oma
git-branch; kun testi valmis ajettevaksi ukko-klusterilla -> merge upstream

* jokaisella skenaariolla nimi: `runannealing(insertdescriptivename)`
    * ajettava skripti: `runannealing(name).m`
    * käyttää `annealing.m`:n versiota `annealing(name).m`
    * tulokset (plottaukset, jne) tallennetaan kansioon `testdata-annealing(name)`
    * skenaarion kuvaus (mitä ko. versio algoritmista tekee;
    jäähdytysskenaariot, alkulämpötilat, jne): `runannealing(name).md`

* skenaariolle yhteiset testidatat kansiossa `testdata-shared`
    * sarja valmiiksi generoituja testikuvia
    * testikuvat jne. kansiossa `testdata-images`
    * eri annealing-versioita (= skenaariot) kokeillaan samalle testidatalle ->
    vertailukelpoisuus
    * generoidaan skriptillä `preparetestdata.m`

* skripti kaikkien skenaarioiden ajamiseksi: `runall`

## Muuta

* kansio `analyzetools` : toistaiseksi järjestelemättömiä skriptejä tulosten tutkimiseksi

