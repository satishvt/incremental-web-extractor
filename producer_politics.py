import requests
from bs4 import BeautifulSoup
import json,sys
import hashlib 
import psycopg2
from kafka import KafkaProducer
import warnings
warnings.filterwarnings('ignore')

    

class databasec():
    def __init__(self, db="news", user="satishvt"):
        self.conn = psycopg2.connect(database=db, user=user)
        self.cur = self.conn.cursor()
    def query(self, query):
        self.cur.execute(query)
    def commit(self):
        self.conn.commit()
        
    def close(self):
        self.cur.close()
        self.conn.close()
        
        
def check_record_add(article_num,hash):
    queryx = "SELECT hash FROM tables.firstpost WHERE url = \'" + article_num + "\';"
    add_query = "INSERT INTO tables.firstpost(url,hash) VALUES({},\'{}\')".format(article_num,hash)
    update_query = "UPDATE tables.firstpost set hash=\'{}\' where url={}".format(hash,article_num)
    db.query(queryx)
    record_present = db.cur.fetchone()
    if record_present:
        if record_present[0] == hash:
            return True
        else:
            db.query(update_query)
            db.commit()  
            return False
    else:
        db.query(add_query)
        db.commit()  
        return False
    

def extract_news_content(url):
    #print(url)
    news_article_full = requests.get(url)
    idx = "article-full-content_" + url.split('-')[-1].split('.')[0]    
    soupx = BeautifulSoup(news_article_full.text, "html.parser")
    result_block = soupx.findAll("script", {"type": "application/ld+json"})

    for ptext in result_block:
        try:
            xy = ptext.string.strip().replace("\n","").replace("\r","")
            if xy.startswith("["):
                xy = xy[1:][:-1]
            xy_json = json.loads(xy)
            xyd_json = json.dumps(xy_json).encode('utf-8')
            hash_object = hashlib.md5(str(xy_json['articleBody']).encode())
            
            article_num = url.split('-')[-1].split('.')[0]
            statusc = check_record_add(article_num,hash_object.hexdigest())
            if statusc:
                pass
            else:
                try:
                    sendresult = producer.send('politics', value=xyd_json)
                    try:
                        record_metadata = sendresult.get(timeout=10)
                        print(record_metadata)
                    except KafkaError as ex:
                        print(ex)
                except KafkaError:
                    print(traceback.format_exc())
            break
        except:
            print("error")
        

db = databasec()
producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])

r = requests.get('https://www.firstpost.com/category/politics')

soup = BeautifulSoup(r.text, 'html.parser')

result_block = soup.find_all('a')

for result in result_block:
    try:
        if (result['href'].startswith("https://www.firstpost.com/politics/")) & (result['href'].endswith('.html')):
            extract_news_content(result['href'])
    except:
        pass

db.close()