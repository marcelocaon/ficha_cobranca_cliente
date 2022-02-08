import fdb
from datetime import date
from reportlab.pdfgen import canvas
import webbrowser

def gerar_relat3(data_in, data_fi):
    try:
        # Create a Cursor object that operates in the context of Connection con:
        con = fdb.connect(
            # host='localhost', database='C:\\KOCH\\SD\\SDDB.FDB',
            host='192.168.25.10', database='C:\\KOCH\\SD\\SDDB.FDB',
            user='SYSDBA', password='masterkey'
        )

        cur = con.cursor()
        data_in = str(data_in).replace("/",".") #somente aceita data com ponto sendo o separador
        data_fi = str(data_fi).replace("/",".")
        consulta = [data_in, data_fi]

        # Execute the SELECT statement:
        cur.execute("select b.nome, sum(a.valor - coalesce(a.valorpag,0.00)) from movcli a, vendedores b, clientes c where a.codcli = c.codcli and c.vendedor = b.codven and coalesce(a.valorpag, 0.00) < a.valor and a.datavenc between (?) and (?) group by b.nome order by b.nome", consulta)

        # Retrieve all rows as a sequence and print that sequence:
        lista = cur.fetchall()
        texto = []
        total_atraso = 0.00
        texto.append(f"Período: {data_in} a {data_fi}")
        texto.append("")
        texto.append('VENDEDOR                              EM ATRASO')
        texto.append("-"*60)
        for i in lista:
            atraso = float(i[1]).__round__(2)
            total_atraso = total_atraso.__round__(2) + atraso.__round__(2)
            nome = str(i[0])
            if nome.__len__() <= 40:
                tamanho = nome.__len__()
                saldo = 40 - tamanho
                j=0
                while j < saldo:
                    nome = nome+" "
                    j += 1
            texto.append(nome+f'R${atraso}')
        texto.append("")
        texto.append(f'Total Geral em atraso: R${total_atraso}')
        gerar_pdf(texto)
        return True
    except:
        print("Erro no relatório 3")

def gerar_pdf(lista):
    try:
        nome_pdf = f'relatorio3_{date.today()}'
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 780 #posicao que começa a escrever, começa a contar sempre de baixo para cima, da esquerda para a direita
        for linha in lista:
            x -= 15
            pdf.setFontSize(8)
            pdf.drawString(45, x, linha)
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 10)
        pdf.drawString(145, 800, 'Relatório 3 - Total de contas em atraso por vendedor:')
        #pdf.setFont("Helvetica-Bold", 12)
        #pdf.drawString(245, 724, 'Nome e idade')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
        webbrowser.open_new(f'ficha_cobranca_{date.today()}.pdf') # para abrir no aplicativo padrao de PDF´s
        #os.startfile(f'ficha_cobranca_{codcli}.pdf')
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))