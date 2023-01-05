from src.data.db_conn import getConnectionPool

def getFoodTrucksByApplicantName(applicant_name, record = 5):
    res = []
    try:
        querry = """SELECT locationid, applicant, facilityType, locationDescription, address, status, foodItems, ExpirationDate FROM facility ORDER BY SIMILARITY(applicant, %s) DESC LIMIT %s;"""
        postgreSQL_pool = getConnectionPool()
        ps_connection = postgreSQL_pool.getconn()
        
        if (ps_connection):
            ps_cursor = ps_connection.cursor()
            ps_cursor.execute(querry, (applicant_name, record,))
            record = ps_cursor.fetchall()
            desc = ps_cursor.description
            if record:
                for eachRow in record:
                    i = 0
                    mp = {}
                    for eachValue in desc:
                        mp[eachValue[0]] = eachRow[i]
                        i += 1
                    res.append(mp.copy())
            ps_cursor.close()
            postgreSQL_pool.putconn(ps_connection)
        return res
    except Exception as e:
        print("Something went wrong", e)
        return res

def getExpiredFoodTrucks(curr_date):
    res = []
    try:
        querry = """select * from facility where expirationdate < %s;"""
        postgreSQL_pool = getConnectionPool()
        ps_connection = postgreSQL_pool.getconn()
        
        if (ps_connection):
            ps_cursor = ps_connection.cursor()
            ps_cursor.execute(querry, (curr_date,))
            record = ps_cursor.fetchall()
            desc = ps_cursor.description
            if record:
                for eachRow in record:
                    i = 0
                    mp = {}
                    for eachValue in desc:
                        mp[eachValue[0]] = eachRow[i]
                        i += 1
                    res.append(mp.copy())
            ps_cursor.close()
            postgreSQL_pool.putconn(ps_connection)
        return res
    except Exception as e:
        print("Something went wrong", e)
        return res

def getFoodTrucksByStreet(street):
    res = []
    try:
        querry = """select locationid, applicant, locationdescription, address from facility where address_with_weights @@ to_tsquery(%s);"""
        postgreSQL_pool = getConnectionPool()
        ps_connection = postgreSQL_pool.getconn()
        
        if (ps_connection):
            ps_cursor = ps_connection.cursor()
            ps_cursor.execute(querry, (street,))
            record = ps_cursor.fetchall()
            desc = ps_cursor.description
            if record:
                for eachRow in record:
                    i = 0
                    mp = {}
                    for eachValue in desc:
                        mp[eachValue[0]] = eachRow[i]
                        i += 1
                    res.append(mp.copy())
            ps_cursor.close()
            postgreSQL_pool.putconn(ps_connection)
        return res
    except Exception as e:
        print("Something went wrong", e)
        return res


def getNearestFoodTrucks(latitude, longitude):
    res = []
    try:
        querry = """SELECT *, ST_Distance(location, ST_SetSRID(ST_MakePoint(%s, %s), 4326)) FROM facility ORDER BY location <-> ST_SetSRID(ST_MakePoint(%s, %s), 4326) limit 10;"""
        postgreSQL_pool = getConnectionPool()
        ps_connection = postgreSQL_pool.getconn()
        
        if (ps_connection):
            ps_cursor = ps_connection.cursor()
            ps_cursor.execute(querry, (latitude, longitude, latitude, longitude,))
            record = ps_cursor.fetchall()
            desc = ps_cursor.description
            if record:
                for eachRow in record:
                    i = 0
                    mp = {}
                    for eachValue in desc:
                        mp[eachValue[0]] = eachRow[i]
                        i += 1
                    res.append(mp.copy())
            ps_cursor.close()
            postgreSQL_pool.putconn(ps_connection)
        return res
    except Exception as e:
        print("Something went wrong", e)
        return res

def insertFoodTrucksEntity(m):
    try:
        querry =  sql = """INSERT INTO public.facility( locationid, applicant, facilitytype, cnn, locationdescription, address, blocklot, block, lot, permit, status, fooditems, x, y, latitude, longitude, schedule, dayshours, noisent, approved, received, priorpermit, expirationdate, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326));"""
        postgreSQL_pool = getConnectionPool()
        ps_connection = postgreSQL_pool.getconn()
        if (ps_connection):
            print("--")
            ps_cursor = ps_connection.cursor()
            ps_cursor.execute(querry, (m.get('objectid'), m.get('applicant'), m.get('facilitytype'), m.get('cnn'), m.get('locationdescription'), m.get('address'), m.get('blocklot'), m.get('block'),m.get('lot'),m.get('permit'), m.get('status'),m.get('fooditems'),m.get('x'), m.get('y'),m.get('latitude') ,m.get('longitude'),m.get('schedule'),m.get('dayshours'),m.get('noisent'),m.get('approved'), m.get('received'),m.get('priorpermit'),m.get('expirationdate'),m.get('latitude'), m.get('longitude'),))
            ps_connection.commit()
            ps_cursor.close()
            postgreSQL_pool.putconn(ps_connection)
        return [{"objectid": m["objectid"]}]
    except Exception as e:
        print("Something went wrong", e)
        return [{"objectid": ""}]

