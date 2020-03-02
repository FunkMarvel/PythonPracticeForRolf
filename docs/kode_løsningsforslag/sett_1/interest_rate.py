"""
Oppgave 1.6, interest_rate.py, av Anders P. Åsbø.

Dette er en "doc-string" som skal stå øverst i programmet.
Den skal kort dokumentere hva koden gjør:
Denne koden beregner A(1+p/100)^n.
Det kan også være lurt å inkludere oppgavenummer i doc-stringen hvis
programmet er del av en besvarelse.
"""

"""
Når man lager variabler er det lurt å inkludere kommentarer som forteller hva
variablene representerer. Enheter skrives i firkant-parantes i kommentaren [m].
Det er også lurt med kommentarer hvor koden gjør en viktig beregning, e.l.
Linjer i koden bør ikke være mer enn 79 tegn lange.
"""
p = 5  # 5% rente.
A = 1000  # startbeløp [€].
n = 3  # tid på konto [år].

B = A*((1 + p/100)**(n))  # beregner nytt beløp.
print("Etter %g år har beløpet vokst til €%g." % (n, B))  # printer resultat.

# kjøreeksempel:
"""
In [4]: run interest_rate.py
Etter 3 år har beløpet vokst til €1157.63.
"""

"""
Alle innleverte kodefiler burde inkludere et kjøreeksempel i bunnen av filen,
som er en kopi av kommandoen som kjører programmet, og
resultatet som printes i terminalen når programmet kjøres.

Hvis programmet ikke printer til terminalen, så skal fortsatt run-kommandoen
inkluderes i kjøreeksempelet sammen med det tomme outputtet, for å vise at
programmet faktisk ikke printet noe når eleven kjørte koden.

Hvis programmet åpner ett eller flere plot, så må dette nevnes under
kjøreeksempelet. See kjøreeksempel-eksempelet under.
"""

# kjøreeksempel:
"""
In [4]: run plot_program.py
"""
# Det åpnes 2 plot.
