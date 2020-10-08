from PyQt5 import uic
import PyQt5.QtWidgets as QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastroprodutos"
)
def func_cadastro():
   
    cod = tela_cadastro.lineEdit.text()
    prod = tela_cadastro.lineEdit_2.text()
    cto = tela_cadastro.lineEdit_3.text()
    mrc = tela_cadastro.lineEdit_4.text()
    quant = tela_cadastro.lineEdit_5.text()
    pcvd = tela_cadastro.lineEdit_6.text()

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO cadprod (codigo, produto, custo, marca, quantidade, preçovenda) VALUES(%s, %s, %s, %s, %s, %s)"
    dados = (str(cod),str(prod),float(cto),str(mrc),int(quant),float(pcvd))
    cursor.execute(comando_SQL,dados)
    banco.commit()
    
    tela_cadastro.lineEdit.setText("")
    tela_cadastro.lineEdit_2.setText("")
    tela_cadastro.lineEdit_3.setText("")
    tela_cadastro.lineEdit_4.setText("")
    tela_cadastro.lineEdit_5.setText("")
    tela_cadastro.lineEdit_6.setText("")

def func_listar():
    tela_cadastro.close()
    tela_listar.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM cadprod"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    tela_listar.tableWidget.setRowCount(len(dados_lidos))
    tela_listar.tableWidget.setRowCount(6)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            tela_listar.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def abrir_del():
    tela_del.show()

def abrir_alt():
    tela_alt.show()

def alt_alt():
    cod = tela_alt.lineEdit.text()
    prc = tela_alt.lineEdit_2.float()
    
    cursor = banco.cursor()
    comando_SQL = "UPDATE cadprod SET preçovenda="+prc+" WHERE codigo="+cod
    cursor.execute(comando_SQL)
    banco.commit()


def fechar_alt():
    tela_alt.close()

def del_del():
    codex = tela_del.lineEdit.text()

    cursor = banco.cursor()
    comando_SQL = "DELETE FROM cadprod WHERE codigo="+codex
    cursor.execute(comando_SQL)
    banco.commit()

def volta_ini():
    tela_listar.close()
    tela_cadastro.show()



app = QtWidgets.QApplication([])
tela_cadastro = uic.loadUi("telacadastro.ui")
tela_listar = uic.loadUi("telalistar.ui")
tela_del = uic.loadUi("teladeletar.ui")
tela_alt = uic.loadUi("telaalterar.ui")


tela_cadastro.pushButton.clicked.connect(func_cadastro)
tela_cadastro.pushButton_2.clicked.connect(func_listar)
tela_listar.pushButton.clicked.connect(abrir_del)
tela_del.pushButton.clicked.connect(del_del)
tela_listar.pushButton_3.clicked.connect(abrir_alt)
tela_listar.pushButton_2.clicked.connect(volta_ini)
tela_alt.pushButton.clicked.connect(fechar_alt)
tela_alt.pushButton_2.clicked.connect(alt_alt)

tela_cadastro.show()
app.exec()