import os,json,requests
import pymongo

files ='E:\抖音APP'
file = os.listdir(files)  #读取files文件数据

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'Cookie': 'BAIDUID=63C607D6CCAB8879FFB894CF0108B849:FG=1; BIDUPSID=63C607D6CCAB8879FFB894CF0108B849; PSTM=1547214620; BD_UPN=12314353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_HOME=0; H_PS_PSSID=1449_28805_21121_28771_28722_28558_28839_28585_26350_28519_28627_28605'}
         ##伪装请求头
client=pymongo.MongoClient('localhost')
db = client['douyin']
esc = db['esc']
for i in file:
        with open(files+'/'+i,'rb')as fp:
                data =fp.read().decode('utf-8')
                obj = json.loads(data)
                for j in obj['aweme_list']:
                        url = j['video']['play_addr']['url_list'][0] #视频地址
                        video = requests.get(str(url),headers=head).content
                        # print(j['desc'])  ##宣传语言
                        print(j['author']['nickname'])  ##用户名字
                        name = j['author']['nickname']
                        # print(j['author']['avatar_larger'])
                        print(url)
                        con ={name:url}
                        esc.insert(con)

                        with open('%s.mp4'%(name),'wb')as fp:
                                fp.write(video)





