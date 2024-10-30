# -*- coding: utf-8 -*-

import requests
import json
from fake_useragent import UserAgent
import logging


TIMEOUT = 7


class YaDiskAPI:
    '''
    Class for getting and saving video from Yandex.Disk
    '''

    def __init__(self):
        st_useragent = UserAgent().random

        self.headers = {
            "Accept": "application/json;charset=utf-8",
            "User-Agent": st_useragent,
            "Content-Type": "application/json",
        }
        
        self.session = requests.Session()
        logging.info('Session object creation successful')
    
    def get_video(self, url: str) -> None:
        self.get_download_url = f'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={url}'
        
        try:
            sub = self.session.get(self.get_download_url, headers=self.headers, timeout=TIMEOUT)
            self.download_url = json.loads(sub.text)["href"]

            self.raw_video_data = self.session.get(self.download_url, headers=self.headers, timeout=TIMEOUT)

        except Exception as e:
            self.raw_video_data = -1
            logging.error(f'Error receiving video: {repr(e)}')
            raise ConnectionError("Check the internet connection...")
    
    def save_video(self, path: str) -> str:
        if self.raw_video_data.status_code == 200:
            with open(path, 'wb') as video_file:
                filesize = video_file.write(self.raw_video_data.content)
            logging.info(f'A video file with a length of {filesize} bit was successfully saved')
            return filesize
        
        else:
            logging.error(f'Failed to get a response: <{self.raw_video_data.status_code}>')