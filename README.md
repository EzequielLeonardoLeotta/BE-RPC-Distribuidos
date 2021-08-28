# BE-RPC-Distribuidos

## Parte 1: Python

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

### Correr el servidor

_python ./servidor.py_

## Parte 2: .Net

### Instalar el SDK de Net 5.0

https://dotnet.microsoft.com/download

### Instalar grpc

_gem install grpc_

### Ir a la ruta del cliente

_cd ../cliente_

### Instalar CommonProtos

_dotnet add package Google.Api.CommonProtos_

### Instalar Grpc.Net.Client

_dotnet add package Grpc.Net.Client_

### Instalar Grpc.Tools

_dotnet add package Grpc.Tools_

### Instalar Grpc.Core

_dotnet add package Grpc.Core_

### Buildear el cliente

_dotnet build_

### Correr el cliente

_dotnet run_

## Comandos para correr cliente y servidor

### Correr el servidor

_python ./servidor.py_

### Correr el cliente

_dotnet run_