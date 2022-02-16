import pandas as pd
def getData(file_name):
    
    chat = []

    # data frame
    df = pd.read_csv(file_name, 
    sep='\n\n', 
    encoding='latin 1',
    header=None,
    engine='python')

    for i in range(df.shape[0]):
        data = {}
        msg = list(df.iloc[i].values)[0]
        
        fi = msg.find('M - ')
        d_and_t = msg[ : ( fi + 1 ) ]
        
        msg = msg[fi+4:]
        
        fi = msg.find(':')
        if fi == -1:
            # if the message doesn't have and authour like security msg
            continue
        author = msg[:fi]
        
        text = msg[fi+2:]
        
        d_and_t = d_and_t.split(', ')
        d_and_t.append(author)
        d_and_t.append(text)
        
        #here d_and_t is list so we convert it to dictonary
        
        val = d_and_t[0].split('/')
        try:
            data['month'] = int(val[0])
            data['day'] = int(val[1])
            data['year'] = int(val[2])
        except:
            continue
        
        val = d_and_t[1].split()
        data['meridiem'] = val[1]
        
        val = val[0].split(':')
        
        data['hour'] = int(val[0])
        data['minute'] = int(val[1])
        
        data['author'] = d_and_t[2]
        data['message'] = d_and_t[3]
        
        chat.append(data)

    dff = pd.DataFrame.from_dict(chat)
    
    return dff, list(set(dff['author']))
