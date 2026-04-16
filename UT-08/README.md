
# Crear un  proyecto

## Crear proyecto con Nuxi

npx: Es parte de npm y descarga y ejecuta el paquete sin dejarlo instalado.

nuxi: Es la interfaz de línea de comandos (CLI) oficial de Nuxt.

init: Le dice a Nuxt que quieres inicializar un proyecto nuevo.

```
npx nuxi@latest init <nombre del proyecto>
```

## Dependencias y lanzar servidor

install: Lee el archivo package.json y descarga todas las herramientas necesarias (como el propio Vue)
dev: Compila la aplicación y levanta un servidor local (en http://localhost:3000).

```
cd <nombre del proyecto>
npm install
npm run dev
```

### En producción

```
npm run build
node .output/server/index.mjs
```

## Si falla (fallará)

Instalar una versión reciente de 

```
# eliminar versión antigua

sudo apt-get remove --purge nodejs npm
sudo apt-get autoremove

# Instalar versión reciente
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc

# Comprobar versión de nvm instalada
nvm --version

# Listar las versiones instaladas
nvm ls

#  Instalar node LTS
nvm install 22.22.2

```