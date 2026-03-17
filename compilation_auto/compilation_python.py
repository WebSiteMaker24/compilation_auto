import sys
import subprocess
import os

# Vérifie qu'on a bien reçu un fichier
if len(sys.argv) < 2:
    print("Usage: compilation_python.py fichier.py")
    input("Appuyez sur Entrée pour quitter...")
    sys.exit(1)

py_file = sys.argv[1]

# Vérifie que le fichier existe
if not os.path.isfile(py_file):
    print(f"Fichier introuvable : {py_file}")
    input("Appuyez sur Entrée pour quitter...")
    sys.exit(1)

# Dossier du fichier
folder = os.path.dirname(os.path.abspath(py_file))
basename = os.path.splitext(os.path.basename(py_file))[0]

# Commande PyInstaller
cmd = [
    sys.executable, "-m", "PyInstaller",
    "--onefile",
    "--noconfirm",
    "--clean",
    py_file,
    "--distpath", folder
]

print(f"Compilation de {py_file} en cours...")
subprocess.run(cmd)

# Supprimer le .spec
spec_file = os.path.join(folder, basename + ".spec")
if os.path.exists(spec_file):
    os.remove(spec_file)

# Rapport mini
exe_path = os.path.join(folder, basename + ".exe")
if os.path.exists(exe_path):
    print(f"✅ Compilation terminée ! .exe créé : {exe_path}")
else:
    print("❌ La compilation a échoué.")

input("Appuyez sur Entrée pour fermer...")
