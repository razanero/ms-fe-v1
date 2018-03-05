# This program prints Hello, world!
import logging
import sys

sys.path.append('/home/odoo/.local/lib/python3.5/site-packages')

import dexml

_logger = logging.getLogger(__name__)

from suds.client import Client

logging.getLogger('suds.client').setLevel(logging.DEBUG)

from dexml import fields


class Item(dexml.Model):
    indicador = fields.String(tagname="indicador")
    numeroOrdenItem = fields.String(tagname="numeroOrdenItem")
    codigoProducto = fields.String(tagname="codigoProducto")
    descripcion = fields.String(tagname="descripcion")
    cantidad = fields.Float(tagname="cantidad")
    unidadMedida = fields.String(tagname="unidadMedida")
    importeUnitarioSinImpuesto = fields.Float(tagname="importeUnitarioSinImpuesto")
    importeUnitarioConImpuesto = fields.Float(tagname="importeUnitarioConImpuesto")
    codigoImporteUnitarioConImpuesto = fields.String(tagname="codigoImporteUnitarioConImpuesto")
    importeTotalSinImpuesto = fields.Float(tagname="importeTotalSinImpuesto")
    importeDescuento = fields.Float(tagname="importeDescuento")
    importeCargo = fields.Float(tagname="importeCargo")
    codigoRazonExoneracion = fields.String(tagname="codigoRazonExoneracion")
    importeIgv = fields.Float(tagname="importeIgv")


class Documento(dexml.Model):
    class meta:
        tagname="person"

    tipoDocumentoEmisor = fields.String(tagname='tipoDocumentoEmisor')
    numeroDocumentoEmisor = fields.String(tagname='numeroDocumentoEmisor')
    razonSocialEmisor = fields.String(tagname='razonSocialEmisor')
    nombreComercialEmisor = fields.String(tagname='nombreComercialEmisor')
    tipoDocumento = fields.String(tagname='tipoDocumento')
    serieNumero = fields.String(tagname='serieNumero')
    fechaEmision = fields.String(tagname='fechaEmision')
    ubigeoEmisor = fields.String(tagname='ubigeoEmisor')
    direccionEmisor = fields.String(tagname='direccionEmisor')
    urbanizacion = fields.String(tagname='urbanizacion')
    provinciaEmisor = fields.String(tagname='provinciaEmisor')
    departamentoEmisor = fields.String(tagname='departamentoEmisor')
    distritoEmisor = fields.String(tagname='distritoEmisor')
    paisEmisor = fields.String(tagname='paisEmisor')
    correoEmisor = fields.String(tagname='correoEmisor')
    tipoDocumentoAdquiriente = fields.String(tagname='tipoDocumentoAdquiriente')
    numeroDocumentoAdquiriente = fields.String(tagname='numeroDocumentoAdquiriente')
    razonSocialAdquiriente = fields.String(tagname='razonSocialAdquiriente')
    correoAdquiriente = fields.String(tagname='correoAdquiriente')
    tipoMoneda = fields.String(tagname='tipoMoneda')
    totalValorVentaNetoOpGravadas = fields.Float(tagname='totalValorVentaNetoOpGravadas')
    totalValorVentaNetoOpNoGravada = fields.Float(tagname='totalValorVentaNetoOpNoGravada')
    totalValorVentaNetoOpExoneradas = fields.Float(tagname='totalValorVentaNetoOpExoneradas')
    subTotal = fields.Float(tagname='subTotal')
    totalIgv = fields.Float(tagname='totalIgv')
    totalDescuentos = fields.Float(tagname='totalDescuentos')
    totalVenta = fields.Float(tagname='totalVenta')
    inHabilitado = fields.String(tagname='inHabilitado')
    codigoLeyenda_1 = fields.String(tagname='codigoLeyenda_1')
    textoLeyenda_1 = fields.String(tagname='textoLeyenda_1')
    items = fields.List(Item)

class Parameter(dexml.Model):
    value = fields.String(attrname="value")
    name = fields.String(attrname="name")


class SignOnLineCmd(dexml.Model):
    declare_sunat = fields.String(attrname="declare-sunat")
    declare_direct_sunat = fields.String(attrname="declare-direct-sunat")
    publish = fields.String()
    output = fields.String()
    parametros = fields.List(Parameter)
    documentos = fields.List(Documento)


p = SignOnLineCmd(declare_sunat="0", declare_direct_sunat="0", publish=0, output="PDF")
p.parametros.append(Parameter(value="10455548816", name="idEmisor"))
p.parametros.append(Parameter(value="01", name="tipoDocumento"))
documento = Documento(totalDescuentos=float(4.52))
documento.tipoDocumentoEmisor = "01"
documento.numeroDocumentoEmisor = "10413168533"
documento.razonSocialEmisor = "test"
documento.nombreComercialEmisor = "dsds"
documento.tipoDocumento = "01"
documento.serieNumero = "F00"
documento.fechaEmision = "2018-02-01"
documento.ubigeoEmisor = ""
documento.direccionEmisor = "2544"
documento.urbanizacion = "5454"
documento.provinciaEmisor = "54"
documento.departamentoEmisor = "5454"
documento.distritoEmisor = "545"
documento.paisEmisor = "PE"
documento.correoEmisor = "DSDSD@DSDS.COM"
documento.tipoDocumentoAdquiriente = "01"
documento.numeroDocumentoAdquiriente = "104125444"
documento.razonSocialAdquiriente = "DSDSD"
documento.correoAdquiriente = "DSDS@SDSD.CIN"
documento.tipoMoneda = "PEN"
documento.totalValorVentaNetoOpGravadas = 100
documento.totalValorVentaNetoOpNoGravada = 200
documento.totalValorVentaNetoOpExoneradas = 200
documento.subTotal = 10
documento.totalIgv = 18
documento.totalDescuentos = 105
documento.totalVenta = 100
documento.inHabilitado = 1
documento.codigoLeyenda_1 = "101"
documento.textoLeyenda_1 = "41545"


item1=Item()
item1.indicador = "D"
item1.numeroOrdenItem = "1"
item1.codigoProducto = "10"
item1.descripcion = "100"
item1.cantidad = 10
item1.unidadMedida = "UM"
item1.importeUnitarioSinImpuesto = 100
item1.importeUnitarioConImpuesto = 100
item1.codigoImporteUnitarioConImpuesto = "100"
item1.importeTotalSinImpuesto = 100
item1.importeDescuento = 100
item1.importeCargo = 100
item1.codigoRazonExoneracion = "10"
item1.importeIgv = 100

documento.items.append(item1)

p.documentos.append(documento)
print p.render(fragment=True)

# from suds.client import Client
# #
# from suds.transport.http import HttpAuthenticated
# t = HttpAuthenticated(username='MAINSOLUTIONS', password='10455548816')
# client = Client(url='http://test3.alignetsac.com/sfewsperu/ws/invoker?wsdl',transport=t)
#
#
# response = client.service.invoke("""<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
#     <SignOnLineCmd declare-sunat='0' declare-direct-sunat='0' publish='1' output='PDF'>
#     <parametros/>
#     <parameter value='10455548816' name='idEmisor'/>
#     <parameter value='01' name='tipoDocumento'/>
#     <documento>
#         <tipoDocumentoEmisor>6</tipoDocumentoEmisor>
#         <numeroDocumentoEmisor>10455548816</numeroDocumentoEmisor>
#         <razonSocialEmisor>BIZLINKS SAC</razonSocialEmisor>
#         <nombreComercialEmisor>BIZLINKS</nombreComercialEmisor>
#         <tipoDocumento>01</tipoDocumento>
#         <serieNumero>FBIZ-00000006</serieNumero>
#         <fechaEmision>2018-01-07</fechaEmision>
#         <ubigeoEmisor>150122</ubigeoEmisor>
#         <direccionEmisor>AV. CASIMIRO ULLOA NRO. 333</direccionEmisor>
#         <urbanizacion>SAN ANTONIO</urbanizacion>
#         <provinciaEmisor>LIMA</provinciaEmisor>
#         <departamentoEmisor>LIMA</departamentoEmisor>
#         <distritoEmisor>MIRAFLORES</distritoEmisor>
#         <paisEmisor>PE</paisEmisor>
#         <correoEmisor>-</correoEmisor>
#         <tipoDocumentoAdquiriente>6</tipoDocumentoAdquiriente>
#         <numeroDocumentoAdquiriente>20100018625</numeroDocumentoAdquiriente>
#         <razonSocialAdquiriente>MEDIFARMA S.A.</razonSocialAdquiriente>
#         <correoAdquiriente>-</correoAdquiriente>
#         <tipoMoneda>PEN</tipoMoneda>
#         <totalValorVentaNetoOpGravadas>78055.79</totalValorVentaNetoOpGravadas>
#         <totalValorVentaNetoOpNoGravada>0.00</totalValorVentaNetoOpNoGravada>
#         <totalValorVentaNetoOpExoneradas>0.00</totalValorVentaNetoOpExoneradas>
#         <subTotal>0.00</subTotal>
#         <totalIgv>14050.03</totalIgv>
#         <totalDescuentos>0.00</totalDescuentos>
#         <totalVenta>92105.82</totalVenta>
#         <inHabilitado>1</inHabilitado>
#         <codigoLeyenda_1>1000</codigoLeyenda_1>
#         <textoLeyenda_1>NOVENTA Y DOS MIL CIENTO CINCO SOLES CON OCHENTA Y DOS CENTIMOS</textoLeyenda_1>
#         <item>
#             <indicador>D</indicador>
#             <numeroOrdenItem>1</numeroOrdenItem>
#             <codigoProducto>3742107600</codigoProducto>
#             <descripcion>RODAJE DE BOLAS</descripcion>
#             <cantidad>10.00</cantidad>
#             <unidadMedida>NIU</unidadMedida>
#             <importeUnitarioSinImpuesto>7803.30</importeUnitarioSinImpuesto>
#             <importeUnitarioConImpuesto>9207.89</importeUnitarioConImpuesto>
#             <codigoImporteUnitarioConImpuesto>01</codigoImporteUnitarioConImpuesto>
#             <importeTotalSinImpuesto>78033.00</importeTotalSinImpuesto>
#             <importeDescuento>0.00</importeDescuento>
#             <importeCargo>0.00</importeCargo>
#             <codigoRazonExoneracion>10</codigoRazonExoneracion>
#             <importeIgv>14045.93</importeIgv>
#         </item>
#     </documento>
# </SignOnLineCmd>""")
# print (response)
