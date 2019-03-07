import requests
import re
from concurrent import futures
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
}
def get_pages(num):
    list1 = []
    for x in range(1,num + 1):
        list1.append('https://www.doutula.com/photo/list/?page=' + str(x))
    return list1      
def download_file(file_url):
    f = requests.get(file_url,headers = headers)
    file_name = file_url.split('/')[-1]
    with open(file_name,'wb') as code:
        code.write(f.content)
def make_data(url):
    html1 = requests.get(url,headers = headers)
    result1 = re.findall('data-original="(.*?)" alt',html1.text,re.S)
    return result1
    
def main():
    numbers = input('请输入要下载的页数:')
    url_list1 = get_pages(int(numbers))
    ex = futures.ThreadPoolExecutor(max_workers=10) # 更改最大线程
    print('[INFO]正在下载请稍后...')
    for x in url_list1:
        html_data = make_data(x)
        for y in range(0,68):
            try:
                img_url = html_data[y]
                ex.submit(download_file,img_url)
                #print(file_name)
            except:
                print('Error')          
    print('[INFO]已经下载到根目录') 
# 以下是主函数
if __name__ == "__main__":
    main()  



    
    





