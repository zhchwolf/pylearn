#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import re
import sys

main_url = 'http://www.lishi.com'

def get_encodings_from_content(content):
    """Returns encodings from given content string.
    :param content: bytestring to extract encodings from.
    """
    charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
    #pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
    pragma_re = re.compile(r'<meta.*?charset=(.+?)["\'/>]', flags=re.I)
    xml_re = re.compile(r'^<\?xml.*?encoding=["\']*(.+?)["\'>]')
    return (pragma_re.findall(content))
            # charset_re.findall(content)
            # pragma_re.findall(content) +
            # xml_re.findall(content)

def image_list(main_url):
    req_url = requests.get(main_url).text
    # print(req_url)
    charset = get_encodings_from_content(req_url)
    print(charset)
image_list(main_url)
