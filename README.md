->Run the import_data.py to insert the data in to the mysql data base.
  (while runing the import_data.py pass the paramiter 1-username
                                                      2-password
                                                      3-ip(localhost if you are on your own computer)
                                                      4-port number
                                                      5-schema on which you want to store the data
  (with this five parameter run this python file)
      
      EX-python import_data.py root(username) 12345(password) localhost(ip) 3306(port number) data(schema name) 



->Then run chat_bot.py for mac user and chat_bot(windows).py for window user to run the application.
 (while runing the import_data.py pass the paramiter 1-username
                                                     2-password
                                                     3-ip(localhost if you are on your own computer)
                                                     4-port number
                                                     5-schema on which your data set is present
   (with this five parameter run this python file)
      
      EX-python chat_bot.py root(username) 12345(password) localhost(ip) 3306(port number) data(schema name)
      
 ->Then ask any type of question related to the life_expectancy data.
      (This data consist of life expectancy of every country form 1800 to 2016)
      
 ->QUESTION YOU CAN ASK
 
      ->predict what will be the life expectancy of country_name(ex-india, china) on a pirticular year
      
      ->name all the country
      
      ->do a scatter of nepal and china from 1870 to 1956
      ->do a GRAPHICAL exploritory data analysis on Brazil from 1800 to 2016
      ->what is the life expectancy of bhutan and russia on 1890
      ->Do a statistical exploritory data analysis on egypt and Afghanistan from 1890 to 1990
      ->what is the varience and std of china and uganda from 1900 to 2015
      ->which country has highest life expectancy on 2000
      ->which country has lowest le on 1800
      etc etc...
 ( BY USING MY BOT YOU WILL GET THE MOST OUT OF THE DATA SET)
 (I HAVE MAKE MY BOT QUITE FLEXIBE TO UNDERSTAND WHAT THE USER IS TRYING TO ASK AND REPLAY ACCORDING TO IT)
Requirment:

    python

    mysql
  
    mysql workbench
  
    python mysql connector

Requirment:(python module)
  
    1-pandas
  
    2-numpy
  
    3-requests
  
    4-matplotlib
  
    5-sqlalchemy
  
    6-sklearn
  
