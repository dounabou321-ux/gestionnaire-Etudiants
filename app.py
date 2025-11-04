etudiants ={
    "Ali": [14, 12, 18],
    "Sara": [9, 7, 11],
    "Dounia": [17, 19, 15],
    "Karim": [8, 6, 10],
    "Nadia": [13, 15, 12]
}
def calculer_moyenne(notes):
    moyenne = sum(notes) / len(notes)
    return moyenne
def statut(moyenne):
    if moyenne >= 10:
        return "Admis"
    else:
        return "Refusé"
for nom, notes in etudiants.items():
    moyenne = calculer_moyenne(notes)
    resultat = statut(moyenne)
    print(f"{nom}: Moyenne = {moyenne:.2f}, Statut = {resultat}")
classement = sorted(
    etudiants.items(),
    key=lambda etudiant: calculer_moyenne(etudiant[1]),
    reverse=True
)
for i, (nom, notes) in enumerate(classement, 1):
    print(f"{i}. {nom} — Moyenne : {calculer_moyenne(notes):.2f}")
admis = [nom for nom, notes in etudiants.items() if calculer_moyenne(notes) >= 10]

for nom in admis:
    print(nom)

