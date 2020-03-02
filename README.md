# Python 3 Øvelsesoppgaver
Øvelsesoppgaver i python, fra [IN1900](https://www.uio.no/studier/emner/matnat/ifi/IN1900/h17/ressurser/undervisningsplan.html), med løsningsforslag skrevet i Python 3.7.

## Oppgaver
De fleste oppgavene er hentet fra 5. utgave av "A Primer on Scientific Programming with Python" av Hans Petter Langtangen. Oppgaver fra andre oppgavesett vil være markert med en link til PDFen de kommer fra.

Hver oppgave er nummerert med oppgavenummer, anbefalt filnavn, og sidetall. Oppgavene var gitt som ukentlige innleveringsoppgaver høst 2017. [Her kan du finne en PDF](docs/OppgavePDFer/in1900_exercises_2017.pdf) med alle oppgavene fra boka.

### 1. sett med oppgaver:
- 1.6 (interest_rate.py, side 43)
  - <details><summary>Åpne løsningsforslag</summary>
    <p>
      
    ```python
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
    
    ```
    
    </p>
    </details>
  - [last ned løsningsforslag](docs/kode_løsningsforslag/sett_1/interest_rate.py).
    
- 1.10 (gaussian1.py, side 45)
  - <details><summary>Åpne løsningsforslag</summary>
    <p>

    ```python
    """
    Oppgave 1.10, kick.py, av Anders P. Åsbø.
    
    Dette programmet evaluerer en gitt Gaussisk fordeling ved en gitt x-verdi.
    """
    import numpy as np  # import-komandoer skal stå øverst under doc-stringen.
    
    m = 0  # gjennomsnittsverdi.
    s = 2  # standard-avvik.
    x = 1  # x-verdi.
    
    # beregner funksjonsverdien. Pass på parantesene!
    f = (1.0/(np.sqrt(2*np.pi)*s))*np.exp((-1.0/2)*(((x)-(m))/s)**2)
    print("f(%g) = %g" % (x, f))
    
    # kjøreeksempel:
    """
    In [8]: run gaussian1.py
    f(1) = 0.176033
    """
    # tatt på kalkulator får jeg f(1) = 0.176033.

    ```

    </p>
    </details>
  - [last ned løsningsforslag](docs/kode_løsningsforslag/sett_1/gaussian1.py).
- 1.11 (kick.py, side 45)
  - <details><summary>Åpne løsningsforslag</summary>
    <p>

    ```python
    """
    Oppgave 1.11, kick.py, av Anders P. Åsbø.
    
    Dette programmet beregner tyngde- og luftmotstandskraft på en ball av
    masse m sparket med starthastighet V_1 og V_2.
    """
    from numpy import pi  # importerer bare det jeg skal bruke.
    
    q = 1.2  # lufttetthet [kg/m**3].
    a = 0.11  # radius til ball [m].
    A = pi*a**2.0  # tversnittareal [m**2].
    C_d = 0.4  # luftmotstandskonstant.
    m = 0.43  # masse til ball [kg].
    g = 9.81  # jordas tyngdeaksellerasjon [m/s**2].
    V_1 = 120.0/3.6  # ballens fart ved hardt spark [m/s].
    V_2 = 30.0/3.6  # ballens fart ved svakt spark [m/s].
    
    F_d1 = (1.0/2)*C_d*q*A*(V_1**2)  # luftmotstandskraft ved høy fart [N].
    F_d2 = (1.0/2)*C_d*q*A*(V_2**2)  # luftmotstandskraft ved lav fart [N].
    G = m*g  # ballens tyngde [N].
    R1 = F_d1/G  # luftmotstand per tyngde for høy fart.
    R2 = F_d2/G  # luftmotstand per tyngde for lav fart.
    print("Ballens tyngde er G = %.1f N." % G)
    print("Hardt spark gir F_d = %.1f N, og F_d/G = %.1f" % (F_d1, R1))
    print("Hardt spark gir F_d = %.1f N, og F_d/G = %.1f" % (F_d2, R2))
    
    # kjøreeksempel:
    """
    In [7]: run kick.py
    Ballens tyngde er G = 4.2 N.
    Hardt spark gir F_d = 10.1 N, og F_d/G = 2.4
    Hardt spark gir F_d = 0.6 N, og F_d/G = 0.2
    """
    
    ```

    </p>
    </details>
  - [last ned løsningsforslag](docs/kode_løsningsforslag/sett_1/kick.py).

### 2. sett med oppgaver:
- 2.9 (ball_table2.py, side 83).
- 2.11 (sum_while.py, side 84).
- 2.17 (ball_table3.py, side 86).
- 1.3 (half_life.py, side 5) [fra fysikkheftet](docs/OppgavePDFer/fysikk_oppgaver.pdf).
