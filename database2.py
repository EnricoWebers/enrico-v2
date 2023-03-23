from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://g49jjg744emluyy3ilul:pscale_pw_MMlzHAqK0tFiVDcfAxBNlQcaYB6k8VVVApkp0NftflK@eu-central.connect.psdb.cloud/enricocareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  column_names = result.keys()   
  result_dicts = []
  for row in result.all():
    result_dicts.append(dict(zip(column_names,row)))

  print(result_dicts)


'''
print("type(result): ",type(result))
result_all = result.all()
print("type(result_all): ", type(result_all))
print("result_all: ",result_all)
first_result = result_all[0]
column_names = result.keys() 
first_result_dict = dict(zip(column_names, first_result))
print("type(first_result_dict): ",type(first_result_dict))
print(first_result_dict)
'''

'''
LEGACY CODE
print("first_result: ", first_result)
print("type(first_result): ", type(first_result))
first_result_dict = dict(result_all[0].__dict__)
print("type(first_result_dict): ",type(first_result_dict))
print(first_result_dict)
'''

'''
https://stackoverflow.com/questions/1958219/how-to-convert-sqlalchemy-row-object-to-a-python-dict
'''
 
'''
THIS VERSION WORKS according to the YouTube video https://www.youtube.com/watch?v=yBDHkveJUf4&t=10984s
'''
