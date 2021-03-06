
from flask import *
from mim.models import *
from mim.ext import *
from flask.ext.restful import Resource

class CommentListAPI(Resource):
	''' Get all comments from a specific widget '''

	def get(self, widget_id):
		# May I replace by Widget.object.only("comments")
		widget = Widget.objects.get(id=widget_id)
		return SuccessResponse(toDict(widget.comments))

# 	''' Create a new comments '''
# 	def post(self, widget_id):
# 		try:
# 			comment = Comment.from_json(request.data)
# 			comment.save()
# 		except Exception, e:
# 			return ErrorResponse(e.message,600)
# 		else: 
# 			SuccessResponse({"id":comment.id})	
		

# class CommentAPI(Resource):
# 	''' Get a specific comments'''
# 	def get(self, widget_id, user_id):
# 		try:
# 			data = Comment.objects.get(pk=user_id)
# 		except Exception,e:
# 			return ErrorResponse(e.message, 600)
# 		else:
# 			return SuccessResponse(toDict(data))
	
# 	''' Update a specific users'''
# 	def put(self, user_id):
# 		try:
# 			postData = json.loads(request.data)
# 			user = User.objects.get(pk=user_id)
# 		except Exception, e:
# 			return ErrorResponse(e.message, 600)

# 		if "nickname" in postData:
# 			user.nickname = postData["nickname"]

# 		if "password" in postData:
# 			user.nickname = postData["password"]

# 		try:
# 			user.save()
# 		except Exception, e:
# 			return ErrorResponse(e.message, 700)

# 		else:
# 			return SuccessResponse({"id":str(user.pk)})
	
# 	''' Delete a specific users'''
# 	def delete(self, user_id):
# 		try:
# 			user = User.objects.get(pk=user_id)
# 			user.delete()
# 		except Exception, e:
# 			return ErrorResponse(e.message, 700)
# 		else:
# 			return SuccessResponse()


# def login():
# 	postData = json.loads(request.data)
# 	print postData

# 	if ("email" not in postData) or ("password" not in postData):
# 		return jsonify(ErrorResponse("Json request is not complete", 700))
# 	try:
# 		user = User.objects.get(email=postData["email"])
# 	except Exception, e:
# 		return jsonify(ErrorResponse(e.message, 700))

# 	else:
# 		if user.password == postData["password"]:
# 			session["current_user"] = str(user.pk)
# 			print session
# 			return jsonify(SuccessResponse())
	
# 	session["current_user"] = None;
# 	return jsonify(SuccessResponse())

# """ User logout
# """
# def logout():
# 	session["current_user"] = None;
# 	return jsonify(SuccessResponse())

# """ User me 
# """
# def me():
# 	if (session["current_user"] is None):
# 		return jsonify(ErrorResponse("you are not logged", 700))
# 	else:
# 		return jsonify(SuccessResponse(toDict(User.objects.get(pk=session["current_user"]))))
