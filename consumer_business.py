from kafka import KafkaConsumer
import json
import os

consumer = KafkaConsumer('business',group_id="consbusiness",
                         bootstrap_servers=['localhost:9092'],
                        auto_offset_reset='earliest', enable_auto_commit=True)
for message in consumer:
    try:
        formatjson = json.loads(message.value.decode('utf-8'))
        if formatjson['@type'] == 'NewsArticle':
            file_name = os.path.join('./data/business',str(formatjson['mainEntityOfPage']).split('-')[-1].split('.')[0])
            #print(file_name)
            file_handle = open(file_name,"w")
            file_handle.write(formatjson['articleBody'])
            file_handle.close()
    except:
        print("Error Parsing JSON")