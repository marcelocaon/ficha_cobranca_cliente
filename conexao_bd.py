import fdb
from datetime import date
from datetime import datetime
import pandas as pd
import gera_pdf as pdf


def data_formatada():
    data_atual = date.today()
    #data_em_texto = data_atual.strftime('%d/%m/%Y')
    data_em_texto = data_atual.strftime('%d.%m.%Y')
    return data_em_texto

def data_com_barras(data_ingles):
    return data_ingles.strftime('%d/%m/%Y')

def relatorio1(codcli):
#    try:
    con = fdb.connect(
        # host='localhost', database='C:\\KOCH\\SD\\SDDB.FDB',
        host='192.168.25.10', database='C:\\KOCH\\SD\\SDDB.FDB',
        user='SYSDBA', password='masterkey'
    )

    cur = con.cursor()
    consulta = []
    data_de_hj = data_formatada()
    consulta.append(int(codcli))
    consulta.append(data_de_hj)
    print(consulta)

    # Execute the SELECT statement:
    cur.execute('select a.codcli, a.data, a.valor, a.datavenc, a.tipo, a.parcela, a.pedido, a.valorpag, a.datapag, b.razao_social from movcli a, clientes b where a.codcli = (?) and a.valor > coalesce(a.valorpag, 0,00) and a.datavenc <= (?) and a.codcli = b.codcli order by a.datavenc, a.pedido',consulta,)

    # Retrieve all rows as a sequence and print that sequence:
    lista = cur.fetchall()
    cabecalho = False

    # for count,item in enumerate(lista):
    vendedor_atual = ''
    divida_total = 0.00
    for i in lista:
        # 0 codcli
        # 1 emissao
        # 2 valor
        # 3 data venc
        # 4 tipo
        # 5 parcela
        # 6 pedido numero
        # 7 valor pago (para calcular o saldo)
        # 8 data de pagamento
        # 9 razao social
        saldo = 0.00
        emissao = data_com_barras(i[1])
        vencimento = data_com_barras(i[3])
        # se nao fez nenhum pagamento a data de pagamento vai estar NULA
        if i[8] != None:
            data_pg = data_com_barras(i[8])
        else:
            data_pg = "          "
        if i[7] == None:
            valor_pg = ""
            saldo = ""
            divida_total = divida_total + float(i[2])
        else:
            valor_pg = i[7]
            saldo = i[2] - i[7]
            divida_total = divida_total + float(saldo)

        if cabecalho == False:
            cabecalho = True
            texto = []
            texto.append(f"Contas a Receber - Gerado em: {datetime.today()}")
            texto.append('*' * 3 + 'Código: '+ str(i[0]) + ' - ' + 'Razão Social: ' + str(i[9]) +'*' * 3)
            texto.append('Emissão        Valor      Vencimento Tipo Parc. Pedido Valor_PG Data_PG  Saldo')
            texto.append('-'*110)
            if saldo != "":
                texto.append(
                    f'{str(emissao)}  R${str(i[2])}   {str(vencimento)}   {str(i[4])}   {str(i[5])}    {str(i[6])}  R${str(valor_pg)}   {str(data_pg)}   R${str(saldo)}')
            else:
                texto.append(f'{str(emissao)}  R${str(i[2])}   {str(vencimento)}   {str(i[4])}   {str(i[5])}    {str(i[6])} {str(valor_pg)}   {str(data_pg)}   {str(saldo)}')
        else:
            if saldo != "":
                texto.append(
                    f'{str(emissao)}  R${str(i[2])}   {str(vencimento)}   {str(i[4])}   {str(i[5])}    {str(i[6])}  R${str(valor_pg)}   {str(data_pg)}   R${str(saldo)}')
            else:
                texto.append(f'{str(emissao)}  R${str(i[2])}   {str(vencimento)}   {str(i[4])}   {str(i[5])}    {str(i[6])} {str(valor_pg)}   {str(data_pg)}   {str(saldo)}')

    texto.append("")
    texto.append(f"Total em atraso: R${divida_total.__round__(2)}")
    texto.append("")
    texto.append("Recebido em: ___/___/___ o valor de R$ __________ por: ________________________________")
    texto.append("Recebido em: ___/___/___ o valor de R$ __________ por: ________________________________")
    texto.append("Recebido em: ___/___/___ o valor de R$ __________ por: ________________________________")
    texto.append("Recebido em: ___/___/___ o valor de R$ __________ por: ________________________________")
    texto.append("Recebido em: ___/___/___ o valor de R$ __________ por: ________________________________")
    #salvar_arquivo(texto, codcli)
    pdf.gerar(texto, codcli)

    cur.close()
    con.close()
    print("Conexão finalizada...")
    # except:
    #     print("Erro na conexão com o BD")

def salvar_arquivo(texto,codcli):
    f = open(f'ficha_cobranca_{codcli}.txt', 'w')
    #f.write(texto+'\n')
    for linha in texto:
        f.writelines(linha+'\n')
        print(linha)
    f.close()
    print('arquivo salvo...')

def procura_cliente(codigo):
    try:
        cliente = []
        con = fdb.connect(
            # host='localhost', database='C:\\KOCH\\SD\\SDDB.FDB',
            host='192.168.25.10', database='C:\\KOCH\\SD\\SDDB.FDB',
            user='SYSDBA', password='masterkey'
        )

        cur = con.cursor()

        # Execute the SELECT statement:
        cur.execute('select razao_social from clientes where codcli = (?)',codigo,)

        # Retrieve all rows as a sequence and print that sequence:
        cliente = cur.fetchall()
        return cliente
    except:
        print("Código do cliente não encontrado")


#conectar(3852)
