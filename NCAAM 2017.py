from bs4 import BeautifulSoup
import requests
import csv
from os.path import expanduser
home = expanduser("~")

os.mkdir('{home}/Downloads/NCAAM 2017'.format(home=home))


def gather_schools()
	schools_page = BeautifulSoup(requests.get('http://www.sports-reference.com/cbb/seasons/2017-school-stats.html').text, 'html')
	primary_schoolist = schools_page('td', {'data-stat': 'school_name'})
	schoolist = []
	for school in primary_schoolist:
	    schoolist.append(str(school).split('/schools/')[1].split('/2017')[0])
	return schoolist()

def gather_team_data(soup):
    final_rows = []
    for row in soup('table')[0].tbody.findAll('tr'):
        tds = row.find_all('td')
        row_write = [elem.text.strip().encode('utf-8') for elem in tds]
        if len(row_write) > 1:
            final_rows.append(row_write)
        else:
            pass
    return final_rows

def fetch_page(school):
    return BeautifulSoup(requests.get(
        'http://www.sports-reference.com/cbb/schools/{school}/2017-gamelogs.html'.format(school=school)).text,
                         'html')

def main():
	schoolist = gather_schools()
    for school in schoolist:
        print(school)
        CompleteName = "{home}/Downloads/NCAAM 2017/{school}.csv".format(home=home, school=school)
        with open(CompleteName, 'w') as f:
            f.write("Date" + "," + " " + "," + "Opp" + "," + "W/L" + "," + "Tm" + "," + "Opp" 
                    + "," + "FG" + "," + "FGA" + "," + "FG%" + "," + "3P" + "," 
                    + "3PA" + "," + "3P%" + "," + "FT" + "," + "FTA" + "," + "FT%" 
                    + "," + "ORB" + "," + "TRB" + "," + "AST" + "," + "STL" + "," 
                    + "BLK" + "," + "TOV" + "," + "PF" + "," + "" + "," + "FG" + "," + "FGA" + "," 
                    + "FG%" + "," + "3P" + "," + "3PA" + "," + "3P%" + "," + "FT" + "," 
                    + "FTA" + "," + "FT%" + "," + "ORB" + "," + "TRB" + "," + "AST" + "," 
                    + "STL" + "," + "BLK" + "," + "TOV" + "," + "PF" + "," + "\n")
            writer = csv.writer(f)
            try:
                to_csv = gather_team_data(fetch_page(school))
            except IndexError:
                continue
            for row in to_csv:
                row_final = [unit.decode('utf-8') for unit in row]
                writer.writerow(row_final)

main()