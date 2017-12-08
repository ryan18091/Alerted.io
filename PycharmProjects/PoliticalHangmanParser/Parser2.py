import urllib.parse
import urllib.request
import bs4 as bs
import sqlite3



conn = sqlite3.connect('PoliticianCompare.db')
c = conn.cursor()
c.execute('SELECT * From Politician_Data')
old_data = [row for row in c.fetchall()]


class Politician_Parser:

    def __init__(self, url, query_tag, query_id):
        self.url = url
        self.query_tag = query_tag
        self.query_id = query_id

    def Politician(self):

        try:
            sauce = urllib.request.urlopen(self.url)
            soup = bs.BeautifulSoup(sauce, 'lxml')
            Pol_list = []
            for div in soup.find_all(self.query_tag, class_ = self.query_id):
                table = str.maketrans(dict.fromkeys('\t\n'))
                Pol_list.append(div.text.translate(table))
            return Pol_list

        except Exception as e:
            print(e)

#Instance Variables
president = Politician_Parser('https://www.whitehouse.gov/', 'span', 'whr-president')
cabinet = Politician_Parser('https://www.whitehouse.gov/administration/cabinet', 'div', 'field-item even')
senate_house = Politician_Parser('https://ballotpedia.org/List_of_current_members_of_the_U.S._Congress', 'td', None)

presData = Politician_Parser.Politician(president)
cabData = Politician_Parser.Politician(cabinet)
senHouseData = Politician_Parser.Politician(senate_house)
data = (presData + cabData + senHouseData)


conn = sqlite3.connect('PoliticianCompare.db')
c = conn.cursor()

def create_tables():
    c.execute('CREATE TABLE IF NOT EXISTS Politician_Data(politician String)')

create_tables()


class DataInput_and_Checker:

    def __init__(self, presData, cabData, senHouseData, old_data):
        self.presData = presData
        self.cabData = cabData
        self.senHouseData = senHouseData
        self.old_data = old_data



    def inputData(self):
        data = self.presData + self.cabData + self.senHouseData
        print(len(old_data))
        if len(old_data) == 0:
            print('Inputting Data')
            for p in data:
                c.execute('Insert INTO Politician_Data VALUES(?)', (p,))
                conn.commit()


    def dataCompare(self):
        old_data = [i for i in c.fetchall()]
        new_data = self.presData + self.cabData + self.senHouseData
        if old_data != new_data:
            return False


    def dataDiff(self):
        old_data = (i for i in c.fetchall())
        new_data = (self.presData + self.cabData + self.senHouseData)
        #Sets require their items to be hashable
        diff_data = (set(old_data)) - set(new_data)
        return diff_data


DbInput = DataInput_and_Checker(presData,cabData,senHouseData, old_data)
if not DbInput.inputData():
    DbInput.dataDiff()