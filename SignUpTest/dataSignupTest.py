from xlrd import open_workbook

class readDatatest:
    def dataTestSignUp(self):
        data_test = open_workbook('../GFG/SignUpTest/dataset.xlsx')
        values = []
        for s in data_test.sheets():
            for r in range(1, s.nrows):
                c_names = s.row(0)
                c_value = []
                for name, c in zip(c_names, range(s.ncols)):
                    value = (s.cell(r, c).value)
                    try:
                        value = str(int(value))
                    except:
                        pass
                    c_value.append(value)
                values.append(c_value)
        return values

