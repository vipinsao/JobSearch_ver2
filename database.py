
from sqlalchemy import create_engine,text
import os

#created a secret key for the database 
db_connection_string = os.environ['DB_CONNECTION_STR']

engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      jobs = []
      for row in result.all():
          jobs.append(row._asdict())
      return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"),{"val":id})
        rows = result.all()
        if len(rows)==0:
            return None
        else:
            return rows[0]._asdict()


def add_application_to_db(job_id,data):
    with engine.connect() as conn:
        query = text('''INSERT INTO applications (job_id,full_name, email,linkedIn_url,Education,work_experience,resume_url) VALUES (:job_id, :full_name, :email, :linkedIn_url, :Education, :work_experience, :resume_url)''')
        conn.execute(query,{
                     'job_id' : job_id,
                     'full_name' : data['full_name'],
                     'email' : data['email'],
                     'linkedIn_url' : data['linkedIn_url'],
                     'Education' : data['Education'],
                 'work_experience' : data['work_experience'],
                    'resume_url' : data['resume_url']
                     })
        conn.commit()