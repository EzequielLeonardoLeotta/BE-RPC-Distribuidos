from servicio_pb2_grpc import LaboratorioFarmaceuticoServicer, add_LaboratorioFarmaceuticoServicer_to_server
from servicio_pb2 import Confirmacion, ListaMedicamentos

import grpc
from concurrent import futures

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "laboratorio"
)

cursor = db.cursor()

class ServicioLaboratorioFarmaceutico(LaboratorioFarmaceuticoServicer):
    
    def Listo(self, request, context):
        return request
    
    def AltaTipoMedicamento(self, request, context):
        tipo = request.tipo
        query = "INSERT INTO tipoMedicamento (tipo) VALUES ('{0}')".format(tipo)
        cursor.execute(query)
        db.commit()
        print(f"Alta de Tipo de Medicamento: {tipo}")
        return Confirmacion("Ok")

    def BajaTipoMedicamento(self, request, context):
        tipo = request.tipo
        query = "UPDATE tipoMedicamento SET activo = 0 WHERE tipo = ('{0}')".format(tipo)
        cursor.execute(query)
        db.commit()
        print(f"Baja de Tipo de Medicamento: {tipo}")
        return Confirmacion("Ok")
    
    def AltaMedicamento(self, request, context):
        query = "INSERT INTO medicamento (codigoAlfabetico, codigoNumerico, digitoVerificador, nombre, droga, tipoMedicamento) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (request.codigoAlfabetico, request.codigoNumerico, request.digitoVerificador, request.nombre, request.droga, request.tipoMedicamento)
        cursor.execute(query, values)
        db.commit()
        print(f"Alta de de Medicamento: {request.nombre}")
        return Confirmacion("Ok")
    
    def TraerMedicamentos(self, request, context):
        print(f"Lista de Medicamentos:")
        return ListaMedicamentos
    
def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_LaboratorioFarmaceuticoServicer_to_server(ServicioLaboratorioFarmaceutico(), server)
    server.add_insecure_port('[::]:50051')
    print("The server is running!")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    start()