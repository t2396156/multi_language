


class Model() :

    def __init__(self) :
        self.wd_idf = {}

    def load(self, mflie) :
        wd_idf = {}
        for line in open(mflie):
            l_data = line.split('\t')
            wd = l_data[0].strip()
            if not wd or len(wd) < 2:
                continue
            try:
                self.wd_idf[wd.decode('utf-8')] = float(l_data[1])
            except:
                print wd, l_data[1]


    def process(self, content) :
        pass