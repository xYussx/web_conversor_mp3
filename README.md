# 🎵 Conversor de Audio M4A → MP3

Aplicación web para convertir archivos de audio **.m4a** a **.mp3** (320kbps) de forma rápida y sencilla. Ideal para coreografías de baile, donde los reproductores de los colegios requieren formato MP3.

---

## 📋 Requisitos (local)

- **Python** 3.8 o superior
- **ffmpeg** (herramienta del sistema para conversión de audio)

---

## 🔧 Instalación de ffmpeg en Windows

### Opción recomendada: Descarga manual del binario

1. Ve a https://www.gyan.dev/ffmpeg/builds/
2. Descarga **ffmpeg-release-essentials.zip**
3. Extrae el contenido en `C:\ffmpeg`
4. Agrega `C:\ffmpeg\bin` al **PATH** del sistema:
   - Abre "Editar variables de entorno del sistema"
   - Haz clic en **Variables de entorno**
   - En "Variables del sistema", selecciona `Path` y haz clic en **Editar**
   - Haz clic en **Nuevo** y agrega `C:\ffmpeg\bin`
   - Acepta todos los diálogos
5. Abre una **nueva terminal** y verifica con: `ffmpeg -version`

---

## 🚀 Instalación y ejecución local

```bash
# 1. Clona o descarga el proyecto
# 2. Abre una terminal en la carpeta del proyecto

# 3. Crea un entorno virtual (opcional pero recomendado)
python -m venv venv
.\venv\Scripts\activate

# 4. Instala las dependencias
pip install -r requirements.txt

# 5. Ejecuta el servidor
python app.py
```

Abre tu navegador en **http://localhost:5000**

---

## 🌐 Despliegue gratis (sin tarjeta de crédito)

### Opción 1: Render.com (recomendada)

1. Sube el proyecto a **GitHub**
2. Ve a [render.com](https://render.com) → Regístrate con GitHub
3. Dashboard → **New +** → **Blueprint** (o Web Service)
4. Conecta tu repositorio
5. Render detecta automáticamente el `Dockerfile` y construye la imagen
6. En **Start Command** deja vacío (lo define el Dockerfile)
7. Dale en **Deploy**

> ⚠️ En el plan gratis, Render "duerme" el servicio a los 15 min de inactividad. Se despierta solo al entrar (tarda ~30s).

### Opción 2: Hugging Face Spaces (con Docker)

1. Ve a [huggingface.co/spaces](https://huggingface.co/spaces)
2. **Create new Space**
3. Nombre: `conversor-m4a-mp3`
4. **Space SDK**: selecciona **Docker**
5. **Space Hardware**: Free (CPU)
6. Sube los archivos (o conecta GitHub)
7. Hugging Face construye y despliega automáticamente

> ✅ **Diferencia clave:** Hugging Face **NO duerme** los Spaces en el plan gratis (excepto si están inactivos por mucho tiempo). Ideal para uso continuo.

### Opción 3: Docker local

```bash
docker build -t conversor-m4a-mp3 .
docker run -p 5000:7860 conversor-m4a-mp3
```

---

## 📱 Cómo usar

1. Arrastra un archivo `.m4a` al área punteada o haz clic para seleccionarlo
2. La conversión comienza automáticamente
3. Espera a que termine (unos segundos)
4. El archivo `.mp3` se descargará automáticamente

### Compatibilidad
- ✅ **Android** (Chrome, Firefox)
- ✅ **Windows** (Chrome, Edge, Firefox)
- ✅ **iOS** (Safari)
- ✅ **macOS** (Safari, Chrome)

---

## 🛠️ Tecnologías

- **Backend:** Python + Flask + Gunicorn
- **Frontend:** HTML5 + JavaScript vanilla + Tailwind CSS (CDN)
- **Conversión:** ffmpeg con códec libmp3lame a 320kbps
- **Despliegue:** Docker + Render / Hugging Face Spaces

---

## 📝 Notas

- Los archivos subidos se eliminan automáticamente después de la conversión
- No se almacena ningún archivo en el servidor
- El puerto se configura automáticamente mediante la variable de entorno `PORT`
