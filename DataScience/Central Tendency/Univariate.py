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