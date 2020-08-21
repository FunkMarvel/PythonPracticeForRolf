"""
Oppgave 2.11, sum_while.py, Anders P. Åsbø.
Dette programet beregner en sum med en while-løkke. Den orginale implimentasjonen var buggy,
så filen inneholder først en kopi av orginalkoden hvor bugsene er påpekt, så en funksjonell omskrivning av koden.
"""

# orginalversjon av kode:
"""
s = 0; k = 1; M = 100

while k < M:  # while-løkken går bare for k<M, når den skulle gå for k<=M.
    s += 1/k  # fordi k sin verdi er den samme hver iterasjon, så vil løkken aldri stoppe.

print s #  dette er python 2 syntax, og vil ikke fungere i python 3.
"""

#  forsøk på å fikse koden:
s, k, M = 0, 1, 100

while k <= M:  # løkken løper nå gjennom alle k<=M.
    s += 1.0/k
    k += 1  # øker verdien til k med 1, slik at løkken tilslutt stopper.

print(s)  # print-funksjon i riktig syntax.

# kjøreeksempel:
"""
run sum_while.py
5.187377517639621
"""
