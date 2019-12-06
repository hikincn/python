from dbutils import DB
if __name__ == '__main__':
    db = DB()
    db.execute("insert into SGBA_ODS_WB_GDZCTZ(gdzctz_id) values(2)")
    db.commit()
    db.close()
