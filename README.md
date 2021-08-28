Instalar Python:
https://www.python.org/downloads/

Abrir el proyecto con VSC

Ir a la ruta del servidor:
cd servidor/

Instalar pip:
py -m ensurepip --upgrade

Actualizar pip:
python -m pip install --upgrade pip

Crear virtualenv:
virtualenv venv

Activar scripts:
source venv/Scripts/activate

Instalar grpcio:
pip install grpcio

Instalar grpcio-tools:
pip install grpcio-tools

Generar servidor:
python -m grpc_tools.protoc -I../definiciones --python_out=. --grpc_python_out=. ../definiciones/servicio.proto

Correr servidor:
python ./servidor.py