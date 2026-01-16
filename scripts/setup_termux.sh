#!/data/data/com.termux/files/usr/bin/bash
# scripts/setup_termux.sh

echo "[*] Instalando sistema de hijacking satelital en Termux"

# Actualizar Termux
pkg update -y && pkg upgrade -y

# Instalar dependencias básicas
pkg install python -y
pkg install git -y
pkg install cmake -y
pkg install build-essential -y
pkg install wget -y
pkg install nano -y

# Instalar dependencias de Python
pip install --upgrade pip
pip install numpy
pip install scipy
pip install cryptography
pip install skyfield
pip install requests

# Instalar RTL-SDR (versión parcheada)
echo "[*] Instalando RTL-SDR..."
git clone https://github.com/rtlsdrblog/rtl-sdr-blog
cd rtl-sdr-blog
mkdir build && cd build
cmake ../ -DINSTALL_UDEV_RULES=OFF -DDETACH_KERNEL_DRIVER=OFF
make
cp src/rtl_* $PREFIX/bin/
cd ../..

# Crear estructura de carpetas
echo "[*] Creando estructura de directorios..."
mkdir -p modules utils config data/captured_signals data/decoded_data data/telemetry_logs data/tmp scripts docs tests

# Dar permisos de ejecución
chmod +x scripts/*.sh
chmod +x main_app.py

echo "[+] Instalación completada!"
echo "[-] Ejecutar: python main_app.py --mode test"
