# Labaratorijas darbs Nr.1.4 "Inerces momenta noteikšana, izmantojot Maksvela svārstu".
# Aprēķini izmantojot Python programmēšanas valodu.
# Skriptu izstrādātāja:

# Maksims Koļcovss
# Karolīna Bucenka

from math import sqrt
from sympy import symbols, diff

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


# Enerģijas nezudamības likums

# Kīnetiskā enerģija sākumā pie standartmasas,m_2,m_3
Wk0 = 0  # (J)
# Potenciāla enerģija sākumā pie standartmasas
# Wp0=mgh
Wp0_pie_m = m * g * h  # (J)
# Potenciāla enerģija sākuma pie m_2
# Wp0=mgh
Wp0_pie_m2 = m_2 * g * h  # (J)
# Potenciāla enerģija sākumā pie m_3
# Wp0=mgh
Wp0_pie_m3 = m_3 * g * h  # (J)

#Kīnetiskā enerģija beigās pie standartmasas
Wkb_pie_m = (m + I1 / (r * r)) * 2 * (h * h) / (tvid_1 * tvid_1)  # (J)
#Kīnetiskā enerģija beigās pie m_2
Wkb_pie_m2 = (m_2 + I_kopa_1 /
              (r * r)) * 2 * (h * h) / (tvid_2 * tvid_2)  # (J)
#Kīnetiskā enerģija beigās pie m_3
Wkb_pie_m3 = (m_3 + I_kopa_2 /
              (r * r)) * 2 * (h * h) / (tvid_3 * tvid_3)  # (J)

# Potenciālā enerģija beigās pie standartmasas,m_2,m_3
Wpb = 0  # (J)




# Kļūdas aprēķiņi laikam

# Kļūdas aprēķiņi laikam t pie standartmasas
# Vidēja kvadratiskā kļūda

Videja_kvadratiska_kluda_m = sqrt(
    ((t_1 - tvid_1) * (t_1 - tvid_1) + (t_2 - tvid_1) * (t_2 - tvid_1) +
     (t_3 - tvid_1) * (t_3 - tvid_1) + (t_4 - tvid_1) * (t_4 - tvid_1) +
     (t_5 - tvid_1) * (t_5 - tvid_1) + (t_6 - tvid_1) * (t_6 - tvid_1) +
     (t_7 - tvid_1) * (t_7 - tvid_1) + (t_8 - tvid_1) * (t_8 - tvid_1) +
     (t_9 - tvid_1) * (t_9 - tvid_1) + (t_10 - tvid_1) * (t_10 - tvid_1)) /
    (10 * (10 - 1)))  # (s)

# Gadījumā kļūda
Gadijuma_kluda_m = Videja_kvadratiska_kluda_m * Stjudents_10  #(s)

# Sistemātiskā kļūda
# mazāka iedaļas vertība =0.001
mv = 0.001
Sistematiska_kluda_m = mv / 3 * Stjudents_Bezgaliba  #(s)

# Absolūta kļūda

if Gadijuma_kluda_m <= Sistematiska_kluda_m:
  Absoluta_kluda_m = Sistematiska_kluda_m  #(s)

elif Gadijuma_kluda_m > Sistematiska_kluda_m:
  Absoluta_kluda_m = Gadijuma_kluda_m  #(s)

# Relatīvā kļūda

Relativa_kluda_m = Absoluta_kluda_m / tvid_1 * 100  #(s)

# Kļūdas aprēķiņi laikam t pie m_2
# Vidēja kvadratiskā kļūda

Videja_kvadratiska_kluda_m2 = sqrt(
    ((t2_1 - tvid_2) * (t2_1 - tvid_2) + (t2_2 - tvid_2) * (t2_2 - tvid_2) +
     (t2_3 - tvid_2) * (t2_3 - tvid_2) + (t2_4 - tvid_2) * (t2_4 - tvid_2) +
     (t2_5 - tvid_2) * (t2_5 - tvid_2)) / (5 * (5 - 1)))  # (s)

# Gadījumā kļūda
Gadijuma_kluda_m2 = Videja_kvadratiska_kluda_m2 * Stjudents_5  #(s)

# Sistemātiskā kļūda
# mazāka iedaļas vertība =0.001
mv2 = 0.001
Sistematiska_kluda_m2 = mv2 / 3 * Stjudents_Bezgaliba  #(s)

# Absolūta kļūda

if Gadijuma_kluda_m2 <= Sistematiska_kluda_m2:
  Absoluta_kluda_m2 = Sistematiska_kluda_m2  #(s)

elif Gadijuma_kluda_m2 > Sistematiska_kluda_m2:
  Absoluta_kluda_m2 = Gadijuma_kluda_m2  #(s)

# Relatīvā kļūda

Relativa_kluda_m2 = Absoluta_kluda_m2 / tvid_2 * 100  #(s)

# Kļūdas aprēķiņi laikam t pie m_3
# Vidēja kvadratiskā kļūda

Videja_kvadratiska_kluda_m3 = sqrt(
    ((t3_1 - tvid_3) * (t3_1 - tvid_3) + (t3_2 - tvid_3) * (t3_2 - tvid_3) +
     (t3_3 - tvid_3) * (t3_3 - tvid_3) + (t3_4 - tvid_3) * (t3_4 - tvid_3) +
     (t3_5 - tvid_3) * (t3_5 - tvid_3)) / (5 * (5 - 1)))  # (s)

# Gadījumā kļūda
Gadijuma_kluda_m3 = Videja_kvadratiska_kluda_m3 * Stjudents_5  #(s)

# Sistemātiskā kļūda
# mazāka iedaļas vertība =0.001
mv3 = 0.001
Sistematiska_kluda_m3 = mv / 3 * Stjudents_Bezgaliba  #(s)

# Absolūta kļūda

if Gadijuma_kluda_m3 <= Sistematiska_kluda_m3:
  Absoluta_kluda_m3 = Sistematiska_kluda_m3  #(s)

elif Gadijuma_kluda_m3 > Sistematiska_kluda_m3:
  Absoluta_kluda_m3 = Gadijuma_kluda_m3  #(s)

# Relatīvā kļūda

Relativa_kluda_m3 = Absoluta_kluda_m3 / tvid_3 * 100  #(s)

# Sistematiskas kļūdas apŗēķins m, h, D1, 

mv4 = 0.001

# Sistemātiskās kļūdas aprēķins
Sistematiska_kluda_m = mv4 / 3 * Stjudents_Bezgaliba
Sistematiska_kluda_h = mv4 / 3 * Stjudents_Bezgaliba
Sistematiska_kluda_d = mv4 / 3 * Stjudents_Bezgaliba

# Relatīvās kļūdas aprēķins
Relativa_kluda_m = Sistematiska_kluda_m / m * 100
Relativa_kluda_h = Sistematiska_kluda_h / h * 100
Relativa_kluda_d1 = Sistematiska_kluda_d / D1 * 100
Relativa_kluda_d2 = Sistematiska_kluda_d / D2 * 100



# Kļūdas aprēķiņi inercei

# Sistematiskās kļūdas aprēķins
Sistematiska_kluda_I1 = sqrt((Relativa_kluda_m / 100 * I1)**2 + (2 * Relativa_kluda_m3 / 100 * I1)**2 + (Relativa_kluda_h / 100 * I1)**2)

# Absolūtās kļūdas aprēķins
Absoluta_kluda_I1 = Sistematiska_kluda_I1

# Relatīvās kļūdas aprēķins
Relativa_kluda_I1 = Absoluta_kluda_I1 / I1 * 100

# Sistematiskās kļūdas aprēķins
Sistematiska_kluda_I_kopa_1 = sqrt((Relativa_kluda_m2 / 100 * I_kopa_1)**2 + (2 * Relativa_kluda_m3 / 100 * I_kopa_1)**2 + (Relativa_kluda_h / 100 * I_kopa_1)**2)

# Absolūtās kļūdas aprēķins
Absoluta_kluda_I_kopa_1 = Sistematiska_kluda_I_kopa_1

# Relatīvās kļūdas aprēķins
Relativa_kluda_I_kopa_1 = Absoluta_kluda_I_kopa_1 / I_kopa_1 * 100

# Sistematiskās kļūdas aprēķins
Sistematiska_kluda_I_kopa_2 = sqrt((Relativa_kluda_m3 / 100 * I_kopa_2)**2 + (2 * Relativa_kluda_m3 / 100 * I_kopa_2)**2 + (Relativa_kluda_h / 100 * I_kopa_2)**2)

# Absolūtās kļūdas aprēķins
Absoluta_kluda_I_kopa_2 = Sistematiska_kluda_I_kopa_2

# Relatīvās kļūdas aprēķins
Relativa_kluda_I_kopa_2 = Absoluta_kluda_I_kopa_2 / I_kopa_2 * 100

# Sistematiskās kļūdas aprēķins
Sistematiska_kluda_Ig1 = sqrt((Relativa_kluda_m2 / 100 * Ig1)**2 + (2 * Relativa_kluda_m3 / 100 * Ig1)**2 + (Relativa_kluda_h / 100 * Ig1)**2)

# Absolūtās kļūdas aprēķins
Absoluta_kluda_Ig1 = Sistematiska_kluda_Ig1

# Relatīvās kļūdas aprēķins
Relativa_kluda_Ig1 = Absoluta_kluda_Ig1 / Ig1 * 100

# Sistematiskās kļūdas aprēķins
Sistematiska_kluda_Ig2 = sqrt((Relativa_kluda_m3 / 100 * Ig2)**2 + (2 * Relativa_kluda_m3 / 100 * Ig2)**2 + (Relativa_kluda_h / 100 * Ig2)**2)

# Absolūtās kļūdas aprēķins
Absoluta_kluda_Ig2 = Sistematiska_kluda_Ig2

# Relatīvās kļūdas aprēķins
Relativa_kluda_Ig2 = Absoluta_kluda_Ig2 / Ig2 * 100



# Parciāla atvasināšana 

# Definē mainīgos
m, r, g, t, h, m_kopa, t_kopa, I1, I_kopa_1 = symbols('m r g t h m_kopa t_kopa I1 I_kopa_1')

# Definē funkciju I un atvasina to pēc laika t
I = m * (r * r) * (g * (t * t) / (2 * h) - 1)
dI_dt = diff(I, t)

# Definē funkciju I_kopa un atvasina to pēc laika t_kopa
I_kopa = m_kopa * (r * r) * (g * (t_kopa * t_kopa) / (2 * h) - 1)
dI_kopa_dt_kopa = diff(I_kopa, t_kopa)

# Definē funkciju Ig1 un atvasina to pēc laika t
Ig1 = I_kopa_1 - I1
dIg1_dt = diff(Ig1, t)







# Saglabāšana teksta datnē ar mērvienībām
with open('rezultati.txt', 'w', encoding='utf-8') as f:
  f.write(f"Inerces moments I1 (bez gredzena): {I1} kg*m^2\n")
  f.write(
      f"Inerces moments I kopa ar gredzenu (0.41816 kg): {I_kopa_1} kg*m^2\n")
  f.write(
      f"Inerces moments I kopa ar gredzenu (0.5545 kg): {I_kopa_2} kg*m^2\n")
  f.write(
      f"Teorētiskā inerces momenta gredzena aprēķins (0.41816 kg): {Ig1_teoretiski} kg*m^2\n"
  )
  f.write(
      f"Teorētiskā inerces momenta gredzena aprēķins (0.5545 kg): {Ig2_teoretiski} kg*m^2\n"
  )
  f.write(f"Inerces moments Ig (0.41816 kg): {Ig1} kg*m^2\n")
  f.write(f"Inerces moments Ig (0.5545 kg): {Ig2} kg*m^2\n")
  f.write(
      f"Potenciāla enerģija pie standartmasas (Wp0_m=6.2392E-01): {Wp0_pie_m} J\n"
  )
  f.write(f"Potenciāla enerģija pie m_2 (Wp0_m2=1.6409E+00): {Wp0_pie_m2} J\n")
  f.write(f"Potenciāla enerģija pie m_3 (Wp0_m3=2.1759E+00): {Wp0_pie_m3} J\n")
  f.write(
      f"Kīnetiskā enerģija pie standartmasas (Wkb_m=6.2392E-01): {Wkb_pie_m} J\n"
  )
  f.write(f"Kīnetiskā enerģija pie m_2 (Wkb_m2=1.6409E+00): {Wkb_pie_m2} J\n")
  f.write(f"Kīnetiskā enerģija pie m_3 (Wkb_m3=2.1759E+00): {Wkb_pie_m3} J\n")
  f.write(
      f"Enerģijas nezudamības likums pie m (Wk0 + Wp0 = Wkb + Wpb): {Wp0_pie_m} + {Wk0} = {Wkb_pie_m} + {Wpb} \n"
  )
  f.write(
      f"Enerģijas nezudamības likums pie m_2 (Wk0 + Wp0 = Wkb + Wpb): {Wp0_pie_m2} + {Wk0} = {Wkb_pie_m2} + {Wpb} \n"
  )
  f.write(
      f"Enerģijas nezudamības likums pie m_3 (Wk0 + Wp0 = Wkb + Wpb): {Wp0_pie_m3} + {Wk0} = {Wkb_pie_m3} + {Wpb} \n"
  )

  f.write(
      f"Vidējā kvadratiskā kļūda pie m (0.01449): {Videja_kvadratiska_kluda_m} s\n"
  )
  f.write(f"Gadījumā kļūda m (0.04290): {Gadijuma_kluda_m} s\n")
  f.write(
      f"Sistematiskā kļūda pie m (0.000653333): {Sistematiska_kluda_m} s\n")
  f.write(f"Absolūta kļūda pie m (0.04290): {Absoluta_kluda_m} s\n")
  f.write(f"Relatīva kļūda pie m (3.161851415): {Relativa_kluda_m} s\n")

  f.write(
      f"Vidējā kvadratiskā kļūda pie m_2 (0.00692): {Videja_kvadratiska_kluda_m2} s\n"
  )
  f.write(f"Gadījumā kļūda m_2 (0.01923): {Gadijuma_kluda_m2} s\n")
  f.write(
      f"Sistematiskā kļūda pie m_2 (0.000653333): {Sistematiska_kluda_m2} s\n")
  f.write(f"Absolūta kļūda m2 (0.01923): {Absoluta_kluda_m2} s\n")
  f.write(f"Relatīva kļūda pie m_2 (0.934583981): {Relativa_kluda_m2} s\n")

  f.write(
      f"Vidējā kvadratiskā kļūda pie m_3 (0.00964): {Videja_kvadratiska_kluda_m3} s\n"
  )
  f.write(f"Gadījumā kļūda m_3 (0.02679): {Gadijuma_kluda_m3} s\n")
  f.write(
      f"Sistematiskā kļūda pie m_3 (0.000653333): {Sistematiska_kluda_m3} s\n")
  f.write(f"Absolūta kļūda m3 (0.02679): {Absoluta_kluda_m3} s\n")
  f.write(f"Relatīva kļūda pie m_3 (1.246394343): {Relativa_kluda_m3} s\n")
 
 
  f.write(f"Masas m relatīvā kļūda: {Relativa_kluda_m}%\n")
  f.write(f"Augstuma h relatīvā kļūda: {Relativa_kluda_h}%\n")
  f.write(f"Diametra D1 relatīvā kļūda: {Relativa_kluda_d1}%\n")
  f.write(f"Diametra D2 relatīvā kļūda: {Relativa_kluda_d2}%\n")

  f.write(f"Sistematiskā kļūda I1: {Sistematiska_kluda_I1} kg*m^2\n")
  f.write(f"Absolūtā kļūda I1: {Absoluta_kluda_I1} kg*m^2\n")
  f.write(f"Relatīvā kļūda I1: {Relativa_kluda_I1}%\n")
  f.write(f"Sistematiskā kļūda I_kopa_1: {Sistematiska_kluda_I_kopa_1} kg*m^2\n")
  f.write(f"Absolūtā kļūda I_kopa_1: {Absoluta_kluda_I_kopa_1} kg*m^2\n")
  f.write(f"Relatīvā kļūda I_kopa_1: {Relativa_kluda_I_kopa_1}%\n")
  f.write(f"Sistematiskā kļūda I_kopa_2: {Sistematiska_kluda_I_kopa_2} kg*m^2\n")
  f.write(f"Absolūtā kļūda I_kopa_2: {Absoluta_kluda_I_kopa_2} kg*m^2\n")
  f.write(f"Relatīvā kļūda I_kopa_2: {Relativa_kluda_I_kopa_2}%\n")
  f.write(f"Sistematiskā kļūda Ig1: {Sistematiska_kluda_Ig1} kg*m^2\n")
  f.write(f"Absolūtā kļūda Ig1: {Absoluta_kluda_Ig1} kg*m^2\n")
  f.write(f"Relatīvā kļūda Ig1: {Relativa_kluda_Ig1}%\n")
  f.write(f"Sistematiskā kļūda Ig2: {Sistematiska_kluda_Ig2} kg*m^2\n")
  f.write(f"Absolūtā kļūda Ig2: {Absoluta_kluda_Ig2} kg*m^2\n")
  f.write(f"Relatīvā kļūda Ig2: {Relativa_kluda_Ig2}%\n")
  f.write(f"Atvasinājums funkcijai I pēc laika t: {dI_dt}\n")
  f.write(f"Atvasinājums funkcijai I_kopa pēc laika t_kopa: {dI_kopa_dt_kopa}\n")
  f.write(f"Atvasinājums funkcijai Ig1 pēc laika t: {dIg1_dt}\n")

