# BE-RPC-Distribuidos

### Instalar Python

https://www.python.org/downloads/

### Abrir el proyecto con VSC

### Ir a la ruta del servidor

_cd servidor/_

### Instalar pip

_py -m ensurepip --upgrade_

### Actualizar pip

_python -m pip install --upgrade pip_

### Crear virtualenv

_virtualenv venv_

### Activar scripts

_source venv/Scripts/activate_

### Instalar grpcio

_pip install grpcio_

### Instalar grpcio-tools

_pip install grpcio-tools_

### Generar servidor

_python -m grpc_tools.protoc -I../definiciones --python_out=. --grpc_python_out=. ../definiciones/servicio.proto_

### Correr servidor

_python ./servidor.py_
