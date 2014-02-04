import pymongo
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, RequestContext
from bson.objectid import ObjectId
import pdb
import node
import patient
import logging

def index(request):
	context = RequestContext(request, {})
	return render(request, 'heart/index.html', context)

def reset(request):
	patient.reset("Bob")
	return do(request)
	
def do(request):
	activity_name = "Pick a Topic"
	message = ""
	requestGet = dict(request.GET.items())

	if "activity_name" in requestGet.keys():
		activity_name = requestGet["activity_name"]
	if "message" in requestGet.keys():
		logging.debug("Message is in the GET keys.")
		message = requestGet["message"]
	children = node.getChildren(activity_name)
	stats = node.getStats(activity_name)

	user = patient.getPatient("Bob")
	if stats:
		user = patient.applyActivity(username="Bob", activity_name=activity_name)
		message += " > Bob's overall is now %(overall)s, and bp is now %(bp)s." % user
	else:
		message += " > %s" % activity_name
	bp_dict = patient.bp_conversions[user['bp']]		
	context = RequestContext(request, {"children": children,
										"activity_name": activity_name,
										"overall": "%d" % user['overall'],
										"systolic" : "%d" % bp_dict['systolic'],
										"diastolic" : "%d" % bp_dict['diastolic'],
										"message": message })
	
	return render(request, 'heart/do.html', context)
