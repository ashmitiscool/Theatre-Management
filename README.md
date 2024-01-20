# Theatre-Management
For school project (Python &amp; SQL)

#-----
First of all: change the conncection password in the entire code to your sql password

Second: The tables are stored in the data folder, you just import them, provided you have a database named cinemax..also, drop all tables you had before..just make a new one lol
_> Export tables(no need this, just put this as info>
SELECT *
INTO OUTFILE '/path/to/output_file.sql'
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
FROM your_table;

_> Import tables(this is waht you need):
LOAD DATA INFILE '/path/to/input_file.sql'
INTO TABLE your_table
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

you get the gist..if it doesnt work, ask chatgpt...it will first give mysqldump, but ask it for another method
