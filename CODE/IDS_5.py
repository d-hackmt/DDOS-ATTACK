import tkinter as tk
from tkinter import *
import pandas as pd
import numpy as np
from hmmlearn import hmm
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.ensemble import VotingClassifier
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
le = LabelEncoder()

root = tk.Tk()

w,h = root.winfo_screenwidth() ,root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.title("DDOS ATTACK")
root.configure(background="cyan2")

image2 = Image.open('IMG.jpg')
image2 = image2.resize((1500, 700), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) 

"""
tpot_data = pd.read_csv(r'D:/DDOS ATTACK/IDS_5_CLASSIFIERS/IDS_5_CLASSIFIERS/KDD_CUP_2.csv')#, sep='COLUMN_SEPARATOR', dtype=np.float64)
tpot_data['protocol_type']=le.fit_transform(tpot_data['protocol_type'])
tpot_data['service']=le.fit_transform(tpot_data['service'])
tpot_data['flag']=le.fit_transform(tpot_data['flag'])

x = tpot_data.drop(['label'],axis=1)
y = tpot_data['label']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
"""
new_data = pd.read_csv(r'KDDTrain.csv')#, sep='COLUMN_SEPARATOR', dtype=np.float64)
new_data['protocol_type']=le.fit_transform(new_data['protocol_type'])
new_data['service']=le.fit_transform(new_data['service'])
new_data['flag']=le.fit_transform(new_data['flag'])
x_train = new_data.drop(["label"],axis=1)
y_train = new_data["label"]


new_data = pd.read_csv(r'KDDTest.csv')#, sep='COLUMN_SEPARATOR', dtype=np.float64)
new_data['protocol_type']=le.fit_transform(new_data['protocol_type'])
new_data['service']=le.fit_transform(new_data['service'])
new_data['flag']=le.fit_transform(new_data['flag'])
x_test = new_data.drop(["label"],axis=1)
y_test = new_data["label"]



def XG_BOOST():
     
    
    
    
    
    
    model1 = XGBClassifier()
    model1.fit(x_train, y_train)
    
    model1_pred = model1.predict(x_test)
    print(model1_pred)
    
    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, model1_pred)))
    print("Accuracy : ",accuracy_score(y_test,model1_pred)*100)
    accuracy = accuracy_score(y_test, model1_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, model1_pred) * 100)
    repo = (classification_report(y_test, model1_pred))
    
    label4 = tk.Label(root,text =str(repo),width=35,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=100)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as XG_BOOST.joblib",width=35,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=320)
    from joblib import dump
    dump (model1,"XG_BOOST.joblib")
    print("Model saved as XG_BOOST.joblib")
    
    
def SVM():
    
    
    
    model2 = SVC(kernel='linear')
    model2.fit(x_train, y_train)
    
    
    
    print("=" * 40)
    model2.fit(x_train, y_train)
    
    model2_pred = model2.predict(x_test)
    #print(model2_pred)
    
    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, model2_pred)))
    print("Accuracy : ",accuracy_score(y_test,model2_pred)*100)
    accuracy = accuracy_score(y_test, model2_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, model2_pred) * 100)
    repo = (classification_report(y_test, model2_pred))
    
    label4 = tk.Label(root,text =str(repo),width=35,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=100)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as SVM.joblib",width=35,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=320)
    from joblib import dump
    dump (model2,"SVM.joblib")
    print("Model saved as SVM.joblib")
    
def NB():
    
    model3 = GaussianNB()
    model3.fit(x_train, y_train)
    
    
    
    print("=" * 40)
    model3.fit(x_train, y_train)
    
    model3_pred = model3.predict(x_test)
    #print(model2_pred)
      
    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, model3_pred)))
    print("Accuracy : ",accuracy_score(y_test,model3_pred)*100)
    accuracy = accuracy_score(y_test, model3_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, model3_pred) * 100)
    repo = (classification_report(y_test, model3_pred))
    
    label4 = tk.Label(root,text =str(repo),width=35,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=100)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as NB.joblib",width=35,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=320)
    from joblib import dump
    dump (model3,"NB.joblib")
    print("Model saved as NB.joblib")
    

def DT():
    
    model4 = DecisionTreeClassifier(criterion = "gini",random_state = 100,max_depth=3, min_samples_leaf=5)   
    
    model4.fit(x_train, y_train)
    
    
    
    print("=" * 40)
    model4.fit(x_train, y_train)
    
    model4_pred = model4.predict(x_test)
    #print(model2_pred)
    
    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, model4_pred)))
    print("Accuracy : ",accuracy_score(y_test,model4_pred)*100)
    accuracy = accuracy_score(y_test, model4_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, model4_pred) * 100)
    repo = (classification_report(y_test, model4_pred))
    
    label4 = tk.Label(root,text =str(repo),width=35,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=100)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as DT.joblib",width=35,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=320)
    from joblib import dump
    dump (model4,"DT.joblib")
    print("Model saved as DT.joblib")
    
    
def RF():
    
    #seed = 7
    num_trees = 100
    max_features = 3
    
    model5 = RandomForestClassifier(n_estimators=num_trees, max_features=max_features)

    
    
    model5.fit(x_train, y_train)
    
    model5_pred = model5.predict(x_test)
    print(model5_pred)
    
    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, model5_pred)))
    print("Accuracy : ",accuracy_score(y_test,model5_pred)*100)
    accuracy = accuracy_score(y_test, model5_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, model5_pred) * 100)
    repo = (classification_report(y_test, model5_pred))
    
    label4 = tk.Label(root,text =str(repo),width=35,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=100)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as RF.joblib",width=35,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=320)
    from joblib import dump
    dump (model5,"RF.joblib")
    print("Model saved as RF.joblib")
    


    
def EXIT():
    root.destroy()



frame = tk.LabelFrame(root,text="Control Panel",width=200,height=500,bd=1,background="cyan2",font=("Tempus Sanc ITC",15,"bold"))
frame.place(x=5,y=50)

# button1 = tk.Button(frame,command=XG_BOOST,text="XG_BOOST",bg="white",fg="black",width=15,font=("Times New Roman",15,"italic"))
# button1.place(x=5,y=1)

button2 = tk.Button(frame,command=SVM,text="SVM",bg="white",fg="black",width=15,font=("Times New Roman",15,"italic"))
button2.place(x=5,y=50)

# button3 = tk.Button(frame,command=NB,text="Naivey Bayes",bg="white",fg="black",width=15,font=("Times New Roman",15,"italic"))
# button3.place(x=5,y=100)

button4 = tk.Button(frame,command=DT,text="Decision Tree",bg="white",fg="black",width=15,font=("Times New Roman",15,"italic"))
button4.place(x=5,y=150)

# button5 = tk.Button(frame,command=RF,text="Random Forest",bg="white",fg="black",width=15,font=("Times New Roman",15,"italic"))
# button5.place(x=5,y=200)

#button6 = tk.Button(frame,command=VE,text="Voting Ensemble",bg="white",fg="black",width=15,font=("Times New Roman",15,"italic"))
#button6.place(x=5,y=250)

TMState=tk.IntVar()
TMState=""

from tkinter import ttk
State_Name = {"XG_BOOST":1,"SUPPORT VECTOR MACHINE":2,"NAIVEY BAYES":3,"DECISION TREE":4,"RANDOM FOREST":5}
TMStateEL=ttk.Combobox(frame,values=list(State_Name.keys()),width=25,textvariable = TMState)
TMStateEL.state(['readonly'])
TMStateEL.bind("<<ComboboxSelected>>", lambda event: print(State_Name[TMStateEL.get()]))

TMStateEL.current(0)
TMStateEL.place(x=5,y=300)

model_list = {"SUPPORT VECTOR MACHINE":"SVM.joblib","DECISION TREE":"IDS_5_CLASSIFIERSDT.joblib"}

def ok():
    
    print ("value is:" + TMStateEL.get())
    model_choice = TMStateEL.get()
    choosen_model = model_list[model_choice]
    print(choosen_model)
    from joblib import load
    ans = load(choosen_model)
    
    from tkinter.filedialog import askopenfilename
    fileName = askopenfilename(initialdir='IDS_5_CLASSIFIERS/', title='Select DataFile For INTRUSION Testing',
                                       filetypes=[("all files", "*.csv*")])
    
    file =pd.read_csv(fileName)
    file['protocol_type']=le.fit_transform(file['protocol_type'])
    file['service']=le.fit_transform(file['service'])
    file['flag']=le.fit_transform(file['flag'])

    qn = file.drop(["label"],axis=1)
    
    A = ans.predict(qn)
    print(A)
    def listToString(s): 
    
        # initialize an empty string
        str1 = "" 
        
        # traverse in the string  
        for ele in s: 
            str1 += ele  
        
        # return string  
        return str1 
    print(listToString(A)) 
    B = listToString(A)
    if B == 'normal':   
        output = 'DDOS NOT ATTACKED'
    else:
        output = 'DDOS ATTACKED'
    
    attack = tk.Label(root,text=str(output),width=30,bg='red',fg='white',font=("Times New Roman",20,'italic'))
    attack.place(x=170,y=550)
    
        
    

button7 = tk.Button(frame,command=ok,text="TEST",bg="white",fg="black",width=15,font=("Times New Roman",15,"italic"))
button7.place(x=5,y=350)

button8 = tk.Button(frame,command=EXIT,text="EXIT",bg="red",fg="black",width=15,font=("Times New Roman",15,"italic"))
button8.place(x=5,y=400)




head = tk.Label(root,text = "DDOS ATTACKED",width=100,height=1,bg='black',fg='white',font=("Tempus Sanc ITC",18,"italic"))
head.place(x=0,y=0)



root.mainloop()



