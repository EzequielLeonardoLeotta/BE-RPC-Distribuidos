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

            var confirmacion = cliente.AltaTipoMedicamento(tipoMedicamento);

            Console.WriteLine($"Resultado: {confirmacion.Confirmacion_}");
        }
    }
}
