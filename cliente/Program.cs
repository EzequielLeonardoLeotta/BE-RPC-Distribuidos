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

            try
            {
                // var response = cliente.AltaTipoMedicamento(tipoMedicamento);
                // var response = cliente.BajaTipoMedicamento(tipoMedicamento);
                var response = cliente.AltaMedicamento(medicamento);
                // var response = cliente.TraerAerosoles(nulo);
                // var response = cliente.TraerMedicamenosConA(nulo);
                Console.WriteLine("Respuesta: " + response.Message);
            }
            catch (RpcException e)
            {
                throw e;
            }
        }
    }
}
