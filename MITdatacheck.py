import wfdb
import matplotlib.pyplot as plt
import numpy as np

# label2description=[
# {"label":"N","description":"Normal beat"},
# {"label":"L","description":"Left bundle branch block beat"},
# {"label":"R","description":"Right bundle branch block beat"},
# {"label":"a","description":"Aberrated atrial premature beat"},
# {"label":"V","description":"Premature ventricular contraction"},
# {"label":"F","description":"Fusion of ventricular and normal beat"},
# {"label":"J","description":"Nodal (junctional) premature beat"},
# {"label":"A","description":"Atrial premature contraction"},
# {"label":"S","description":"Premature or ectopic supraventricular beat"},
# {"label":"E","description":"Ventricular escape beat"},
# {"label":"j","description":"Nodal (junctional) escape beat"},
# {"label":"/","description":"Paced beat"},
# {"label":"Q","description":"Unclassifiable beat"},
# {"label":"~","description":"Signal quality change"},
# {"label":"|","description":"Isolated QRS-like artifact"},
# {"label":"s","description":"ST change"},
# {"label":"T","description":"T-wave change"},
# {"label":"*","description":"Systole"},
# {"label":"D","description":"Diastole"},
# {"label":"\"","description":"Comment annotation"},
# {"label":"=","description":"Measurement annotation"},
# {"label":"p","description":"P-wave peak"},
# {"label":"B","description":"Left or right bundle branch block"},
# {"label":"^","description":"Non-conducted pacer spike"},
# {"label":"t","description":"T-wave peak"},
# {"label":"+","description":"Rhythm change"},
# {"label":"u","description":"U-wave peak"},
# {"label":"?","description":"Learning"},
# {"label":"!","description":"Ventricular flutter wave"},
# {"label":"[","description":"Start of ventricular flutter/fibrillation"},
# {"label":"]","description":"End of ventricular flutter/fibrillation"},
# {"label":"e","description":"Atrial escape beat"},
# {"label":"n","description":"Supraventricular escape beat"},
# {"label":"@","description":"Link to external data (aux_note contains URL)"},
# {"label":"x","description":"Non-conducted P-wave (blocked APB)"},
# {"label":"f","description":"Fusion of paced and normal beat"},
# {"label":"(","description":"Waveform onset"},
# {"label":")","description":"Waveform end"},
# {"label":"r","description":"R-on-T premature ventricular contraction"}
# ]

annotation= wfdb.rdann('100','atr')
record_name=annotation.record_name     #读取记录名称
label1=annotation.symbol #心拍的标签
label2=annotation.aux_note  #节律片段的标签
label_index=annotation.sample   #标签索引
record=wfdb.rdsamp('100')#读取100记录
linkwire=record[1].get("sig_name")
#print(record[1])
#{'fs': 360, 'sig_len': 650000, 'n_sig': 2, 'base_date': None, 'base_time': None, 'units': ['mV', 'mV'], 'sig_name': ['MLII', 'V5'], 'comments': ['69 M 1085 1629 x1', 'Aldomet, Inderal']}


'''将心拍按人工标记切片'''
wantedlabel="N"
wantedlabel_index=[]
saveimage=False#是否保存二值化的图片
needperfectECG=True#是否只保存完整心拍
# print(label1[2])
# print(label_index[2])
for i in range(len(label1)):
    if label1[i]==wantedlabel:
        wantedlabel_index.append(label_index[i])
#print(record[1])
#print(wantedlabel_index)
filesaver1=open(record_name+" " + wantedlabel +" "+ linkwire[0] + " data.txt","w",encoding="utf-8")
filesaver2=open(record_name +" "+ wantedlabel +" " +linkwire[1] + " data.txt","w",encoding="utf-8")
j = 1
for i in wantedlabel_index:
    if (i-100>=0)&(i+150<=len(record[0])):
        heartwave_type=record[0][i-100:i+150]
        heartwave_type=np.array(heartwave_type)
        #print(len(heartwave_type))
        #print(heartwave_type)
        heartwave_type1 = heartwave_type[:,0]
        filesaver1.write(str(heartwave_type1)+"\n")
        #print(heartwave_type1)
        heartwave_type2 = heartwave_type[:,1]
        filesaver2.write(str(heartwave_type2) + "\n")
        #print(heartwave_type2)
        if saveimage==True:
            plt.plot(range(250), heartwave_type1, "black")
            plt.axis('off')  # 关闭坐标轴
            plt.savefig(record_name + " " + wantedlabel + " " + linkwire[0] + " " + str(j) + ".png")
            plt.show()
            plt.plot(range(250), heartwave_type2, "black")
            plt.axis('off')  # 关闭坐标轴
            plt.savefig(record_name + " " + wantedlabel + " " + linkwire[1] + " " + str(j) + ".png")
            plt.show()
    else:
        if needperfectECG==False:
            if i - 100 < 0:
                heartwave_type = record[0][0:i + 150]
                heartwave_type = np.array(heartwave_type)
                heartwave_type1 = heartwave_type[:, 0]
                filesaver1.write(str(heartwave_type1) + "\n")
                heartwave_type2 = heartwave_type[:, 1]
                filesaver2.write(str(heartwave_type2) + "\n")
                if saveimage == True:
                    plt.plot(range(len(heartwave_type1)), heartwave_type1, "black")
                    plt.axis('off')  # 关闭坐标轴
                    plt.savefig(record_name + " " + wantedlabel + " " + linkwire[0] + " " + str(j) + ".png")
                    plt.show()
                    plt.plot(range(len(heartwave_type2)), heartwave_type2, "black")
                    plt.axis('off')  # 关闭坐标轴
                    plt.savefig(record_name + " " + wantedlabel + " " + linkwire[1] + " " + str(j) + ".png")
                    plt.show()
            else:
                heartwave_type = record[0][i - 100:len(record[0])]
                heartwave_type = np.array(heartwave_type)
                heartwave_type1 = heartwave_type[:, 0]
                filesaver1.write(str(heartwave_type1) + "\n")
                heartwave_type2 = heartwave_type[:, 1]
                filesaver2.write(str(heartwave_type2) + "\n")
                if saveimage == True:
                    plt.plot(range(len(heartwave_type1)), heartwave_type1, "black")
                    plt.axis('off')  # 关闭坐标轴
                    plt.savefig(record_name + " " + wantedlabel + " " + linkwire[0] + " " + str(j) + ".png")
                    plt.show()
                    plt.plot(range(len(heartwave_type2)), heartwave_type2, "black")
                    plt.axis('off')  # 关闭坐标轴
                    plt.savefig(record_name + " " + wantedlabel + " " + linkwire[1] + " " + str(j) + ".png")
                    plt.show()
    j=j+1
    # plt.axis('off')#关闭坐标轴
    # plt.savefig(record_name+wantedlabel+linkwire[0]+str(i) + ".png")
    # plt.show()
#print(label_index)
#print(record)
#if label[j]=='A' or label[j]=='a' or label[j]=='J' or label[j]=='S':
#    Seg=record[label_index[j]-144:label_index[j]+180]
#    segment=resample(Seg,251, axis=0) #根据文章要求，重采样到251个点
#    SVEB_Seg.append(segment)
#starttime=1000
#endtime=5000
#i=0
#while True:
#    if endtime<label_index[i]:
#        break
#    i=i+1
#for j in range(i):
#    print("第",j+1,"个波形的标签为",label1[j])
#time=list(range(0,650000, 1))
#voltage=[]
#for i in range(len(record[0])):
#    voltage.append(record[0][i][0])#采样频率360Hz,时间长度650000,单位mV,0为MLII,1为V5， 'n_sig': 2,'comments': ['69 M 1085 1629 x1', 'Aldomet, Inderal']
#plt.plot(time[starttime:endtime],voltage[starttime:endtime])
#plt.show()