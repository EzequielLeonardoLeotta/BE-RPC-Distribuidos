# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import servicio_pb2 as servicio__pb2


class LaboratorioFarmaceuticoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Listo = channel.unary_unary(
                '/LaboratorioFarmaceutico/Listo',
                request_serializer=servicio__pb2.Nulo.SerializeToString,
                response_deserializer=servicio__pb2.Nulo.FromString,
                )
        self.AltaTipoMedicamento = channel.unary_unary(
                '/LaboratorioFarmaceutico/AltaTipoMedicamento',
                request_serializer=servicio__pb2.TipoMedicamento.SerializeToString,
                response_deserializer=servicio__pb2.Response.FromString,
                )
        self.BajaTipoMedicamento = channel.unary_unary(
                '/LaboratorioFarmaceutico/BajaTipoMedicamento',
                request_serializer=servicio__pb2.TipoMedicamento.SerializeToString,
                response_deserializer=servicio__pb2.Response.FromString,
                )
        self.AltaMedicamento = channel.unary_unary(
                '/LaboratorioFarmaceutico/AltaMedicamento',
                request_serializer=servicio__pb2.Medicamento.SerializeToString,
                response_deserializer=servicio__pb2.Response.FromString,
                )
        self.TraerAerosoles = channel.unary_unary(
                '/LaboratorioFarmaceutico/TraerAerosoles',
                request_serializer=servicio__pb2.Nulo.SerializeToString,
                response_deserializer=servicio__pb2.Response.FromString,
                )
        self.TraerMedicamenosConA = channel.unary_unary(
                '/LaboratorioFarmaceutico/TraerMedicamenosConA',
                request_serializer=servicio__pb2.Nulo.SerializeToString,
                response_deserializer=servicio__pb2.Response.FromString,
                )
        self.TraerTiposMedicamentos = channel.unary_unary(
                '/LaboratorioFarmaceutico/TraerTiposMedicamentos',
                request_serializer=servicio__pb2.Nulo.SerializeToString,
                response_deserializer=servicio__pb2.Response.FromString,
                )


class LaboratorioFarmaceuticoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Listo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AltaTipoMedicamento(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BajaTipoMedicamento(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AltaMedicamento(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TraerAerosoles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TraerMedicamenosConA(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TraerTiposMedicamentos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LaboratorioFarmaceuticoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Listo': grpc.unary_unary_rpc_method_handler(
                    servicer.Listo,
                    request_deserializer=servicio__pb2.Nulo.FromString,
                    response_serializer=servicio__pb2.Nulo.SerializeToString,
            ),
            'AltaTipoMedicamento': grpc.unary_unary_rpc_method_handler(
                    servicer.AltaTipoMedicamento,
                    request_deserializer=servicio__pb2.TipoMedicamento.FromString,
                    response_serializer=servicio__pb2.Response.SerializeToString,
            ),
            'BajaTipoMedicamento': grpc.unary_unary_rpc_method_handler(
                    servicer.BajaTipoMedicamento,
                    request_deserializer=servicio__pb2.TipoMedicamento.FromString,
                    response_serializer=servicio__pb2.Response.SerializeToString,
            ),
            'AltaMedicamento': grpc.unary_unary_rpc_method_handler(
                    servicer.AltaMedicamento,
                    request_deserializer=servicio__pb2.Medicamento.FromString,
                    response_serializer=servicio__pb2.Response.SerializeToString,
            ),
            'TraerAerosoles': grpc.unary_unary_rpc_method_handler(
                    servicer.TraerAerosoles,
                    request_deserializer=servicio__pb2.Nulo.FromString,
                    response_serializer=servicio__pb2.Response.SerializeToString,
            ),
            'TraerMedicamenosConA': grpc.unary_unary_rpc_method_handler(
                    servicer.TraerMedicamenosConA,
                    request_deserializer=servicio__pb2.Nulo.FromString,
                    response_serializer=servicio__pb2.Response.SerializeToString,
            ),
            'TraerTiposMedicamentos': grpc.unary_unary_rpc_method_handler(
                    servicer.TraerTiposMedicamentos,
                    request_deserializer=servicio__pb2.Nulo.FromString,
                    response_serializer=servicio__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LaboratorioFarmaceutico', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LaboratorioFarmaceutico(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Listo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LaboratorioFarmaceutico/Listo',
            servicio__pb2.Nulo.SerializeToString,
            servicio__pb2.Nulo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AltaTipoMedicamento(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LaboratorioFarmaceutico/AltaTipoMedicamento',
            servicio__pb2.TipoMedicamento.SerializeToString,
            servicio__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BajaTipoMedicamento(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LaboratorioFarmaceutico/BajaTipoMedicamento',
            servicio__pb2.TipoMedicamento.SerializeToString,
            servicio__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AltaMedicamento(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LaboratorioFarmaceutico/AltaMedicamento',
            servicio__pb2.Medicamento.SerializeToString,
            servicio__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TraerAerosoles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LaboratorioFarmaceutico/TraerAerosoles',
            servicio__pb2.Nulo.SerializeToString,
            servicio__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TraerMedicamenosConA(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LaboratorioFarmaceutico/TraerMedicamenosConA',
            servicio__pb2.Nulo.SerializeToString,
            servicio__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TraerTiposMedicamentos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LaboratorioFarmaceutico/TraerTiposMedicamentos',
            servicio__pb2.Nulo.SerializeToString,
            servicio__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
