
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import seaborn as sb
import os

class Ui_MainWindow(object):
    def pred(self):
        print("Button Clicked")
        print(self.Bmar.value())
        if int(self.Brnd.value())<50 or int(self.Badm.value())<50 or int(self.Bmar.value())<50:
            self.lineEdit.setText('0')
        elif str(self.Cchoice.currentText()) == "Multiple Regression":
            self.lineEdit.setText(str(self.mulreg()).replace("[","").replace("]",""))
        elif str(self.Cchoice.currentText()) == "Support Vector Regression":
            self.lineEdit.setText(str(self.svr()).replace("[","").replace("]",""))
        elif str(self.Cchoice.currentText()) == "Random Forest":
            self.lineEdit.setText(str(self.RF()).replace("[","").replace("]",""))
        elif str(self.Cchoice.currentText()) == "Wisdom of Models":
            self.lineEdit.setText(str(self.WOM()).replace("[","").replace("]",""))
            
        
    def WOM(self):
        return (self.mulreg()+self.RF()+self.svr())/3
        
    def mulreg(self):
        #importing dataset
        dataset=pd.read_csv('50_Startups.csv')      
        x=dataset.iloc[:,:-1].values
        y=dataset.iloc[:,-1].values
        
        #Encoding catagorical data
        from sklearn.preprocessing import LabelEncoder,OneHotEncoder
        labelencoder_X=LabelEncoder()
        x[:,3]=labelencoder_X.fit_transform(x[:,3])
        onehotencoder=OneHotEncoder(categorical_features=[3])
        x=onehotencoder.fit_transform(x).toarray()
        
        #Avoiding dummy variable trap
        x=x[:,1:]
        
        self.company_name="TCS" if self.Rtcs.isChecked() else "Wipro" if self.Rvpro.isChecked() else "DXC"
        data=[str(self.Brnd.value()),str(self.Badm.value()),str(self.Bmar.value()),self.company_name]
        datast={'R&D Spend':data[0] if data[0]!='' else 100000,'Administration':data[1] if data[1]!='' else 40000,'Marketing Spend':data[2] if data[2]!='' else 25000,'Company name':data[3]if data[3]!=''else 'TCS'}
        datast=pd.DataFrame(datast,index=[0])
        
        datast.to_csv('file.csv')
        data=pd.read_csv('file.csv',usecols=['R&D Spend','Administration','Marketing Spend','Company name'])
        x_test=data.iloc[:,:].values
        
        #from sklearn.preprocessing import LabelEncoder,OneHotEncoder
        #labelencoder_X=LabelEncoder()
        x_test[:,3]=labelencoder_X.transform(x_test[:,3])
        #onehotencoder=OneHotEncoder(categorical_features=[3])
        x_test=onehotencoder.transform(x_test).toarray()
    
        #Avoiding dummy variable trap
        x_test=x_test[:,1:]
        
        from sklearn.linear_model import LinearRegression
        regressor=LinearRegression()
        regressor.fit(x,y)
        
        return regressor.predict(x_test)

    def RF(self):
        #importing dataset
        dataset=pd.read_csv('50_Startups.csv')      
        x=dataset.iloc[:,:-1].values
        y=dataset.iloc[:,-1].values
        
        #Encoding catagorical data
        from sklearn.preprocessing import LabelEncoder,OneHotEncoder
        labelencoder_X=LabelEncoder()
        x[:,3]=labelencoder_X.fit_transform(x[:,3])
        onehotencoder=OneHotEncoder(categorical_features=[3])
        x=onehotencoder.fit_transform(x).toarray()
        
        #Avoiding dummy variable trap
        x=x[:,1:]
        
        self.company_name="TCS" if self.Rtcs.isChecked() else "Wipro" if self.Rvpro.isChecked() else "DXC"
        data=[str(self.Brnd.value()),str(self.Badm.value()),str(self.Bmar.value()),self.company_name]
        datast={'R&D Spend':data[0] if data[0]!='' else 100000,'Administration':data[1] if data[1]!='' else 40000,'Marketing Spend':data[2] if data[2]!='' else 25000,'Company name':data[3]if data[3]!=''else 'TCS'}
        datast=pd.DataFrame(datast,index=[0])
        
        datast.to_csv('file.csv')
        data=pd.read_csv('file.csv',usecols=['R&D Spend','Administration','Marketing Spend','Company name'])
        x_test=data.iloc[:,:].values
        
        #from sklearn.preprocessing import LabelEncoder,OneHotEncoder
        #labelencoder_X=LabelEncoder()
        x_test[:,3]=labelencoder_X.transform(x_test[:,3])
        #onehotencoder=OneHotEncoder(categorical_features=[3])
        x_test=onehotencoder.transform(x_test).toarray()
    
        #Avoiding dummy variable trap
        x_test=x_test[:,1:]
        
        from sklearn.ensemble import RandomForestRegressor
        regressor=RandomForestRegressor(n_estimators=500)
        regressor.fit(x,y)
        #print("RF",regressor.predict(x_test))
        return regressor.predict(x_test)
        
    def svr(self):
        #importing dataset
        dataset=pd.read_csv('50_Startups.csv')      
        x=dataset.iloc[:,:-1].values
        y=dataset.iloc[:,-1].values
        
        #Encoding catagorical data
        from sklearn.preprocessing import LabelEncoder,OneHotEncoder
        labelencoder_X=LabelEncoder()
        x[:,3]=labelencoder_X.fit_transform(x[:,3])
        onehotencoder=OneHotEncoder(categorical_features=[3])
        x=onehotencoder.fit_transform(x).toarray()
        
        #Avoiding dummy variable trap
        x=x[:,1:]
        
        self.company_name="TCS" if self.Rtcs.isChecked() else "Wipro" if self.Rvpro.isChecked() else "DXC"
        data=[str(self.Brnd.value()),str(self.Badm.value()),str(self.Bmar.value()),self.company_name]
        datast={'R&D Spend':data[0] if data[0]!='' else 100000,'Administration':data[1] if data[1]!='' else 40000,'Marketing Spend':data[2] if data[2]!='' else 25000,'Company name':data[3]if data[3]!=''else 'TCS'}
        datast=pd.DataFrame(datast,index=[0])
        
        datast.to_csv('file.csv')
        data=pd.read_csv('file.csv',usecols=['R&D Spend','Administration','Marketing Spend','Company name'])
        x_test=data.iloc[:,:].values
        
        #from sklearn.preprocessing import LabelEncoder,OneHotEncoder
        #labelencoder_X=LabelEncoder()
        x_test[:,3]=labelencoder_X.transform(x_test[:,3])
        #onehotencoder=OneHotEncoder(categorical_features=[3])
        x_test=onehotencoder.transform(x_test).toarray()
    
        #Avoiding dummy variable trap
        x_test=x_test[:,1:]
        
        
        from sklearn.preprocessing import StandardScaler
        sc_X=StandardScaler()
        sc_y=StandardScaler()
        x=sc_X.fit_transform(x)
        y=sc_y.fit_transform(y.reshape(len(y),1))
        y=y[:,0]
    
        #Fitting SVR to the dataset
        from sklearn.svm import SVR
        regressor=SVR(kernel='linear')
        regressor.fit(x,y)
        #print("SVR",sc_y.inverse_transform(regressor.predict(sc_X.transform(x_test))))
        return sc_y.inverse_transform(regressor.predict(sc_X.transform(x_test)))

    
    def cle(self):
        print("Clean clicked")
        self.Brnd.setValue(float(0))
        self.Badm.setValue(float(0))
        self.Bmar.setValue(float(0))
        
        self.Rtcs.setChecked(1)
        
        self.Cchoice.setCurrentIndex(0)
        
        self.lineEdit.setText('')
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(1061, 823)
        MainWindow.setFixedSize(1061,823)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 231))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.Lrnd = QtWidgets.QLabel(self.groupBox)
        self.Lrnd.setGeometry(QtCore.QRect(10, 25, 81, 21))
        self.Lrnd.setObjectName("Lrnd")
        
        self.Ladm = QtWidgets.QLabel(self.groupBox)
        self.Ladm.setGeometry(QtCore.QRect(10, 80, 121, 31))
        self.Ladm.setObjectName("Ladm")
        
        self.Lmar = QtWidgets.QLabel(self.groupBox)
        self.Lmar.setGeometry(QtCore.QRect(10, 150, 101, 21))
        self.Lmar.setObjectName("Lmar")
        
        self.Brnd = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Brnd.setGeometry(QtCore.QRect(160, 20, 141, 31))
        self.Brnd.setObjectName("Brnd")
        self.Brnd.setMaximum(10000000)
        
        self.Badm = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Badm.setGeometry(QtCore.QRect(160, 80, 141, 31))
        self.Badm.setObjectName("Badm")
        self.Badm.setMaximum(10000000)
        
        self.Bmar = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Bmar.setGeometry(QtCore.QRect(160, 150, 141, 31))
        self.Bmar.setObjectName("Bmar")
        self.Bmar.setMaximum(10000000)
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(430, 11, 350, 131))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.Rtcs = QtWidgets.QRadioButton(self.groupBox_2)
        self.Rtcs.setGeometry(QtCore.QRect(60, 20, 201, 31))
        self.Rtcs.setObjectName("Rtcs")
        self.Rtcs.setChecked(1)
        
        self.Rvpro = QtWidgets.QRadioButton(self.groupBox_2)
        self.Rvpro.setGeometry(QtCore.QRect(60, 50, 191, 31))
        self.Rvpro.setObjectName("Rvpro")
        
        self.Rdx = QtWidgets.QRadioButton(self.groupBox_2)
        self.Rdx.setGeometry(QtCore.QRect(60, 80, 191, 31))
        self.Rdx.setObjectName("Rdx")
        
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(430, 161, 350, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.Lalgorithm = QtWidgets.QLabel(self.groupBox_3)
        self.Lalgorithm.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.Lalgorithm.setObjectName("Lalgorithm")
        
        self.Cchoice = QtWidgets.QComboBox(self.groupBox_3)
        self.Cchoice.setGeometry(QtCore.QRect(90, 30, 210, 31))
        self.Cchoice.setObjectName("Cchoice")
        self.Cchoice.addItem("")
        self.Cchoice.addItem("")
        self.Cchoice.addItem("")
        self.Cchoice.addItem("")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(810, 30, 241, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.predict = QtWidgets.QPushButton(self.frame)
        self.predict.setGeometry(QtCore.QRect(10, 10, 100, 40))
        self.predict.setObjectName("predict")
        self.predict.clicked.connect(self.pred)
        
        self.clear = QtWidgets.QPushButton(self.frame)
        self.clear.setGeometry(QtCore.QRect(130, 10, 100, 40))
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.cle)
        
        self.ext = QtWidgets.QPushButton(self.frame)
        self.ext.setGeometry(QtCore.QRect(70, 70, 100, 40))
        self.ext.setObjectName("ext")
        self.ext.clicked.connect(sys.exit)
        
        self.backimg = QtWidgets.QLabel(self.centralwidget)
        self.backimg.setGeometry(QtCore.QRect(0, 0, 1061, 844))
        self.backimg.setText("")
        self.backimg.setPixmap(QtGui.QPixmap("blue-wave-vector-abstract-background-vector-abstract-greyscale-graphic-design-138278819.jpg"))
        self.backimg.setScaledContents(True)
        self.backimg.setObjectName("backimg")
        
        self.Lres = QtWidgets.QLabel(self.centralwidget)
        self.Lres.setGeometry(QtCore.QRect(360, 410, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Lres.setFont(font)
        self.Lres.setObjectName("Lres")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(550, 421, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength(10)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        
        self.backimg.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.frame.raise_()
        self.Lres.raise_()
        self.lineEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "costs"))
        self.Lrnd.setText(_translate("MainWindow", "R&D"))
        
        self.Ladm.setText(_translate("MainWindow", "Administration"))
        
        self.Lmar.setText(_translate("MainWindow", "Marketing"))
        
        self.groupBox_2.setTitle(_translate("MainWindow", "Company"))
        self.Rtcs.setText(_translate("MainWindow", "Tata Cunsultancy Service"))
        
        self.Rvpro.setText(_translate("MainWindow", "Wipro"))
        
        self.Rdx.setText(_translate("MainWindow", "DXC"))
        
        self.groupBox_3.setTitle(_translate("MainWindow", "Algorithm"))
        self.Lalgorithm.setText(_translate("MainWindow", "Algorithm"))
        
        self.Cchoice.setItemText(0, _translate("MainWindow", "Multiple Regression"))
        
        self.Cchoice.setItemText(1, _translate("MainWindow", "Support Vector Regression"))
        
        self.Cchoice.setItemText(2, _translate("MainWindow", "Random Forest"))
        
        self.Cchoice.setItemText(3, _translate("MainWindow", "Wisdom of Models"))
        
        self.predict.setText(_translate("MainWindow", "PREDICT"))
        
        self.clear.setText(_translate("MainWindow", "Clear All"))
        
        self.ext.setText(_translate("MainWindow", "exit"))
        
        self.Lres.setText(_translate("MainWindow", "Predicted Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

