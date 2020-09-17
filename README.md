# TRGN Assignment 4
## About the App
This program, ensg2hugo.py, will take a csv file and print a dataframe in which the ENSEMBL gene name has been converted into a HUGO gene name. It takes a column number as an input and a csv file as an argument. The column number option should have a prefix of -f, so -f2 would be column 2. The column number is where the ENSEMBL gene names are located in your csv file, so that is where the replacement will occur.
## Installation and Usage
* Git clone can be used to install the app. Use `git clone https://github.com/aomidsalar/trgn_assignment4` into the terminal
* You will need a reference file, Homo\_sapiens.GRCh37.75.gtf, that will be used to create a dictionary matching the ENSEMBL names with the HUGO names.
    * In order to download the gtf file, you can use the command `curl http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz`. This will download the file in zipped form. In order to unzip a file, use the command `gunzip Homo_sapiens.GRCh37.75.gtf.gz`.
* The program `ensg2hugo.py` that you downloaded using git can then be run. Make sure the Homo\_sapiens.GRCh37.75.gtf file is in the same directory as the python program. The column number option should have a prefix of -f, and you will have the option of "-f[0-9]. If no column number is indicated, it will run the program on the first column of your csv file.
* If there are no matches, the ENSG gene name will not be replaced
## Dependencies
* git
* file input
* sys
* regular expressions
* pandas
* numpy
## Contact
aomidsal@usc.edu
   
