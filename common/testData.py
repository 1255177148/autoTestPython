import pandas
import logging

def read_excel(file, **kwargs):
    data_dict = []
    logger = logging.getLogger('main.testData')
    try:
        data = pandas.read_excel(file, **kwargs)
        data_dict = data.to_dict('records')
    except Exception as e:
        logger.error('读取数据报错--->', e)
    finally:
        return data_dict


if __name__ == '__main__':
    print(read_excel("D://testData.xlsx"))