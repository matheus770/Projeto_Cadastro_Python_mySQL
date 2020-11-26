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




app = QtWidgets.QApplication([])
tela_cadastrar = uic.loadUi("telacadastro.ui")
tela_de_listagem = uic.loadUi("telalistar.ui")



tela_cadastrar.pushButton.clicked.connect(cadastro)
tela_cadastrar.pushButton_2.clicked.connect(listagem)


tela_de_listagem.pushButton.clicked.connect(voltar_inicio)
tela_de_listagem.pushButton_2.clicked.connect(deletar)

tela_cadastrar.show()
app.exec()