import pandas as pd
import numpy as np
from mako.template import Template


def gen_report_html(temp_file, input_object, output_file):
    t = Template(filename=temp_file, input_encoding='utf-8', output_encoding='utf-8')
    genStr = t.render(py_object=input_object)
    with open(output_file, 'wb') as f:
        print('Writing %s' % output_file)
        f.write(genStr)


class MakoTest(object):
    def __init__(self):
        self.columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6', 'Column 7']
        self.data = pd.DataFrame(np.random.randint(1,100,size=(30,7)),columns= self.columns )
        print(self.data)

    def test_func(self):
        print("test_func")


if __name__ == '__main__':
    M = MakoTest()
    gen_report_html("index_mako.html", M, "index_mako_out.html")
