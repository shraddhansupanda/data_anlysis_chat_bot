->Run the import_data.py to insert the data in to the mysql data base.
  (while runing the import_data.py pass the paramiter 1-username
                                                      2-password
                                                      3-ip(localhost if you are on your own computer)
                                                      4-port number
                                                      5-schema on which you want to store the data
  (with this five parameter run this python file)
      
      EX-python import_data.py root(username) 12345(password) localhost(ip) 3306(port number) data(schema name) 



->Then run chat_bot.py to run the chat_bot.py.
 (while runing the import_data.py pass the paramiter 1-username
                                                     2-password
                                                     3-ip(localhost if you are on your own computer)
                                                     4-port number
                                                     5-schema on which your data set is present
   (with this five parameter run this python file)
      
      EX-python chat_bot.py root(username) 12345(password) localhost(ip) 3306(port number) data(schema name)
      
 ->Then ask any type of question related to the life_expectancy data.
      (This data consist of life expectancy of every country form 1800 to 2016)
      QUESTION YOU CAN ASK
      ->predict what will be the life expectancy of country_name(ex-india, china) on a pirticular year
      ->name all the country
      ->

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
  
