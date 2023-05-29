import pandas as pd
import re

def getData(file_name):
    
    chat = []

    # data frame
    df = pd.read_csv(file_name, 
    sep='\n\n',
    header=None,
    engine='python')

    for i in range(1,df.shape[0]):
        data = {}
        msg = df.iloc[i].values[0]
        
        try:
            date_pattern = r"\d{2}/\d{2}/\d{4}"  # Regular expression pattern to match dates in DD-MM-YYYY seperated by /
            dates = re.findall(date_pattern, msg)[0]

            #here space number in ascii 32 , but here it is 8239 in ascii which called 'Narrow No-Break Space'
            time_pattern = r"\d{1,2}:\d{2} [ap]m"  # Regular expression pattern to match time
            times = re.findall(time_pattern, msg)[0]
            times = times.replace(' ',' ')    #both space are different converting ascii 8239 to ascii 32


            #message
            matches = re.finditer(r" - .*?:", msg)
            last_index = 0
            for match in matches:
                last_index = match.end()
                break
            message = msg[last_index:]
            
            
            data['day'] = int(dates.split('/')[0])
            data['month'] = int(dates.split('/')[1])
            data['year'] = int(dates.split('/')[2])
            
            
            #times
            vals = times.split() #['12:45', 'am']

            data['hour'] = int(vals[0].split(':')[0])
            data['minute'] = int(vals[0].split(':')[1])
            data['meridiem'] = vals[1]

            #message
            data['message'] = message
            
            #author
            auth = re.findall(r" - .*?:", msg)[0]
            
            data['author'] = auth[3:-1]

            chat.append(data)
        except:
            continue
    dff = pd.DataFrame.from_dict(chat)

    return dff, list(set(dff['author']))
