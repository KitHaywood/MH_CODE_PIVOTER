import pandas as pd

def loader(filename,sheet):
    data = pd.read_excel(filename, sheet_name=sheet,engine='openpyxl')
    print(data.columns)
    def nan_replacer(item):
        if isinstance(item,float):
            item = ' '
        else:
            pass
        return item
    data['P6'] = data['P6'].apply(lambda x: nan_replacer(x))
    data['MH_CODE_TYPE'] = [type(x) for x in data['P6']]
    print(data)
    data['MH_CODE'] = [x.split(',')[0] for x in data['P6']]
    return data

if __name__=='__main__':
    data = loader('george_confirm.xlsx','WORKING')    
    print(data)

