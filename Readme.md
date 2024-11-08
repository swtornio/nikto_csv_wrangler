# nikto csv wrangler

For when you have a big pile of nikto csv files and just want to peruse or manipulate them in a nice Excel window.

## Set up a virtual environment and install requirements

```
danny@Dannys-MacBook-Pro nikto_csv_wrangler % python3 -m venv .env
danny@Dannys-MacBook-Pro nikto_csv_wrangler % source .env/bin/activate
(.env) danny@Dannys-MacBook-Pro nikto_csv_wrangler % pip install --upgrade pip
(.env) danny@Dannys-MacBook-Pro nikto_csv_wrangler % pip install -r requirements.txt 

```

## Sample Output
```
└─$ python ./nikto_csv_wrangler.py -h

usage: nikto_csv_wrangler.py [-h] input_dir output_file

Combine multiple CSV files from a directory into a single output file.

positional arguments:
  input_dir    Directory containing the CSV files to combine
  output_file  Path for the combined output CSV file

options:
  -h, --help   show this help message and exit
```

Credits: [Chris Sullo](https://github.com/sullo) for actually writing [nikto](https://github.com/sullo/nikto) and keeping its zombie language undead in the modern era.