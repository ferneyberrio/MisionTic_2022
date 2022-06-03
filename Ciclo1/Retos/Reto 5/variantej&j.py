import csv, json
def solucion():
    archivo=open('JandJ.csv')
    x=csv.reader(archivo)
    Date=[]
    Open=[]
    High=[]
    Low=[]
    Close=[]
    Adj_Close=[]
    Volume=[]
    
    next(x,None)
    for i in x:
        Date.append(i[0])
        Open.append(float(i[1]))
        High.append(float(i[2]))
        Low.append(float(i[3]))
        Close.append(float(i[4]))
        Adj_Close.append(float(i[5]))
        Volume.append(int(i[6]))
    
    archivo.close()
    n=len(Date)
    alza=[]
    Abs=[]
    for i in range(n):
        resta=Close[i]-Open[i]
        Abs.append(abs(Close[i]-Open[i]))
        if resta>0:
            alza.append('SUBE')
        elif resta<0:
            alza.append('BAJA')
        elif resta==0:
            alza.append('ESTABLE')
        
            
    #Creación de archivo CSV
    with open('analisis_archivo.csv','w') as file:
        file.write('Fecha analizada\tComportamiento de la accion\tabs Diferencia Close-Open\n')
        for i in range(n):
            file.write('%s\t' % Date[i])
            file.write('%s\t' % alza[i])
            file.write('%s\n' % Abs[i])
        file.close()
    
    dic={}
    lowest=min(Volume)
    highest=max(Volume)
    mean=sum(Volume)/len(Volume)
    greatest=max(Abs)
    
    for i in range(n):
        if Volume[i]==lowest:
            dic['date_lowest_volume']=Date[i]
            dic['lowest_volume']=lowest
        if Volume[i]==highest:
            dic['date_highest_volume']=Date[i]
            dic['highest_volume']=highest
        dic['mean_volume']=mean
        if Abs[i]==greatest:
            dic['date_greatest_difference']=Date[i]
            dic['greatest_difference']=greatest
    with open('detalles.json','w') as file:
        json.dump(dic,file)