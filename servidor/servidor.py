from servicio_pb2_grpc import LaboratorioFarmaceuticoServicer, add_LaboratorioFarmaceuticoServicer_to_server
from servicio_pb2 import Confirmacion, ListaMedicamentos

import grpc
from concurrent import futures

class ServicioLaboratorioFarmaceutico(LaboratorioFarmaceuticoServicer):
    
    def Listo(self, request, context):
        return request
    
    def AltaTipoMedicamento(self, request, context):
        print(f"Alta de Tipo de Medicamento: {request.tipo}")
        return Confirmacion(True)

    def BajaTipoMedicamento(self, request, context):
        print(f"Baja de Tipo de Medicamento: {request.tipo}")
        return Confirmacion(True)
    
    def AltaMedicamento(self, request, context):
        print(f"Alta de de Medicamento: {request.nombre}")
        return Confirmacion(True)
    
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