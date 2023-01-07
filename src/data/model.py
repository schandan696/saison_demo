from src.data.db_conn import getConnectionPool



postgreSQL_pool = getConnectionPool()

def __createResponse(record, desc, res):
    if record:
        for eachRow in record:
            i = 0
            mp = {}
            for eachValue in desc:
                mp[eachValue[0]] = eachRow[i]
                i += 1
            res.append(mp.copy())

def __execute_querry(res, querry, params):
    ps_connection = postgreSQL_pool.getconn()
    if (ps_connection):
        ps_cursor = ps_connection.cursor()
        ps_cursor.execute(querry, params)
        record = ps_cursor.fetchall()
        desc = ps_cursor.description
        __createResponse(record, desc, res)
        ps_cursor.close()
        postgreSQL_pool.putconn(ps_connection)

def getFoodTrucksByApplicantName(applicant_name, record = 5):
    res = []
    try:
        querry = """SELECT locationid, applicant, facilityType, locationDescription, address, status, foodItems, ExpirationDate FROM facility ORDER BY SIMILARITY(applicant, %s) DESC LIMIT %s;"""
        __execute_querry(res, querry, (applicant_name, record,))
        return res
    except Exception as e:
        print("Something went wrong", e)
        return res

def getExpiredFoodTrucks(curr_date):
    res = []
    try:
        querry = """select * from facility where expirationdate < %s;"""
        __execute_querry(res, querry, (curr_date,))
        return res
    except Exception as e:
        print("Something went wrong", e)
        return res

def getFoodTrucksByStreet(street):
    res = []
    try:
        querry = """select locationid, applicant, locationdescription, address from facility where address_with_weights @@ to_tsquery(%s);"""
        __execute_querry(res, querry, (street,))
        return res
    except Exception as e:
        print("Something went wrong", e)
        return res


def getNearestFoodTrucks(latitude, longitude):
    res = []
    try:
        querry = """SELECT *, ST_Distance(location, ST_SetSRID(ST_MakePoint(%s, %s), 4326)) FROM facility ORDER BY location <-> ST_SetSRID(ST_MakePoint(%s, %s), 4326) limit 10;"""
        __execute_querry(res, querry, (latitude, longitude, latitude, longitude,))
        return res
    except Exception as e:
        print("Something went wrong", e)
        return res

def insertFoodTrucksEntity(m):
    try:
        querry =  sql = """INSERT INTO public.facility( locationid, applicant, facilitytype, cnn, locationdescription, address, blocklot, block, lot, permit, status, fooditems, x, y, latitude, longitude, schedule, dayshours, noisent, approved, received, priorpermit, expirationdate, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326));"""
        __execute_querry(res, querry, (m.get('objectid'), m.get('applicant'), m.get('facilitytype'), m.get('cnn'), m.get('locationdescription'), m.get('address'), m.get('blocklot'), m.get('block'),m.get('lot'),m.get('permit'), m.get('status'),m.get('fooditems'),m.get('x'), m.get('y'),m.get('latitude') ,m.get('longitude'),m.get('schedule'),m.get('dayshours'),m.get('noisent'),m.get('approved'), m.get('received'),m.get('priorpermit'),m.get('expirationdate'),m.get('latitude'), m.get('longitude'),))
        return [{"objectid": m["objectid"]}]
    except Exception as e:
        print("Something went wrong", e)
        return [{"objectid": ""}]

