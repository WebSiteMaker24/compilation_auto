🐍 Python → EXE en un clic

Transforme vos fichiers Python (.py) en exécutables Windows (.exe) facilement, avec PyInstaller et un script de compilation automatique.

⚡ Fonctionnalités

Compilation automatique des .py en .exe

.exe généré dans le même dossier que le fichier source

Suppression automatique du fichier .spec

Mini-rapport affiché après compilation

Option clic droit pour tous les .py

📂 Contenu
Fichier	Description
compilation_python.py	Script Python qui compile le .py en .exe et supprime le .spec.
AjouterClicDroitPyInstaller.reg	Fichier registre pour ajouter l’option clic droit “Compiler avec PyInstaller”.
Makefile	Compilation universelle via terminal pour tous les .py du dossier.
🛠 Prérequis

Python 3.10+

PyInstaller (pip install pyinstaller)

Windows (clic droit fonctionne uniquement sur Windows)

🚀 Installation

Place le script compilation_python.py dans un dossier fixe :

C:\compilation_auto\compilation_python.py


Double-clique sur AjouterClicDroitPyInstaller.reg pour ajouter l’option clic droit.

🖱 Utilisation
Via clic droit

Clique droit sur un .py

Choisis “Compiler avec PyInstaller”

L’exe est créé dans le même dossier que le fichier source

Via terminal / Makefile

Place le Makefile dans le dossier contenant tes scripts .py

Dans le terminal :

make        # Compile tous les .py en .exe
make clean  # Supprime les .exe et .spec


Les .exe sont générés dans dist/.

🔗 Liens utiles

Python : https://www.python.org/downloads/
PyInstaller : https://www.pyinstaller.org/
