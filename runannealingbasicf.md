
# Annealing test run

## Basic version of the algorithm

(Renamed runannealingbasic: data taken for each transition,
not just the final configuarion of a Markov chain)

* max running time: n = 300 markov chains / temperatures
* markov chain length: fixed l = 10
* cut-off thresold: sum of ((accepted / attempted ratios) of the last 4 chains) <= 0.2
* temperature update: t = 0.98*t
* generation of the transition candidate:
    * randomly choose of the candidate circles to be moved
    * delta = max(M/15, N/15) : skaalaa satunnaismuuttuujaa [-1, 1]
    * rnew(toMove) = abs(delta*baseChange + r(toMove));
    * rajoitus: r >= max(N,M) /50, r <= max(N,M)
    * valitse satunnainen suunta, skaalaa keskipisteen siirtymää siihen deltalla
    * ei keskipistettä kuvan ulkopuolelle
* alkulämpötilan valinta:
    * generoidaan 10 satunnaisen siirron ketju (olettaen että kaikki hyväksytään)
    * arvioidaan keskimääräiseksi siirtoon liittyväksi energiaksi yo. siirtojen keskiarvo
* hintafunktio:
    * circle.m
    * päällekkäiset kokeiluympyrät -> negatiivinen arvo
