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
                DigitoVerificador = 1,
                Nombre = "Anginovag",
                Droga = "Hidrocortisona",
                TipoMedicamento = 1
            };

            try
            {
                // var confirmacion = cliente.AltaTipoMedicamento(tipoMedicamento);
                // var confirmacion = cliente.BajaTipoMedicamento(tipoMedicamento);
                // var confirmacion = cliente.AltaMedicamento(medicamento);
            }
            catch (RpcException e)
            {
                throw e;
            }
        }
    }
}
