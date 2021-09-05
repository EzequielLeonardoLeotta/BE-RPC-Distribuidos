using System;
using Grpc.Core;
using Grpc.Net.Client;

namespace cliente
{
    class Program
    {
        static void Main(string[] args)
        {
            AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);
            var channel = GrpcChannel.ForAddress("http://localhost:50051");

            var cliente = new LaboratorioFarmaceutico.LaboratorioFarmaceuticoClient(channel);

            cliente.Listo(new Nulo());

            var tipoMedicamento = new TipoMedicamento
            {
                Tipo = "aerosoles"
            };

            var medicamento = new Medicamento
            {
                CodigoAlfabetico = "AAA",
                CodigoNumerico = 12345,
                DigitoVerificador = 0,
                Nombre = "Anginovag",
                Droga = "Hidrocortisona",
                TipoMedicamento = 1
            };

            var nulo = new Nulo();

            string procedimiento = "TraerMedicamenosConA";

            try
            {
                switch (procedimiento)
                {
                    case "AltaTipoMedicamento":
                        Console.WriteLine("Respuesta: " + cliente.AltaTipoMedicamento(tipoMedicamento).Message);
                        break;
                    case "BajaTipoMedicamento":
                        Console.WriteLine("Respuesta: " + cliente.BajaTipoMedicamento(tipoMedicamento).Message);
                        break;
                    case "AltaMedicamento":
                        Console.WriteLine("Respuesta: " + cliente.AltaMedicamento(medicamento).Message);
                        break;
                    case "TraerAerosoles":
                        Console.WriteLine("Respuesta: " + cliente.TraerAerosoles(nulo).Message);
                        break;
                    case "TraerMedicamenosConA":
                        Console.WriteLine("Respuesta: " + cliente.TraerMedicamenosConA(nulo).Message);
                        break;
                    default: 
                        Console.WriteLine("Error: no se puede llamar a un procedimiento inexistente");
                        break;
                }
            }
            catch (RpcException e)
            {
                Console.WriteLine(e.Message + " " + e.StackTrace);
            }
        }
    }
}
