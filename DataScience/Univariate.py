class Univariate():
    def quanqual(Dataset):
        quan=[]
        qual=[]
        for columnName in Dataset.columns:
            if(Dataset[columnName].dtype=='O'):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual
    
    def freqTable(columnName,Dataset):
        freqTable=pd.DataFrame(columns=['Unique_Values','Frequency','Relative Frequency','Cusum'])
        freqTable['Unique_Values']=Dataset[columnName].value_counts().index
        freqTable['Frequency']=Dataset[columnName].value_counts().values
        freqTable['Relative Frequency']=(freqTable['Frequency']/103)
        freqTable['Cusum']=freqTable['Relative Frequency'].cumsum()
        return freqTable
    
    def Univariate(Dataset,quan):
        descriptive=pd.DataFrame(index=['Mean','Median','Mode','Q1:25%','Q2:50%','Q3:75%','99%','Q4:100%','IQR',
                                    '1.5rule','Lesser','Greater','Min','Max'],columns=quan)
            for columnName in quan:
                descriptive[columnName]['Mean']=Dataset[columnName].mean()
                descriptive[columnName]['Median']=Dataset[columnName].median()
                descriptive[columnName]['Mode']=Dataset[columnName].mode()[0]
                descriptive[columnName]['Q1:25%']=Dataset.describe()[columnName]['25%']
                descriptive[columnName]['Q2:50%']=Dataset.describe()[columnName]['50%']
                descriptive[columnName]['Q3:75%']=Dataset.describe()[columnName]['75%']
                descriptive[columnName]['99%']=np.percentile(Dataset[columnName],99)
                descriptive[columnName]['Q4:100%']=Dataset.describe()[columnName]['max']
                descriptive[columnName]['IQR']=descriptive[columnName]['Q3:75%']-descriptive[columnName]['Q1:25%']
                descriptive[columnName]['1.5rule']=1.5*descriptive[columnName]['IQR']
                descriptive[columnName]['Lesser']=descriptive[columnName]['Q1:25%']-descriptive[columnName]['1.5rule']
                descriptive[columnName]['Greater']=descriptive[columnName]['Q3:75%']+descriptive[columnName]['1.5rule']
                descriptive[columnName]['Min']=Dataset[columnName].min()
                descriptive[columnName]['Max']=Dataset[columnName].max()

            return descriptive
    
    def ReplaceOutlier(Dataset,lesser,greater):
        for columnName in lesser:
            Dataset[columnName][Dataset[columnName]<descriptive[colunName]['Lesser']]=descriptive[colunName]['Lesser']
        for columnName in greater:
            Dataset[columnName][Dataset[columnName]>descriptive[colunName]['Greater']]=descriptive[colunName]['Greater']

        return lesser,greater
    
    def outliercolumnnames(descriptive,quan):
        lesser=[]
        greater=[]
        for colunName in quan:
            if(descriptive[colunName]['Min']<descriptive[colunName]['Lesser']):
                lesser.append(colunName)
            if(descriptive[colunName]['Max']>descriptive[colunName]['Greater']):
                greater.append(colunName)

        return lesser,greater