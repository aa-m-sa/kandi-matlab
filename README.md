# Kandin koodit

* Muutos 2015-11-15: Siirretty koodit omaan Git-repoonsa (snapshot vanhasta
reposta)

* Matlab-yhteensopivaa Octave-koodia: SA-algoritmin toteutus

* Kommentit ja koodi englanniksi (koodarin pinttynyt tapa: lähdekoodi on aina
englanniksi), dokumentaatio yleensä suomeksi

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

## Formaalit testiskenaariot

* perusbranch `master`

* jokaiselle skenaarion valmistelulle (`annealing.m`:n muokkaus) oma
git-branch; kun testi valmis ajettevaksi ukko-klusterilla -> merge upstream

* jokaisella skenaariolla nimi: `runannealing(insertdescriptivename)`
    * ajettava skripti: `runannealing(name).m`
    * jokainen kutsuu `annealing.m` sopivin parametrein
    * tulokset (plottaukset, jne) tallennetaan kansioon `testdata-annealing(name)`
    * skenaarion kuvaus (mitä ko. versio algoritmista tekee;
    jäähdytysskenaariot, alkulämpötilat, jne): `runannealing(name).md`

* skenaariolle yhteiset testidatat kansiossa `testdata-shared`
    * sarja valmiiksi generoituja testikuvia
    * testikuvat jne. kansiossa `testdata-images`
    * eri annealing-versioita (= skenaariot) kokeillaan samalle testidatalle ->
    vertailukelpoisuus
    * generoidaan skriptillä `preparetestdata.m`

* skripti kaikkien skenaarioiden ajamiseksi: `runall` TODO

## Muuta

* kansio `analyzetools` : toistaiseksi järjestelemättömiä skriptejä tulosten tutkimiseksi

