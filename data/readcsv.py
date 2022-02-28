import csv
import datetime
from operator import itemgetter
import numpy as np
import os
import re
import pandas as pd


libpath = os.path.dirname(__file__)
csv_infos = os.path.join(libpath, 'data_infos.csv')
csv_update_date = os.path.join(libpath, 'data_infos_update_date.csv')
csv_companies = os.path.join(libpath, 'data_setup_companies.csv')


class ContentsTable:
    def __init__(self) -> None:
        # データの更新日時
        self.update_time = None
        # 会社名のリスト
        self.companies_ordered = None
        # 記事のdataFrame
        self.df_articles = None


        self._get_update_date()
        self._get_data()

        return


    def _get_update_date(self)->None:
        """:key
        更新日時の取得
        """
        with open(csv_update_date, encoding='utf-8-sig', newline='') as f:
            self.update_date = f.readline().replace('"', '')
        # print(self.update_date)


    def _get_data(self):
        """
        会社名のリスト
        """
        df_companies = pd.read_csv(csv_companies,encoding='utf-8-sig',usecols=['company_id', 'company_name'])
        self.companies_ordered = list(df_companies.company_name)
        df_companies.reset_index(inplace=True)
        df_companies.rename(columns={'index': 'company_order'}, inplace=True)
        df_companies.drop(columns='company_name', inplace=True)

        df_articles = pd.read_csv(csv_infos, encoding='utf-8-sig',
                        usecols=['company_id', 'company_name', 'company_url',
                                  'article_type', 'article_date', 'article_title', 'article_url'])
        df_articles = pd.merge(df_articles, df_companies, on='company_id')
        df_articles.sort_values(['company_order', 'article_date'], ascending=[True, False], inplace=True)
        self.df_articles = df_articles
        print(df_articles.article_date)


    def select_table(self, comps, days, d_today, key_words):
        cp_articles = self.df_articles.copy()
        _f = lambda x: x in comps
        fg_f = cp_articles.company_name.map(_f)


        if key_words:
            regex = re.compile('|'.join(key_words))
            _h = lambda x: len(regex.findall(x)) > 0
            fg_h = cp_articles.company_name.map(_h)
        else:
            fg_h = np.array([True] * len(cp_articles))


if __name__ == '__main__':
    CT = ContentsTable()
#    print(CT.select_table(['日本生命'], 1, ['保険金', '金庫']))
