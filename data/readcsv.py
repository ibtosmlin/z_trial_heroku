import datetime
import numpy as np
import os
import re
import pandas as pd


libpath = os.path.dirname(__file__)
csv_infos = os.path.join(libpath, 'data_infos.csv')
csv_update_date = os.path.join(libpath, 'data_infos_update_date.csv')
csv_companies = os.path.join(libpath, 'data_setup_companies.csv')


def search_string_to_list(tgt: str)-> list:
    tgts = re.split('\s+', tgt)
    tgts = [tgt for tgt in tgts if len(tgt)!=0]
    return tgts


class ContentsTable:
    def __init__(self) -> None:
        # 現時点での日時
        self.today = None
        # 現時から起算した過去5年のリスト
        self.years = None
        # データの更新日時
        self.update_date = None
        # 会社名のリスト
        self.companies_ordered = None
        # 記事のdataFrame
        self.df_articles = None
        # method = "get"の場合のdataFrame
        self.df_articles_init = None


        self._get_years_list()
        self._get_update_date()
        self._get_data()
        self._get_initial_table()

        return


    def _get_years_list(self)->None:
        # 現時点での日時
        self.today = str(datetime.date.today())
        year = int(self.today[:4])
        self.years = []
        for i in range(4):
            self.years.append("="+str(year - i))
        self.years.append("<"+str(year - i))


    def _get_update_date(self)->None:
        """:key
        更新日時の取得
        """
        with open(csv_update_date, encoding='utf-8-sig', newline='') as f:
            self.update_date = f.readline().replace('"', '').replace('\n', '')
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


    def df_articles_selected(self, companies: list, years: list, key_words: list):
        key_words_list = search_string_to_list(key_words)
        cp_articles = self.df_articles.copy()
        fg = np.array([True] * len(cp_articles))

        if companies:
            _f = lambda x: x in companies
            fg_companies = cp_articles.company_name.map(_f)
        else:
            fg_companies = fg.copy()

        if years:   #  "=yyyy" or "<yyyy"
            fg_years = np.array([False] * len(cp_articles))
            _g = lambda x: self.today[:4] if x[:4] == '----' else x[:4]
            article_year = cp_articles.article_date.map(_g)
            for year in years:
                if year[0] == '=':
                    fg_years |= article_year == year[1:]
                else:
                    fg_years |= article_year < year[1:]
        else:
            fg_years = fg.copy()

        if key_words_list:
            regex = re.compile('|'.join(key_words_list))
            _h = lambda x: False if len(regex.findall(x)) == 0 else True
            fg_key_words = cp_articles.article_title.map(_h)
        else:
            fg_key_words = fg.copy()

        return cp_articles[fg_companies&fg_years&fg_key_words]


    def _get_initial_table(self):
        """
        10日以内のデータを出力する
        "----"のデータは非表示
        """
        inner = 10
        cp_articles = self.df_articles.copy()

        # 現時点での日時
        kijun = datetime.datetime.strptime(self.update_date + ':00', '%Y-%m-%d %H:%M:%S')

        def _f(x):
            if x == '----':
                # x = kijun
                return False
            else:
                x = datetime.datetime.strptime(x, '%Y-%m-%d')
#            return (kijun - x).days <= inner
            return True

        fg = cp_articles.article_date.map(_f)
        self.df_articles_init = cp_articles[fg]



if __name__ == '__main__':
    CT = ContentsTable()
#    print(CT.select_table(['日本生命保険相互会社'], ['=2021', "=2019"], '人事異動'))
#    print(CT.select_table(['朝日生命保険相互会社'], ['=2022', "<2019"], '').article_date)
#    print(CT.select_table(['朝日生命保険相互会社'], ["<2019"], '').article_date)
    print(CT.df_articles_init.article_date.info())
