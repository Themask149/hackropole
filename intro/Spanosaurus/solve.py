import matplotlib.pyplot as plt
import pandas as pd

# Chargement des données de la trace de l'utilisateur
file_path_user = './trace_utilisateur.csv'
trace_user_data = pd.read_csv(file_path_user, header=None)
trace_user_data.columns = ['Energy Consumption User']

# Chargement des données de la trace de l'administrateur
file_path_admin = './trace_admin.csv'
trace_admin_data = pd.read_csv(file_path_admin, header=None)
trace_admin_data.columns = ['Energy Consumption Admin']

# Création du graphique
plt.figure(figsize=(15, 6))

# Tracé de la courbe de l'administrateur
plt.plot(trace_admin_data['Energy Consumption Admin'], label='Administrateur', color='red')

# Tracé de la courbe de l'utilisateur
# plt.plot(trace_user_data['Energy Consumption User'], label='Utilisateur', color='blue')

# Ajout du titre et des légendes
plt.title('Comparaison des Traces de Consommation d\'Énergie - Utilisateur vs Administrateur')
plt.xlabel('Temps')
plt.ylabel('Consommation d\'Énergie')
plt.legend()

# Affichage du graphique
plt.grid(True)
plt.show()
