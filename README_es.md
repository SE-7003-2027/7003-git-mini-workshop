Aquí tienes la traducción del README manteniendo todos los tecnicismos en inglés:

# Git Mini Workshop

¡Bienvenido al taller de Git! En esta tarea práctica aprenderás a hacer **fork**, trabajar con **feature branches**, seguir los éstandares de **commit**, resolver **merge conflicts** y abrir un **Pull Request (PR)**.

Para proteger tus datos personales en este repositorio público, **no escribas tu nombre real ni tu ID de estudiante en ningún archivo**. Utilizarás un hash anónimo generado por un script local de Python.

---

## 🛠️ Prerequisitos

Asegúrate de tener instaladas las siguientes herramientas en tu máquina local:

* [Git](https://git-scm.com/)
* [Python 3.x](https://www.python.org/)
* Un editor de código (por ejemplo, VS Code, Neovim, Emacs)

---

## 📑 Instrucciones paso a paso

### Step 1: Clona el Repositorio

1. Haz clic en el botón **Code** en la esquina superior derecha de esta página de GitHub para obtener el enlace de este repositorio.
2. Clona el repositorio:

```bash
git clone https://github.com/MarisolAL/7003-git-mini-workshop.git
cd 7003-git-mini-workshop

```

O puedes usar GitHub CLI:

```bash
gh repo clone MarisolAL/7003-git-mini-workshop

```

### Step 2: Genera tu Hash Anónimo

Ejecuta el script interactivo de Python incluido en el repositorio para generar tu hash ID único:

```bash
python3 scripts/generate_hash.py

```

El script te pedirá tu nombre completo y ID universitario, y devolverá un Hash ID de 12 caracteres (por ejemplo, `a5b8f7e29c1d`). ¡Guarda este hash!

### Step 3: Crea una Feature Branch

Crea y cámbiate a una nueva branch. El nombre de tu branch DEBE seguir este formato: `<hash>-profile`

```bash
# Ejemplo: si tu hash es a5b8f7e29c1d
git switch -c a5b8f7e29c1d-profile

```

### Step 4: Realiza tus Cambios

Debes actualizar solo dos archivos en el directorio `profiles/`:

1. Crea tu archivo de perfil individual (`profiles/<hash>.json`):
Crea un nuevo archivo llamado `profiles/<tu-hash>.json` usando la siguiente plantilla:

```json
{
  "hash_id": "TU_HASH_AQUÍ",
  "favorite_language": "Python",
  "favorite_git_command": "git status",
  "learning_goal": "Destroy prod without traces~"
}

```

2. Agrega tu hash al directorio compartido (`profiles/all-da-people.json`):
Abre `profiles/all-da-people.json` y añade la entrada de tu hash al array.

⚠️ **Nota sobre Merge Conflicts**: Dado que todos los estudiantes están editando `profiles/all-da-people.json`, es posible que te encuentres con un merge conflict al hacer merge de los cambios de upstream. Consulta la sección de conflictos más abajo si es necesario.

### Step 5: Stage y Commit solo de los cambios necesarios

No hagas commit de archivos sin seguimiento (untracked) ni temporales. Haz stage ÚNICAMENTE de tus dos archivos modificados/creados en la carpeta `profiles/`:

```bash
git add profiles/<tu-hash>.json profiles/all-da-people.json

```

#### (,; ⩌ ;,) Guía para tu Commit Message 🐤

Tu mensaje de commit debe seguir el formato de Conventional Commits:

* Formato del título: `<type>(<scope>): <short summary>`
* Tipos permitidos: `feat` (nueva característica), `fix` (corrección de errores), `docs` (actualizaciones de documentación).
* Scope: `profile`

Ejemplos válidos:

* `feat(profile): add profile for hash a5b8f7e29c1d`
* `docs(profile): update profile details`

Crea tu commit:

```bash
git commit -m "feat(profile): add profile for hash <tu-hash>"

```

### Step 6: Push a tu branch y abre un PR

1. Haz push de tu branch a tu remoto en GitHub:

```bash
git push -u origin <tu-hash>-profile

```

2. Navega al repositorio en GitHub.
3. Verás un banner que dice "Compare & pull request". Haz clic en él.

#### ദ്ദി◝ ⩊ ◜.ᐟ Pull Request Guidelines 🪷

* Título del PR: Debe coincidir con el formato de tu commit: `feat(profile): add profile for hash <tu-hash>`
* Descripción del PR: Completa el template de Pull Request proporcionado en su totalidad.
* Verifica que el chequeo automatizado de `Privacy & PII Guardrail` pase correctamente.

### 🔒 Privacy Notice

* Nunca hagas commit de tu nombre real, ID de estudiante o correo electrónico personal (@my.mail o cualquier otro dominio).
* Los PRs serán revisados en diferentes momentos, así que actualiza tus branches con frecuencia:

```bash
git fetch --all
```