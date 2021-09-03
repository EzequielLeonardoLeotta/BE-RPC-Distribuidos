from servicio_pb2_grpc import LaboratorioFarmaceuticoServicer, add_LaboratorioFarmaceuticoServicer_to_server
from servicio_pb2 import Response

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
        try:
            tipo = request.tipo

            #Verifico si ya existe
            queryVerificacion = "SELECT * FROM tipoMedicamento WHERE tipo = '{0}'".format(tipo)
            cursor.execute(queryVerificacion)
            resultado = cursor.fetchall()
            
            if(resultado == []):
                query = "INSERT INTO tipoMedicamento (tipo) VALUES ('{0}')".format(tipo)
                cursor.execute(query)
                db.commit()
                print(f"Alta de Tipo de Medicamento: {tipo}")
                return Response(message = "Alta de Tipo de Medicamento: '{0}'".format(tipo))
            else:
                print(f"Error al dar de alta el Tipo de Medicamento: {tipo}, porque ya existe")
                return Response(message = "Error: el tipo de medicamento ya existe")
        except:
            print(f"Error al dar de alta el Tipo de Medicamento: {tipo}")
            return Response(message = "Error")

    def BajaTipoMedicamento(self, request, context):
        try:
            tipo = request.tipo
            query = "UPDATE tipoMedicamento SET activo = 0 WHERE tipo = ('{0}')".format(tipo)
            cursor.execute(query)
            db.commit()
            print(f"Baja de Tipo de Medicamento: {tipo}")
            return Response(message = "Ok")
        except:
            print(f"Error al dar de baja el Tipo de Medicamento: {tipo}")
            return Response(message = "Error")

    def AltaMedicamento(self, request, context):
        try:
            query = "INSERT INTO medicamento (codigoAlfabetico, codigoNumerico, digitoVerificador, nombre, droga, tipoMedicamento) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (request.codigoAlfabetico, request.codigoNumerico, request.digitoVerificador, request.nombre, request.droga, request.tipoMedicamento)
            cursor.execute(query, values)
            db.commit()
            print(f"Alta de de Medicamento: {request.nombre}")
            return Response(message = "Ok")
        except:
            print(f"Error al dar de alta el Medicamento: {request.nombre}")
            return Response(message = "Error")
        
    def TraerAerosoles(self, request, context):
        try:
            #Obtengo el id de aerosoles
            queryGetIdAerosoles = "SELECT id FROM tipoMedicamento WHERE tipo = 'aerosoles'"
            cursor.execute(queryGetIdAerosoles)
            records = cursor.fetchall()
            idAerosoles = records[0][0]
           
            #Obtengo los medicamentos de tipo aerosoles
            query = "SELECT * FROM medicamento WHERE tipoMedicamento = {0}".format(idAerosoles)
            cursor.execute(query)
            aerosoles = cursor.fetchall()
            print(f"Traer aerosoles")
            return Response(message = str(aerosoles))
        except:
            print(f"Error al traer aerosoles")
            return Response(message = "Error")

    def TraerMedicamenosConA(self, request, context):
        try:
            query = "SELECT * FROM tipoMedicamento WHERE tipo  LIKE 'a%'"
            cursor.execute(query)
            medicamentos = cursor.fetchall()
            print(f"Traer Medicamentos que empiezan con A")
            return Response(message = str(medicamentos))
        except:
            print(f"Error al traer Medicamentos que empiezan con A")
            return Response(message = "Error")
    
def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_LaboratorioFarmaceuticoServicer_to_server(ServicioLaboratorioFarmaceutico(), server)
    server.add_insecure_port('[::]:50051')
    print("The server is running!")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    start()