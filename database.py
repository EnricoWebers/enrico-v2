import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()   
    jobs = []
    for row in result.all():
      jobs.append(dict(zip(column_names,row)))
    return jobs
    '''
    print(result_dicts)
    '''


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id={id}")
      )
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])
      '''
      the following returns a list of 1 element:
      return [dict(row) for row in rows]
      '''
    
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

'''