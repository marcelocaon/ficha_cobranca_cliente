#import PyPDF2
from reportlab.pdfgen import canvas
import webbrowser

#gera o pdf do relatorio1
def gerar(texto, codcli):
    # f = open(f'ficha_cobranca_{codcli}.txt', 'w')
    # #f.write(texto+'\n')
    # for linha in texto:
    #     f.writelines(linha+'\n')
    #     print(linha)
    # f.close()
    # print('arquivo salvo...')

    try:
        nome_pdf = f'ficha_cobranca_{codcli}'
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 780 #posicao que começa a escrever, começa a contar sempre de baixo para cima, da esquerda para a direita
        for linha in texto:
            x -= 15
            pdf.setFontSize(8)
            pdf.drawString(20, x, linha)
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 10)
        pdf.drawString(245, 800, 'Ficha de Cobrança')
        #pdf.setFont("Helvetica-Bold", 12)
        #pdf.drawString(245, 724, 'Nome e idade')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
        webbrowser.open_new(f'ficha_cobranca_{codcli}.pdf') # para abrir no aplicativo padrao de PDF´s
        #os.startfile(f'ficha_cobranca_{codcli}.pdf')
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))


# Explorando código
# Linha 1: Estamos importando o método canvas da biblioteca reportlab (para saber mais sobre os métodos clique aqui);
# Linha 6: canvas.Canvas(arquivo.pdf) cria um objeto canvas que irá gerar um arquivo pdf com o nome e local inserido. No exemplo armazenamos o objeto na variável pdf;
# Linha 7 até 10: A função drawString(y,x,texto) utiliza na folha do pdf um plano cartesiano com eixos X e Y (a página possui 595.27 de largura e 841.89 de altura no padrão A4). Então basicamente demos uma posição y = 247 e x = 700 para centralizar na tela, depois para cada nome,idade na lista iremos escrever cada um começando na posição 700 e descrescendo o x toda vez que terminar de escrevar uma linha com o nome e a idade;
# Linha 11: pdf.setTitle(titulo) adicionará um título no pdf;
# Linha 12: pdf.setFont(Nome da font, tamanho) irá selecionar a fonte e o seu tamanho para os itens;
# Linha 16: pdf.Save() salvará as modificações feitas no caminho especificado do objeto canvas.Canvas();
# Linha 21: Criamos uma variável chamada lista do tipo dicionário inserindo alguns valores;
# Linha 23: Invocamos a função GeneratePDF(lista) passando a variável lista como argumento;

