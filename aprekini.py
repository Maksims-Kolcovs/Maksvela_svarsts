# Labaratorijas darbs Nr.1.4 "Inerces momenta noteikšana, izmantojot Maksvela svārstu".
# Aprēķini izmantojot Python programmēšanas valodu.
# Skripta izstrādātāja:
# Maksims Koļcovss
# Karolīna Bucenka

from math import sqrt
# Stjūdentu koeficenti:

Stjudents_Bezgaliba = 1.96
Stjudents_5 = 2.78
Stjudents_10 = 2.96

# Aprēķini bez gredzena (nenoslogota svārsta inerces moments I)
# I = mr^2 (gt^2 / 2h - 1)

g = 9.81  # Brīvās krišanas paātrinājums (m/s^2)
r = 0.005  # radiuss (m)
h = 0.4  # augstums (m)
tvid_1 = 1.36  # laiks vidējais (s)
m = 0.159  # masa (kg)

# Laika rezultāti pie m
t_1 = 1.324  # (s)
t_2 = 1.353  # (s)
t_3 = 1.281  # (s)
t_4 = 1.437  # (s)
t_5 = 1.368  # (s)
t_6 = 1.341  # (s)
t_7 = 1.374  # (s)
t_8 = 1.368  # (s)
t_9 = 1.41  # (s)
t_10 = 1.312  # (s)

# Laika rezultāti pie m_2
t2_1 = 2.052  # (s)
t2_2 = 2.061  # (s)
t2_3 = 2.034  # (s)
t2_4 = 2.074  # (s)
t2_5 = 2.067  # (s)

# Laika rezultāti pie m_3
t3_1 = 2.159  # (s)
t3_2 = 2.135  # (s)
t3_3 = 2.181  # (s)
t3_4 = 2.146  # (s)
t3_5 = 2.126  # (s)

# Inerces moments I1 (bez gredzena)

I1 = m * (r * r) * (g * (tvid_1 * tvid_1) / (2 * h) - 1)

# Aprēķini ar gredzenu (Noslogotais svārsts)
# I = mr^2 (gt^2 / 2h - 1)

m_2 = 0.41816  # masa (kg)
tvid_2 = 2.06  # laiks vidējais (s)

# I kopa ar gredzenu (0.41816 kg)

I_kopa_1 = m_2 * (r * r) * (g * (tvid_2 * tvid_2) / (2 * h) - 1)

# Aprēķini ar gredzenu (Noslogotais svārsts)
# I = mr^2 (gt^2 / 2h - 1)

m_3 = 0.5545  # masa (kg)
tvid_3 = 2.15  # laiks vidējais (s)

# I kopa ar gredzenu (0.5545 kg)

I_kopa_2 = m_3 * (r * r) * (g * (tvid_3 * tvid_3) / (2 * h) - 1)

# Teorētiskā inerces momenta gredzena aprēķins (0.41816 kg)
# Ig teoretiskais = Mg / 8 (D1^2-D2^2)

D1 = 0.085  # Diametrs (metros) - gredzena iekšējais diametrs
D2 = 0.105  # Diametrs (metros) - ārējais diametrs

gredzens_1 = 0.25916  # gredzena svars (kg)
gredzens_2 = 0.5545  # gredzena svars (kg)

Ig1_teoretiski = (gredzens_1 / 8) * ((D1 * D1) * (D2 * D2))

# Teorētiskā inerces momenta gredzena aprēķins (0.5545 kg)
# Ig teoretiskais = Mg / 8 (D1^2-D2^2)

Ig2_teoretiski = (gredzens_2 / 8) * ((D1 * D1) * (D2 * D2))

# Inerces moments Ig
# Ig= Ikop - I

Ig1 = I_kopa_1 - I1
Ig2 = I_kopa_2 - I1


