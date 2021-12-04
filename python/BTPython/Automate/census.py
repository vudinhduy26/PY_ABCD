import openpyxl
import pprint

def main():
    wb = openpyxl.load_workbook('censuspopdata.xlsx')
    #chon bang tinh
    sheet = wb['Population by Census Tract']

    countyData = {}

    #----
    for row in range(2,sheet.max_row+1):
        state = sheet['B'+str(row)].value
        county = sheet['C'+str(row)].value
        pop = sheet['D'+str(row)].value

        # Make sure the key for this state exists.
        countyData.setdefault(state,{})
        # Make sure the key for this county in this state exists.
        countyData[state].setdefault(county,{'tracts': 0, 'pop': 0})
        ## Mỗi hàng đại diện cho một đường điều tra dân số, vì vậy hãy tăng lên một.
        countyData[state][county]['tracts'] += 1
        # Tăng dân số quận bằng cách tăng dân số trong đường điều tra dân số này.
        countyData[state][county]['pop'] += int(pop)

    print("Writing result ....")
    resultFile = open('census2020.py','w')
    resultFile.write('allData = ' + pprint.pformat(countyData))
    resultFile.close()
    print("Done")
    

    
if __name__ == '__main__':
    main()