# coding = utf-8
"""
命令行火车票查询器

Usage:
    tickets [-gdtkz] <from> <to> <date>
Options:
    -h, --help  显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-01-01
    tickets -dg 成都 新疆 2016-10-10
"""
from docopt import docopt
from parse_station import stations
import requests

class TrainCollectioin:
    header = '车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()
    def __init__(self,available_trains,options):
        """查询到的火车班次集合
        ：param available_trains:一个列表，包含可获得的火车班次，每个火车班次是一个字典
        ：param options: 查询的选项，如高铁，动车，etc...
        """
        self.available_trains = available_trains
        self.options = options
    def _get_duration(self,raw_train):
        duration = raw_train.get('lishi').replace(':','小时') + '分'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return  duration


def cli():
    '''command-line interface'''
    arguments = docopt(__doc__)
    print(arguments)
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments.get(arguments['<date>'])
    # 构建URL
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(
        date, from_station, to_station
    )
    #添加verify=False参数不验证证书
    r = requests.get(url,verify=False)
    print(r.json())
    available_trains = r.json()['date']['datas']

if __name__ == '__main__' :
    cli()