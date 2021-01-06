# Exercise 2.2, Anders P. Åsbø.

F = 0  # startpunkt for temperatur [°F].
dF = 10  # temperaturendring per iterasjon [°F].

print("  F:   |   C:   |   C_approx:")  # printer header.

while F <= 100:  # løper gjennom F i [0°F, 100°F]
    C = (5.0/9.0)*(F - 32)  # Konverterer til °C.
    C_a = (F - 30)/2.0  # Tilnærmer temperatur i °C.

    # printer verdiene:
    print(f"{F:6.2f} | {C:6.2f} | {C_a:6.2f}")
    """
    Her bruker vi f-string formatering til å pynte på utskriften.
    Ta f. eks. {F:6.2f} - 'F' er variabelen vi skal printe,
    ':' separerer det som skal printes fra formateringsinformasjonen,
    '6' er antall plasser utskriften skal ta opp (en plass tilsvarer ett tegn),
    '.2' forteller at vi skal ha to gjeldene siffere etter desimalpunktet, og
    'f' forteller at vi skal printe verdien til 'F' som flyttall (vanlig
    desimaltall).
    """

    F += dF  # dette er det samme som F = F + dF.

# kjøreeksempel:
"""
In [2]: run f2c_approx_table.py
  F:   |   C:   |   C_approx:
  0.00 | -17.78 | -15.00
 10.00 | -12.22 | -10.00
 20.00 |  -6.67 |  -5.00
 30.00 |  -1.11 |   0.00
 40.00 |   4.44 |   5.00
 50.00 |  10.00 |  10.00
 60.00 |  15.56 |  15.00
 70.00 |  21.11 |  20.00
 80.00 |  26.67 |  25.00
 90.00 |  32.22 |  30.00
100.00 |  37.78 |  35.00
"""
