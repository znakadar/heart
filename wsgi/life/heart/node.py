import pymongo

def getNode(node_name):
	pass
	
def getChildren(node_name):
	# 1. Connect to the db
	# 2. Use the node name to find the node
	# 3. Use the "children" part of the node to get the children
	# 4. Return the children (in some format).
	db = getDb()
	activities = db.activities.find({"name":node_name})
	children = None
	if activities.count() == 1:
		activity = activities[0]
		children = activity["children"] if "children" in activity.keys() else None
	return children

def getStats(node_name):
	db = getDb()
	activities = db.activities.find({"name":node_name})
	stats = None
	if activities.count() == 1:
		activity = activities[0]
		stats = activity["stats"] if "stats" in activity.keys() else None
	return stats


def getDb():
	client=pymongo.MongoClient("localhost",27017)
	return client.heart
	

