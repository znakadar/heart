import pymongo

bp_conversions = {	-5 : {"systolic": 70, "diastolic": 40}, 
					-4 : {"systolic": 77, "diastolic": 48},
					-3 : {"systolic": 85, "diastolic": 55},
					-2 : {"systolic": 92, "diastolic": 61},
					-1 : {"systolic": 100, "diastolic": 66},
					0 : {"systolic": 110, "diastolic": 70},
					1 : {"systolic": 115, "diastolic": 75},
					2 : {"systolic": 124, "diastolic": 82},
					3 : {"systolic": 135, "diastolic": 88},
					4 : {"systolic": 147, "diastolic": 93},
					5 : {"systolic": 160, "diastolic": 100},
				}

def reset(username):
	db = getDb()
	db.patients.update({"name":username}, {"$set": {"overall":75, "bp":0}})

def getPatient(username):
	db = getDb()
	users = db.patients.find({"name":username})
	user = None
	if users.count() == 1:
		user = users[0]
	return user


def applyActivity(username, activity_name):
	"""
	1. Retrive the user.
	2. Retrieve the activity.
	3. Apply the stats from the activity to the attributes of the user.
	4. Save the user.
	"""
	user = getPatient(username)
	
	db = getDb()
	activities = db.activities.find({"name":activity_name})
	activity = None
	if activities.count() == 1:
		activity = activities[0]
	
	if user and activity:
		overall_change = activity['stats']['overall']
		bp_change = activity['stats']['bp']
		new_overall = user['overall'] + overall_change
		if new_overall > 100:
			new_overall = 100
		if new_overall < 0:
			new_overall = 0
			
		old_bp = user['bp']
		new_bp = old_bp + bp_change
		activity_is_good = overall_change > 0
		if activity_is_good:
			# A good activity will never get you out of the 
			# good range of blood pressure
			if new_bp < -3:
				new_bp = -3
			if new_bp > 3:
				new_bp = 3
		else:
			if new_bp < -5:
				new_bp = -5
			if new_bp > 5:
				new_bp = 5
		db.patients.update({"name":username}, {"$set" : {"overall":new_overall, "bp":new_bp}}, False)
		user = getPatient(username)
	return user
	
def getDb():
	client=pymongo.MongoClient("localhost",27017)
	return client.heart