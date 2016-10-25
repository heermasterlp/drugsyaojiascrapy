# coding: utf-8
import time
import urllib2
from bs4 import BeautifulSoup

'''
    Scrapy data from: http://drugs.yaojia.org/

    The basic website: http://www.yaojia.org/thread-26281-1-1.html?_dsign=5ea81f5c
'''

class DrugyaojiaScrapy:

    def __init__(self, path, url):
        self.path = path     # save data file
        self.url = url       # url of website

    def __del__(self):
        pass

    # parse the website
    def parse(self):

        # parse website from 13-624 page
        with open(self.path, 'w') as file:

            for page_num in range(13, 14):

                page_source = urllib2.urlopen(self.url + str(page_num))
                if page_source == None:
                    print 'page source is None!'
                    continue
                # bs4
                bsObj = BeautifulSoup(page_source.read())

                if bsObj == None:
                    print 'bs object is none!'
                    continue

                print '----dt----'
                dts = bsObj.find_all('dt')
                print len(dts)

                print '----dd---'
                dds = bsObj.find_all('dd')
                print len(dds)

                jsondata = '{'
                if len(dds) != len(dts):
                    print '__len__not__match:', page_num
                    continue
                else:
                    length = len(dts)
                    for index in range(0, length):
                        dtStr = dts[index].get_text().encode('utf-8').strip()
                        ddStr = dds[index].get_text().encode('utf-8').strip()

                        # if '\n' in ddStr:
                        #     print type(ddStr)
                        #     ddStr = str.replace(ddStr,'\n','')

                        # if '\n' in ddStr:
                        #     # print ddStr
                        #     # print '\\n in string'
                        #     # ddStr = ddStr.replace('\n','')
                        #     ddsplits = ddStr.split('\n')
                        #
                        #     print 'split len:', len(ddsplits)
                        #     line = ''
                        #     for sp in ddsplits:
                        #         print 'sp:', sp
                        #         line += sp
                        #     print 'line:', line
                        #     ddStr = line


                        print ddStr
                        print '---------'
                        if dtStr == '' and index == 1:
                            jsondata += '"摘要":"' + ddStr + '",'

                        elif index == length - 1:    # end the json data
                            jsondata += '"' + dtStr + '":"' + ddStr + '"}'
                        else:
                            jsondata += '"' + dtStr + '":"' + ddStr + '",'


                # print jsondata

                if '\n' in jsondata:
                    jsondata = jsondata.replace('\n','')

                print jsondata

                # file.write(jsondata)



                time.sleep(4)

        print 'write end!'




if __name__ == '__main__':

    url = 'http://drugs.yaojia.org/index.php?m=drugs&c=index&a=show&catid=7&id='
    path = '/Users/heermaster/Documents/python/googlepatentsscrapy/src/drugsyaojiajsondata.txt'

    drugsyaojiascrapy = DrugyaojiaScrapy(path, url)

    print 'begin parse'
    drugsyaojiascrapy.parse()

    print 'end parse'


    # page = urllib2.urlopen(url)
    #
    # bsObj = BeautifulSoup(page.read())
    #
    # div = bsObj.find('div', {'class' : 'detail'})
    #
    # print '----dt----'
    # dts = bsObj.find_all('dt')
    # print len(dts)
    # # if dts:
    # #     for dt in dts:
    # #         print dt.get_text()
    #
    #
    #
    # print '----dd----'
    # dds = bsObj.find_all('dd')
    # print len(dds)
    # # if dds:
    # #     for dd in dds:
    # #         print dd.get_text()
    #
    # for i in range(0,11):
    #     if dts[i].get_text().strip() == '' and i == 1:
    #         print '摘要', ' : ', dds[i].get_text().strip()
    #     else:
    #         print dts[i].get_text().strip(), ' : ', dds[i].get_text().strip()




    # print div.get_text()
