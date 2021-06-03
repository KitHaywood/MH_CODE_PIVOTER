import pandas as pd

def parser(df):
    df['1or2'] = [x.split('-')[-1] for x in df['Project ID']]
    df2 = df[df['1or2']=='2'].reset_index()
    df6 = df[(df['1or2']=='6') | (df['1or2']=='1') | (df['1or2']=='3')].reset_index()
    df2['NMS_CODE'] = [x.split(')')[-1] for x in df2['Project Name']]

    def extract_MH_names(item):
        if len(str(item))<10:
            item = item
        if '(Target 20-05-21)' and ',' in item:
            item = item.split(',')[0]
        elif '(Target 21-01-21)' and ',' in item:
            item = item.split(',')[0]
        elif '(Target 21-01-21)' in item and ',' not in item:
            item = item.split('Template-')[0]
        elif ',' not in item:
            item = item.split('Template-')[0]
        else:
            pass
        return item
    
    def extract_name(item):
        if 'MH' in item:
            groups = item.split(' ')
            item = ' '.join(groups)[2:]
        else:
            item = item.split(' ')[1]
        return item
    
    def final_extract(item):
        if len(item.split(' '))>2:
            item = ' '.join(item.split(' ')[1:])
        else:
            pass
        return item

    df2['MH_NAME'] = df2['Project Name'].apply(lambda x: extract_name(extract_MH_names(x)))
    df6['MH_NAME'] = df6['Project Name'].apply(lambda x: extract_name(extract_MH_names(x)))
    df2['MH_NAME'] = df2['MH_NAME'].apply(lambda x:final_extract(x))
    df6['MH_NAME'] = df6['MH_NAME'].apply(lambda x:final_extract(x))
    return df2,df6 

if __name__ == '__main__':
    data = parser(pd.read_excel('paul_update_020621.xlsx',engine='openpyxl'))
    data2,data6 = data[0],data[1]
    print(data2.to_markdown(),data6.to_markdown())


    