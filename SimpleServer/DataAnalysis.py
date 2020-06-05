#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import pymysql
import time

# 上报数据类型
REPORT_TYPE_EVENT = "0"  # 事件数据
REPORT_TYPE_PERFORMANCE = "1"  # 性能数据
REPORT_TYPE_EXCEPTION = "2"  # 异常数据

# 异常数据类型
EXCEPTION_TYPE_CRASH = "0"  # 奔溃数据
EXCEPTION_TYPE_FREEZE = "1"  # 卡顿数据

# 性能数据类型
PERFORMANCE_TYPE_REQUEST = "0"  # 网络请求耗时
PERFORMANCE_TYPE_IMAGE = "1"  # 图片下载和展示耗时
PERFORMANCE_TYPE_WEB = "2"  # 网页加载请求耗时
PERFORMANCE_TYPE_PAGE_OPEN_TIME = "3"  # 页面打开请求耗时

# 事件数据类型
EVENT_TYPE_CLICK = "0"  # 点击
EVENT_TYPE_BROWSE = "1"  # 浏览
EVENT_TYPE_MANUAL = "2"  # 手动

# update data key
REPORT_TYPE_KEY = "a"
REPORT_PARAM_KEY = "b"
REPORT_BASIC_KEY = "c"
REPORT_PROFILE_SET_KEY = "d"

# event param key
EVENT_PARAM_KET_dataType = "a"
EVENT_PARAM_KET_dataName = "b"
EVENT_PARAM_KET_viewPath = "c"
EVENT_PARAM_KET_viewId = "d"
EVENT_PARAM_KET_actionUrl = "e"
EVENT_PARAM_KET_pageAlias = "f"
EVENT_PARAM_KET_pageId = "g"
EVENT_PARAM_KET_extra = "h"

# exception param key
EXCEPTION_PARAM_KET_dataType = "a"
EXCEPTION_PARAM_KET_error = "b"
EXCEPTION_PARAM_KET_extra = "c"
EXCEPTION_PARAM_KET_abnormalStack = "d"
EXCEPTION_PARAM_KET_signal = "e"
EXCEPTION_PARAM_KET_signalName = "f"
EXCEPTION_PARAM_KET_exceptionName = "g"
EXCEPTION_PARAM_KET_exceptionReason = "h"
EXCEPTION_PARAM_KET_pagechain = "i"

# performance param key
PERFORMANCE_PARAM_KET_dataType = "a"
PERFORMANCE_PARAM_KET_dataName = "b"
PERFORMANCE_PARAM_KET_time = "c"
PERFORMANCE_PARAM_KET_url = "d"
PERFORMANCE_PARAM_KET_code = "e"
PERFORMANCE_PARAM_KET_length = "f"
PERFORMANCE_PARAM_KET_method = "g"

# common param key
COMMON_PARAM_KET_fps = "a"
COMMON_PARAM_KET_udid = "b"
COMMON_PARAM_KET_sdkVersion = "c"
COMMON_PARAM_KET_operatingSystem = "d"
COMMON_PARAM_KET_osVersion = "e"
COMMON_PARAM_KET_deviceModel = "f"
COMMON_PARAM_KET_resolution = "g"
COMMON_PARAM_KET_macAddress = "h"
COMMON_PARAM_KET_appInstallationFingerprint = "i"
COMMON_PARAM_KET_appBuildVersion = "j"
COMMON_PARAM_KET_appVersion = "k"
COMMON_PARAM_KET_carrier = "l"
COMMON_PARAM_KET_country = "m"
COMMON_PARAM_KET_language = "n"
COMMON_PARAM_KET_longitude = "o"
COMMON_PARAM_KET_latitude = "p"
COMMON_PARAM_KET_sessionId = "q"
COMMON_PARAM_KET_networkState = "r"
COMMON_PARAM_KET_timeStamp = "s"
COMMON_PARAM_KET_cpu = "t"
COMMON_PARAM_KET_memory = "u"
COMMON_PARAM_KET_quantity = "v"


class DataAnalysis:
    cursor = None
    db_connect = None

    def __init__(self):
        print('init data analysis')
        self.connect_database()

    def connect_database(self):
        self.db_connect = pymysql.connect(host='127.0.0.1',  # 连接名称，默认127.0.0.1
                                          user='root',  # 用户名
                                          passwd='12345678',  # 密码
                                          port=3306,  # 端口，默认为3306
                                          db='event_trace',  # 数据库名称
                                          charset='utf8'  # 字符编码
                                          )
        if self.db_connect:
            print("connect success")
        else:
            print("connect failed")
        self.cursor = self.db_connect.cursor()  # 生成游标对象

    def execute_insert_sql(self, sql):
        print("insert sql is: " + sql)
        try:
            self.cursor.execute(sql)
            self.db_connect.commit()
            print('insert success')
            return True
        except:
            # Rollback in case there is any error
            print('insert false')
            self.db_connect.rollback()
            return False

    def insert_basic_table(self, insert_dict):
        keys = ""
        values = ""
        time_str = '0'
        for (key, value) in insert_dict.items():
            if self.common_table_key(key) == '':
                continue
            keys += self.common_table_key(key) + ", "
            values += "'" + value + "'" + ", "
            if key == COMMON_PARAM_KET_timeStamp and value:
                time_str = value
        keys += 'time'

        try:
            values += "'" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time_str) / 1000)) + "'"
        except Exception as e:
            values += "'" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(0)) + "'"
            print(e)

        sql = "INSERT INTO basic_info (%s) VALUES (%s)" % (keys, values)
        if self.execute_insert_sql(sql):
            self.cursor.execute('SELECT MAX(id) FROM basic_info')
            data = self.cursor.fetchall()  # 通过fetchall方法获得数据
            return data[0][0]
        else:
            return -1

    def insert_param_table(self, report_type, basic_id, insert_dict):

        keys = ""
        values = ""
        for (key, value) in insert_dict.items():
            if self.param_table_key(report_type, key) == '':
                continue
            keys += self.param_table_key(report_type, key) + ", "
            values += "'" + value + "'" + ", "

        if report_type == REPORT_TYPE_EVENT:
            table_name = 'event'
        elif report_type == REPORT_TYPE_EXCEPTION:
            table_name = 'exception'
        elif report_type == REPORT_TYPE_PERFORMANCE:
            table_name = 'performance'
        else:
            table_name = ''

        if table_name:
            sql = "INSERT INTO %s (basic_id, %s) VALUES (%s, %s)" % (table_name, keys[:-2], basic_id, values[:-2])
            return self.execute_insert_sql(sql)
        else:
            return -1

    def analysis_data(self, data):
        print('start analysis')
        json_str = data.decode('utf8')
        print('receive json is: ' + json_str)
        try:
            receive_json = json.loads(json_str)
            if isinstance(receive_json, dict):
                return self.save_data_item(receive_json)
            elif isinstance(receive_json, list):
                result = True
                print('receive count %d' % len(receive_json))
                for item in receive_json:
                    result = self.save_data_item(item)
                    if not result:
                        break
                return result
            else:
                return False

        except Exception as e:
            print(e)
            return False

    def save_data_item(self, item):
        print(type(item))
        item_dict = {}
        if isinstance(item, str):
            item_dict = json.loads(item)
        elif isinstance(item, dict):
            item_dict = item
        try:
            report_type = item_dict[REPORT_TYPE_KEY]
            report_param = item_dict[REPORT_PARAM_KEY]
            report_basic = item_dict[REPORT_BASIC_KEY]
            report_profile = item_dict[REPORT_PROFILE_SET_KEY]
        except Exception as e:
            print("json analysis error: ")
            print(e)
            return False

        if self.insert_param_table(report_type, self.insert_basic_table(report_basic), report_param):
            return True
        return False

    def common_table_key(self, key):
        if key == COMMON_PARAM_KET_fps:
            return "fps"
        elif key == COMMON_PARAM_KET_udid:
            return "udid"
        elif key == COMMON_PARAM_KET_sdkVersion:
            return "sdk_version"
        elif key == COMMON_PARAM_KET_operatingSystem:
            return "operating_system"
        elif key == COMMON_PARAM_KET_osVersion:
            return "system_version"
        elif key == COMMON_PARAM_KET_deviceModel:
            return "device_model"
        elif key == COMMON_PARAM_KET_resolution:
            return "resolution"
        elif key == COMMON_PARAM_KET_macAddress:
            return "mac_address"
        elif key == COMMON_PARAM_KET_appInstallationFingerprint:
            return "install_fingerprint"
        elif key == COMMON_PARAM_KET_appBuildVersion:
            return "build_version"
        elif key == COMMON_PARAM_KET_appVersion:
            return "app_version"
        elif key == COMMON_PARAM_KET_carrier:
            return "carrier"
        elif key == COMMON_PARAM_KET_country:
            return "country"
        elif key == COMMON_PARAM_KET_language:
            return "language"
        elif key == COMMON_PARAM_KET_longitude:
            return "longitude"
        elif key == COMMON_PARAM_KET_latitude:
            return "latitude"
        elif key == COMMON_PARAM_KET_sessionId:
            return "session_id"
        elif key == COMMON_PARAM_KET_networkState:
            return "network_status"
        elif key == COMMON_PARAM_KET_timeStamp:
            return "time_stamp"
        elif key == COMMON_PARAM_KET_cpu:
            return "cpu"
        elif key == COMMON_PARAM_KET_memory:
            return "memory"
        elif key == COMMON_PARAM_KET_quantity:
            return "quantity"
        return ''

    def param_table_key(self, report_type, key):
        if report_type == REPORT_TYPE_EVENT:
            # event param key
            if key == EVENT_PARAM_KET_dataType:
                return "type"
            elif key == EVENT_PARAM_KET_dataName:
                return "name"
            elif key == EVENT_PARAM_KET_viewPath:
                return "view_path"
            elif key == EVENT_PARAM_KET_viewId:
                return "view_id"
            elif key == EVENT_PARAM_KET_actionUrl:
                return "action_url"
            elif key == EVENT_PARAM_KET_pageAlias:
                return "page_alias"
            elif key == EVENT_PARAM_KET_pageId:
                return "page_id"
            elif key == EVENT_PARAM_KET_extra:
                return "extra"

        elif report_type == REPORT_TYPE_PERFORMANCE:
            # performance param key
            if key == PERFORMANCE_PARAM_KET_dataType:
                return "type"
            elif key == PERFORMANCE_PARAM_KET_dataName:
                return "name"
            elif key == PERFORMANCE_PARAM_KET_time:
                return "time"
            elif key == PERFORMANCE_PARAM_KET_url:
                return "url"
            elif key == PERFORMANCE_PARAM_KET_code:
                return "code"
            elif key == PERFORMANCE_PARAM_KET_length:
                return "length"
            elif key == PERFORMANCE_PARAM_KET_method:
                return "method"

        elif report_type == REPORT_TYPE_EXCEPTION:
            # exception param key
            if key == EXCEPTION_PARAM_KET_dataType:
                return "type"
            elif key == EXCEPTION_PARAM_KET_error:
                return "error"
            elif key == EXCEPTION_PARAM_KET_extra:
                return "extra"
            elif key == EXCEPTION_PARAM_KET_abnormalStack:
                return "stack"
            elif key == EXCEPTION_PARAM_KET_signal:
                return "signal_tag"
            elif key == EXCEPTION_PARAM_KET_signalName:
                return "signal_name"
            elif key == EXCEPTION_PARAM_KET_exceptionName:
                return "exception_name"
            elif key == EXCEPTION_PARAM_KET_exceptionReason:
                return "exception_reason"
            elif key == EXCEPTION_PARAM_KET_pagechain:
                return "page_chain"

        return ''

# if __name__ == '__main__':
#     analysis = DataAnalysis()
#     analysis.connect_database()
#
#     test_json = '{"d" : {},"b" : {"c" : "1aa"},"c" : {"p" : "120.0","c" : "1.0.0","q" : "","d" : "iOS","r" : "","e" : "13.4","f" : "x86_64","t" : "1588052296894","g" : "414.0*896.0","u" : "u","h" : "","v" : "v","i" : "","w" : "","j" : "1","k" : "1.0","l" : "无服务","m" : "","n" : "en-CN","a" : "a","o" : "o","b" : "AA687585-0849-4228-A805-A6A56BFCB751"},"a" : "0"}'
#
#     analysis.analysis_data(test_json.encode('utf8'))
