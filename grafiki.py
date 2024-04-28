import matplotlib.pyplot as plt

# Dati
masas = [0.159, 0.41816, 0.5545]
inerces_momenti = [8.618086200000002e-05, 0.00053354231383, 0.0007719112191406249]
energijas = [0.623916, 1.64085984, 2.1758580000000003]

# Inerces momenta grafiks
plt.figure(figsize=(10, 5))
plt.plot(masas, inerces_momenti, marker='o')
plt.title('Inerces moments atkarībā no masas')
plt.xlabel('Masa (kg)')
plt.ylabel('Inerces moments (kg*m^2)')
plt.grid(True)
plt.show()

# Enerģijas grafiks
plt.figure(figsize=(10, 5))
plt.plot(masas, energijas, marker='o', color='r')
plt.title('Enerģija atkarībā no masas')
plt.xlabel('Masa (kg)')
plt.ylabel('Enerģija (J)')
plt.grid(True)
plt.show()
