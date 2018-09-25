#coding=utf-8
#!/bin/python
#
# -*- coding: utf-8-*-
import re


##过滤HTML中的标签
# 将HTML中标签等信息去掉
# @param htmlstr HTML字符串.
def filter_tags(htmlstr):
    # 先过滤CDATA
    re_cdata = re.compile('//<!/[CDATA/[[^>]*///]/]>', re.I)  # 匹配CDATA
    re_script = re.compile('</s*script[^>]*>[^<]*</s*//s*script/s*>', re.I)  # Script
    re_style = re.compile('</s*style[^>]*>[^<]*</s*//s*style/s*>', re.I)  # style
    re_br = re.compile('<br/s*?/?>')  # 处理换行
    re_h = re.compile('</?/w+[^>]*>')  # HTML标签
    re_comment = re.compile('<!--[^>]*-->')  # HTML注释
    s = re_cdata.sub('', htmlstr)  # 去掉CDATA
    s = re_script.sub('', s)  # 去掉SCRIPT
    s = re_style.sub('', s)  # 去掉style
    s = re_br.sub('/n', s)  # 将br转换为换行
    s = re_h.sub('', s)  # 去掉HTML 标签
    s = re_comment.sub('', s)  # 去掉HTML注释
    # 去掉多余的空行
    blank_line = re.compile('/n+')
    s = blank_line.sub('/n', s)
    s = replaceCharEntity(s)  # 替换实体
    return s


##替换常用HTML字符实体.
# 使用正常的字符替换HTML中特殊的字符实体.
# 你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
# @param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                     'lt': '<', '60': '<',
                     'gt': '>', '62': '>',
                     'amp': '&;', '38': '&;',
                     'quot': '"', '34': '"', }

    re_charEntity = re.compile(r'&;#?(?P<name>/w+);')
    sz = re_charEntity.search(htmlstr)
    while sz:
        entity = sz.group()  # entity全称,如&;gt;
        key = sz.group('name')  # 去除&;;后entity,如&;gt;为gt
        try:  # by www.ahlinux.com
            htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
        except KeyError:
            # 以空串代替
            htmlstr = re_charEntity.sub('', htmlstr, 1)
            sz = re_charEntity.search(htmlstr)
    return htmlstr


def repalce(s, re_exp, repl_string):
    return re_exp.sub(repl_string, s)


if __name__ == '__main__':
    strsd='<li class="pagation"><a href="https://www.aliyun.com/jiaocheng/481404.html" class="next">上一篇</a><a href="https://www.aliyun.com/jiaocheng/481403.html" class="one">1</a><a href="https://www.aliyun.com/jiaocheng/481402.html">2</a><a href="https://www.aliyun.com/jiaocheng/481408.html">3</a><a href="https://www.aliyun.com/jiaocheng/481407.html">4</a><a href="https://www.aliyun.com/jiaocheng/481406.html" class="next">下一篇</a></li>'
    ttss=re.sub(r'<a(.*?)>','',strsd,0,re.S)
    ttss = re.sub(r'</a.*?>', '', ttss,0, re.S)
    print ttss
    # s = file('Google.htm').read()
    # news = filter_tags(s)
    # print news
