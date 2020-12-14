from PyQt5 import uic
import PyQt5.QtWidgets as QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastroprodutos"
)
def cadastro():
   
    cod = tela_cadastrar.lineEdit.text()
    prod = tela_cadastrar.lineEdit_2.text()
    cto = tela_cadastrar.lineEdit_3.text()
    mrc = tela_cadastrar.lineEdit_4.text()
    quant = tela_cadastrar.lineEdit_5.text()
    pcvd = tela_cadastrar.lineEdit_6.text()

    cursor = banco.cursor()
    try:
        comando_SQL = "INSERT INTO cadprod (codigo, produto, custo, marca, quantidade, preçovenda) VALUES(%s, %s, %s, %s, %s, %s)"
        dados = (str(cod),str(prod),float(cto),str(mrc),int(quant),float(pcvd))
        cursor.execute(comando_SQL,dados)
        banco.commit()

        tela_cadastrar.lineEdit.setText("")
        tela_cadastrar.lineEdit_2.setText("")
        tela_cadastrar.lineEdit_3.setText("")
        tela_cadastrar.lineEdit_4.setText("")
        tela_cadastrar.lineEdit_5.setText("")
        tela_cadastrar.lineEdit_6.setText("")
        tela_cadastrar.label_8.setText("")
    except:
        tela_cadastrar.label_8.setText("Erro, codigo existente ou Campos em branco")    
            

def listagem():
    tela_cadastrar.close()
    tela_de_listagem.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM cadprod"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    tela_de_listagem.tableWidget.setRowCount(len(dados_lidos))
    tela_de_listagem.tableWidget.setRowCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            tela_de_listagem.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def voltar_inicio():
    #Volta a tela inicio
    tela_de_listagem.close()
    tela_cadastrar.show()

def deletar():
    produto_selecionado = tela_de_listagem.tableWidget.currentRow()
    tela_de_listagem.tableWidget.removeRow(produto_selecionado)

    cursor = banco.cursor()
    cursor.execute("SELECT codigo FROM cadprod")
    idsel = cursor.fetchall()
    iddel = idsel[produto_selecionado][0]
    cursor.execute("DELETE FROM cadprod WHERE codigo="+iddel)

def abrir_att():
     tela_att.show()

def fechar_att():
    tela_att.close()
    tela_cadastrar.show()

def atualizar_produto():
    
    cod = tela_att.lineEdit.text()
    prod = tela_att.lineEdit_2.text()
    cto = tela_att.lineEdit_3.text()
    mrc = tela_att.lineEdit_4.text()
    quant = tela_att.lineEdit_5.text()
    pcvd = tela_att.lineEdit_6.text()

    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM cadprod WHERE codigo='{cod}'")
    p = cursor.fetchall()
    pnome = p[0][1]
    pcusto = p[0][2]
    pmarca = p[0][3]
    pquant = p[0][4]
    pvenda = p[0][5]
    print(f"{pnome} {pcusto} {pmarca} {pquant} {pvenda}")
    if(prod == ""):
        prod = pnome
    if(cto == ""):
        cto = pcusto
    if(mrc == ""):
        mrc = pmarca
    if(quant == ""):
        quant = pquant
    if(pcvd == ""):
        pcvd = pvenda
    
    cursor.execute(f"UPDATE cadprod SET produto='{prod}', custo='{cto}', marca='{mrc}', quantidade='{quant}', preçovenda='{pcvd}' WHERE codigo='{cod}'")

    tela_att.lineEdit.setText("")
    tela_att.lineEdit_2.setText("")
    tela_att.lineEdit_3.setText("")
    tela_att.lineEdit_4.setText("")
    tela_att.lineEdit_5.setText("")
    tela_att.lineEdit_6.setText("")




app = QtWidgets.QApplication([])
tela_cadastrar = uic.loadUi("telacadastro.ui")
tela_de_listagem = uic.loadUi("telalistar.ui")
tela_att = uic.loadUi("telaatualizar.ui")

tela_cadastrar.pushButton.clicked.connect(cadastro)
tela_cadastrar.pushButton_2.clicked.connect(listagem)
tela_cadastrar.pushButton_3.clicked.connect(abrir_att)

tela_de_listagem.pushButton.clicked.connect(voltar_inicio)
tela_de_listagem.pushButton_2.clicked.connect(deletar)

tela_att.pushButton_2.clicked.connect(fechar_att)
tela_att.pushButton.clicked.connect(atualizar_produto)

tela_cadastrar.show()
app.exec()