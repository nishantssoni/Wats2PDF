import pandas as pd
import re

def getData(file_name):
    """
    Read a WhatsApp chat log file and extract the data into a pandas DataFrame.

    Parameters:
        file_name (str): The path or name of the chat log file.

    Returns:
        DataFrame: A pandas DataFrame containing the extracted chat data.
        list: A list of unique authors in the chat.

    """
   
    # Create an empty list to store the extracted chat data 
    chat = []

    # Read the chat log file into a pandas DataFrame
    df = pd.read_csv(file_name, 
    sep='\n\n',
    header=None,
    engine='python')

    # Iterate over the rows of the DataFrame (skipping the header)
    for i in range(1,df.shape[0]):
        data = {}
        msg = df.iloc[i].values[0]
        
        try:
            # Extract the date from the message using a regular expression
            date_pattern = r"\d{2}/\d{2}/\d{4}" 
            dates = re.findall(date_pattern, msg)[0]

            # Extract the time from the message using a regular expression
            # here space number in ascii 32 , but here it is 8239 in ascii which called 'Narrow No-Break Space'
            time_pattern = r"\d{1,2}:\d{2} [ap]m"
            times = re.findall(time_pattern, msg)[0]
            times = times.replace(' ',' ')    # Replace the narrow no-break space with a regular space


            # Extract the message text from the message
            matches = re.finditer(r" - .*?:", msg)
            last_index = 0
            for match in matches:
                last_index = match.end()
                break
            message = msg[last_index:]
            
            # Extract the day, month, and year from the date
            data['day'] = int(dates.split('/')[0])
            data['month'] = int(dates.split('/')[1])
            data['year'] = int(dates.split('/')[2])
            
            
            # Extract the hour, minute, and meridiem from the time
            vals = times.split() #['12:45', 'am']
            data['hour'] = int(vals[0].split(':')[0])
            data['minute'] = int(vals[0].split(':')[1])
            data['meridiem'] = vals[1]

            # Store the message and author in the data dictionary
            data['message'] = message
            auth = re.findall(r" - .*?:", msg)[0]
            data['author'] = auth[3:-1]
            
            # Append the data dictionary to the chat list
            chat.append(data)
        except:
            continue
    # Create a DataFrame from the chat list
    dff = pd.DataFrame.from_dict(chat)
    
    # Get a list of unique authors in the chat
    authors = list(set(dff['author']))

    # Return the DataFrame and the list of authors
    return dff, authors
