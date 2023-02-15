# test2task
Test task to a new job to define skills. This app parced data form weather site and before recording data to the db creates this db. Or if the DB was created before this app updated the old data.

## Installation

It`s a test work without installation. Only some scripts in here such as : beautifulsoup4, pandas, sqllite3, mysql.connect, apschedular, python 3.9.0, requests.

```bash
pip install beautifulsoup4
pip install pandas
pip install sqllite3
pip install mysql.connect
pip install apschedular
pip install requests

```

## Usage

```python
import parsing.py

parsing.getDataFromSiteNow() # returns dictionary with weather data
parsing.getDataFromSite() # returns list with in a 5 days`s  weather data
parsing.main() # returns list with all the data

import datadb.py (if use sqllite3)

datadb.insertData() # returns None


import start.py

start.timeNow() # returns None
start.main() # returns None


import create.py(if use mysql)

create.createTable() # returns None


import rows.py(if use mysql)

rows.createRows() # returns None
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
