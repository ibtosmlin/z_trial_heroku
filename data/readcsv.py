import datetime
import numpy as np
import os
import re
import pandas as pd


libpath = os.path.dirname(__file__)
csv_infos = os.path.join(libpath, 'data_infos.csv')
csv_update_date = os.path.join(libpath, 'data_infos_update_date.csv')
csv_companies = os.path.join(libpath, 'data_setup_companies.csv')
txt_new = os.path.join(libpath, 'new.txt')


def search_string_to_list(tgt: str)-> list:
    tgts = re.split('\s+', tgt)
    tgts = [tgt for tgt in tgts if len(tgts)!=0]
    return tgts

def short_name(comp_str: str) -> str:
    return comp_str.replace('株式会社', '').replace('相互会社', '').replace('生命保険', '生命')

class ContentsTable:
    def __init__(self) -> None:
        # 現時点での日時
        self.today = datetime.date.today().strftime('%Y-%m-%d')
        # 現時から起算した過去5年のリスト
        self.years = None
        # データの更新日時
        self.update_date = None
        # 会社名のリスト
        self.companies_ordered = None
        # 記事のdataFrame
        self.df_articles = None
        # method = "post"の場合のdataFrame
        self.cp_articles_selected = None
        # new-badgeの個数
        self.newcount = 0


        self._get_update_date()
        self._get_data()
        self._get_new()

        return


    def _get_update_date(self)->None:
        """:key
        更新日時の取得
        """
        with open(csv_update_date, encoding='utf-8-sig', newline='') as f:
            self.update_date = f.readline().replace('"', '').replace('\n', '')

    def _get_new(self)->None:
        """:key
        最新コメントの取得
        """
        with open(txt_new, encoding='utf-8-sig', newline='') as f:
            self.news = f.read().splitlines()
        self.news = [n for n in self.news if n]

    def _sort_data(self, df):
        dfc = df.copy()
        dfc["dumd"] = dfc.article_date
        x = dfc.article_date[dfc.is_new & (dfc.article_date != "----")]
        if len(x)>0:
            mx = max(x)
            mn = min(x)
            mn = datetime.datetime.strptime(mn, "%Y-%m-%d") - datetime.timedelta(days=1)
            mn = mn.strftime('%Y-%m-%d')
            dfc.loc[(dfc.article_date == "----") & dfc.is_new, "dumd"] = mx
            dfc.loc[(dfc.article_date == "----") & ~(dfc.is_new),"dumd"] = mn
        dfc.sort_values(["dumd", "company_order"], ascending=[False, True], inplace=True)
        return dfc.drop("dumd", axis=1)


    def _get_data(self):
        """
        会社名のリストをマージして、ソート
        """
        df_companies = pd.read_csv(csv_companies,encoding='utf-8-sig',usecols=['company_id', 'company_name'])
        self.companies_ordered = []
        for c in list(df_companies.company_name):
            self.companies_ordered.append((c, short_name(c)))

        df_companies.reset_index(inplace=True)
        df_companies.rename(columns={'index': 'company_order'}, inplace=True)
        df_companies.drop(columns='company_name', inplace=True)

        df_articles = pd.read_csv(csv_infos, encoding='utf-8-sig',
                        usecols=['company_id', 'company_name', 'company_url',
                                  'article_type', 'article_date', 'article_title', 'article_url', 'is_new'])
        df_articles = pd.merge(df_articles, df_companies, on='company_id')
        df_articles['company_name_s'] = df_articles.company_name.map(short_name)
        self.df_articles = self._sort_data(df_articles)
        self.newcount = np.count_nonzero(self.df_articles.is_new)


    def df_articles_selected(self, companies: list, ym: str, key_words: tuple):
        cp_articles = self.df_articles.copy()
        fg = np.array([True] * len(cp_articles))

        if companies and companies[0] != 'all':
            _f = lambda x: x in companies
            fg_companies = cp_articles.company_name.map(_f)
        else:
            fg_companies = fg.copy()

        if ym != "":   #  "yyyy-MM"
            fg_ym = np.array([False] * len(cp_articles))
            _g = lambda x: self.today[:7] if x[:4] == '----' else x[:7]
            article_year = cp_articles.article_date.map(_g)
            fg_ym |= article_year == ym
        else:
            fg_ym = fg.copy()

        key_words_inc = search_string_to_list(key_words[0])
        key_words_exc = search_string_to_list(key_words[1])
        if key_words_inc != [""]:
            regex = re.compile('|'.join(key_words_inc))
            _h = lambda x: False if len(regex.findall(x)) == 0 else True
            fg_key_words_inc = cp_articles.article_title.map(_h)
        else:
            fg_key_words_inc = fg.copy()

        if key_words_exc != [""]:
            regex = re.compile('|'.join(key_words_exc))
            _h = lambda x: False if len(regex.findall(x)) else True
            fg_key_words_exc = cp_articles.article_title.map(_h)
        else:
            fg_key_words_exc = fg.copy()

        self.cp_articles_selected = self._sort_data(cp_articles[fg_companies&fg_ym&fg_key_words_inc&fg_key_words_exc])
        return self.cp_articles_selected



if __name__ == '__main__':
    CT = ContentsTable()
#    print(CT.select_table(['日本生命保険相互会社'], '2021-03', ('人事異動', None)))
    print(CT.df_articles.info())
