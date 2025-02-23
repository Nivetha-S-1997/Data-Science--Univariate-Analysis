class Univariate():

    def QuanQual(dataset):
    Quan=[]
    Qual=[]
    for columnName in dataset.columns:
        if dataset[columnName].dtype=="O":
            #print("Qual")
            Qual.append(columnName)
        else:
            #print("Quan")
            Quan.append(columnName)
    return Quan,Qual

    
    def descriptive(dataset,Quan):
        Univariate=pd.DataFrame(index=["Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%","IQR","1.5IQR","LesserIQR","GreaterIQR",
                                       "Min","Max","Skewness","Kurtosis","Variance","Std_Dev"], columns=Quan)
    
        for columnName in Quan:
            Univariate[columnName]["Mean"]=dataset[columnName].mean()
            Univariate[columnName]["Median"]=dataset[columnName].median()
            Univariate[columnName]["Mode"]=dataset[columnName].mode()[0]
            Univariate[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            Univariate[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            Univariate[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            Univariate[columnName]["99%"]=np.percentile(dataset[columnName],99)
            Univariate[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            Univariate[columnName]["IQR"]=Univariate[columnName]["Q3:75%"]-Univariate[columnName]["Q1:25%"]
            Univariate[columnName]["1.5IQR"]=1.5*Univariate[columnName]["IQR"]
            Univariate[columnName]["LesserIQR"]=Univariate[columnName]["Q1:25%"]-Univariate[columnName]["1.5IQR"]
            Univariate[columnName]["GreaterIQR"]=Univariate[columnName]["Q3:75%"]+Univariate[columnName]["1.5IQR"]
            Univariate[columnName]["Min"]=dataset[columnName].min()
            Univariate[columnName]["Max"]=dataset[columnName].max()
            Univariate[columnName]["Skewness"]=dataset[columnName].skew()
            Univariate[columnName]["Kurtosis"]=dataset[columnName].kurtosis()
            Univariate[columnName]["Variance"]=dataset[columnName].var()
            Univariate[columnName]["Std_Dev"]=dataset[columnName].std()
        return Univariate

    
    def frequency(dataset):
        FreqTable=pd.DataFrame(columns=["Unique_values","Frequency","Rel_freq","Cumsum"])
        
        FreqTable["Unique_values"]=dataset["ssc_p"].value_counts().index
        FreqTable["Frequency"]=dataset["ssc_p"].value_counts().values
        FreqTable["Rel_freq"]=FreqTable["Frequency"]/103
        FreqTable["Cumsum"]=FreqTable["Rel_freq"].cumsum()
        return FreqTable
        

    def pdf(dataset,startrange,endrange):
        sns.distplot(dataset,kde_kws={'color':'Green'},color='Blue')
        pyplot.axvline(startrange,color='Red')
        pyplot.axvline(endrange,color='Red')
        
        Mean=dataset.mean()
        Std_dev=dataset.std()
        print("Mean: ",Mean, "Standard deviation: ", Std_dev)
        
        dist=norm(Mean,Std_dev)
        
        values=[value for value in range(startrange,endrange)]
        probability=[dist.pdf(value) for value in values]
        prob_func=sum(probability)
        print("The area between {} & {} is {}".format(startrange,endrange,prob_func))
        return prob_func


    def stdNB(dataset):
        Mean=dataset.mean()
        Std_dev=dataset.std()
        print("Mean: ",Mean, "Standard Deviation: ",Std_dev)
        
        values=[i for i in dataset]
        z_score=[((x-Mean)/Std_dev) for x in values]
        sns.distplot(z_score,kde_kws={"color":"Red"})
        #return z_score