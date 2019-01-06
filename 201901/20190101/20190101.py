# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-06 20:43:46
@LastEditTime: 2019-01-06 22:24:08
@Description: 
'''

from splinter.driver.webdriver.chrome import Options,Chrome
from splinter.browser import Browser
from contextlib import closing
import requests, json, time, re, os, sys, time
from bs4 import BeautifulSoup

class DouYin(object):
    def __init__(self, width=500, height=300):
        """
        抖音App视频下载
        """
        chrome_options = Options()
        chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"')
        self.driver = Browser(driver_name='chrome', executable_path=r'F:\software\chromedriver_win32\chromedriver', options=chrome_options, headless=True)

    def get_video_urls(self, user_id):
        video_names = []
        video_urls = []
        unique_id = ''
        while unique_id != user_id:
            search_url = f'https://api.amemv.com/aweme/v1/discover/search/?cursor=0&keyword={user_id}&count=10&type=1&retry_type=no_retry&iid=17900846586&device_id=34692364855&ac=wifi&channel=xiaomi&aid=1128&app_name=aweme&version_code=162&version_name=1.6.2&device_platform=android&ssmix=a&device_type=MI+5&device_brand=Xiaomi&os_api=24&os_version=7.0&uuid=861945034132187&openudid=dc451556fc0eeadb&manifest_version_code=162&resolution=1080*1920&dpi=480&update_version_code=1622'
            req = requests.get(url = search_url, verify=False)
            html = json.loads(req.text)
            aweme_count = html['user_list'][0]['user_info']['aweme_count']
            uid = html['user_list'][0]['user_info']['uid']
            nickname = html['user_list'][0]['user_info']['nickname']
            unique_id = html['user_list'][0]['user_info']['unique_id']
        user_url = f'https://www.douyin.com/aweme/v1/aweme/post/?user_id={uid}&max_cursor=0&count={aweme_count}'
        req = requests.get(url=user_url, verify=False)
        html = json.loads(req.text)
        i = 1
        for each in html['aweme_list']:
            share_desc = each['share_info']['share_desc']
            if '抖音-原创音乐短视频社区' == share_desc:
                video_names.append(str(i) + '.mp4')
                i += 1
            else:
                video_names.append(share_desc + '.mp4')
            video_urls.append(each['share_info']['share_url'])
        
        return video_names, video_urls, nickname

    def get_download_url(self, video_url):
        req = requests.get(url=video_url, verify=False)
        bf = BeautifulSoup(req.text, 'lxml')
        script = bf.find_all('script')[-1]
        video_url_js = re.findall(r'var data = \[(.+)\];', str(script))[0]
        video_html = json.loads(video_url_js)
        download_url = video_html['video']['play_addr']['url_list'][0]
        return download_url

    def video_downloader(self, video_url, video_name, watermark_flag=True):
        size = 0
        if watermark_flag == True:
            video_url = self.remove_watermark(video_url)
        else:
            video_url = self.get_download_url(video_url)
        with closing(requests.get(video_url, stream=True, verify=False)) as response:
            chunk_size = 1024
            content_size = int(response.headers['content-length'])
            if response.status_code == 200:
                sys.stdout.write(f'[文件大小]:{content_size/chunk_size/1024:0.2f} MB\n')

                with open(video_name, 'wb') as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        file.flush

                        sys.stdout.write(f' [下载进度]: {float(size/content_size*100):.2f}\r')
                        sys.stdout.flush
    
    def remove_watermark(self, video_url):
        self.driver.visit('http://douyin.iiilab.com/')
        self.driver.find_by_tag('input').fill(video_url)
        self.driver.find_by_xpath('//button[@class="btn btn-default"]').click()
        html = self.driver.find_by_xpath('//div[@class="thumbnail"]/div/p')[0].html
        bf = BeautifulSoup(html, 'lxml')
        return bf.find('a').get('href')

    def run(self):
        user_id = input('请输入ID（例如40103580）：')
        video_names, video_urls, nickname = self.get_video_urls(user_id)
        if nickname not in os.listdir():
            os.makedirs(nickname)
        print(f'视频下载中：共有{len(video_urls)}个作品\n')
        for num in range(len(video_urls)):
            print(f'解析第{num+1}个短视频链接{video_urls[num]}中，请稍后\n')
            if '\\' in video_names[num]:
                video_name = video_names[num].replace('\\', '')
            elif '/' in video_names[num]:
                video_name = video_names[num].replace('/', '')
            else:
                video_name = video_names[num]
            self.video_downloader(video_urls[num], os.path.join(nickname, video_name))


if __name__ == "__main__":
    douyin = DouYin()
    douyin.run()