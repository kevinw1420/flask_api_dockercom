from flask import jsonify, request,make_response,session
from flask_restful import Resource, Api
from employee_service import app ,db
from . import models  
from .models import Employee, Admin


api = Api(app)

PositionSchema=models.PositonSchema()
EmployeesSchema=models.EmployeeSchema(many=True)
EmployeeSchema=models.EmployeeSchema()

def check_auth(session,token):
    
    return session.get(token,None)

class EmployeeResource_NeedID(Resource):
   
    def get(self,user_id): 
        # check auth
        if (imput_auth:=request.headers.get('Authorization',None))==None:
            return  make_response(jsonify({'err': -1, 'err_msg': 'Auth Fail'}), 404)
        else:
            
            if check_auth(session,imput_auth.split(" ")[1])==None:
                return  make_response(jsonify({'err': -1, 'err_msg': 'Auth Fail'}), 404)
    
        if user_id=="all":
            query_result = Employee.query.all()
            query_result = EmployeesSchema.dump(query_result)
            return jsonify({'err': 0, 'rows':query_result })
        elif user_id.isdigit():
            query_result = Employee.query.get(user_id) 
            query_result = EmployeeSchema.dump(query_result)
            return jsonify({'err': 0, 'rows': query_result})
        else:
            return make_response(jsonify({'err': -1, 'err_msg': 'Id type error'}), 422)

    def put(self,user_id):
        # check auth
        if (imput_auth:=request.headers.get('Authorization',None))==None:
            return  make_response(jsonify({'err': -1, 'err_msg': 'Auth Fail'}), 404)
        else:
            
            if check_auth(session,imput_auth.split(" ")[1])==None:
                return  make_response(jsonify({'err': -1, 'err_msg': 'Auth Fail'}), 404)

        RequestPost = request.get_json(force=True)
        if not RequestPost:
            return make_response(jsonify({'err': -1, 'err_msg': 'No input data provided'}), 400)
        #get user
        queryid=Employee.query.filter_by(id=user_id).all()
        if len(queryid)==0:
            return make_response(jsonify({'err': -1, 'err_msg': 'Employee Not Found'}), 422)
        # check data struct
        try :
            queryid[0].email=RequestPost['email'], 
            queryid[0].mobile=RequestPost['mobile'],
            queryid[0].title=RequestPost['position']['title'],
            queryid[0].department=RequestPost['position']['department']
        except:
            return make_response(jsonify({'err': -1, 'err_msg': 'Data Struct Error'}), 422)

        # Validate 
        if len(RequestPost['mobile'])!=10:
            return make_response(jsonify({'err': -1, 'err_msg': 'Mobile type error'}), 422)
        queryMail=Employee.query.filter_by(email=RequestPost['email']).count()
        queryMobile=Employee.query.filter_by(mobile=RequestPost['mobile']).count()
        if queryMail > 0 :   
            return make_response(jsonify({'err': -1, 'err_msg': 'Mail exist'}), 422)
        elif queryMobile > 0 :
            return make_response(jsonify({'err': -1, 'err_msg': 'Mobile exist'}), 422)
        # db commit
        db.session.commit()
        return jsonify({'err': 0, 'err_msg': f'id = {queryid[0].id}'})
    
    def delete(self,user_id):
        # check auth
        if (imput_auth:=request.headers.get('Authorization',None))==None:
            return  make_response(jsonify({'err': -1, 'err_msg': 'Auth Fail'}), 404)
        else:
            
            if check_auth(session,imput_auth.split(" ")[1])==None:
                return  make_response(jsonify({'err': -1, 'err_msg': 'Auth Fail'}), 404)

        #get user
        queryid=Employee.query.filter_by(id=user_id).all()
        if len(queryid)==0:
            return make_response(jsonify({'err': -1, 'err_msg': 'Employee Not Found'}), 422)
        # check data struct
        
        db.session.delete(queryid[0])
        db.session.commit()

        return jsonify({'err': 0, 'err_msg': f'id = {queryid[0].id}'})


class EmployeeResource(Resource):
    

    def post(self,user_id=None):
        # check auth
        if (imput_auth:=request.headers.get('Authorization',None))==None:
            return  make_response(jsonify({'err': -1, 'err_msg': 'Auth Fail'}), 404)
        else:
            
            if check_auth(session,imput_auth.split(" ")[1])==None:
                return  make_response(jsonify({'err': -1, 'err_msg': 'Auth Fail'}), 404)
                
        RequestPost = request.get_json(force=True)
        if not RequestPost:
            return make_response(jsonify({'err': -1, 'err_msg': 'No input data provided'}), 400)
        # check data struct
        try :
            NewEmployee = Employee(
                                    email=RequestPost['email'], 
                                    mobile=RequestPost['mobile'],
                                    title=RequestPost['position']['title'],
                                    department=RequestPost['position']['department']
                                    )
        except:
            return make_response(jsonify({'err': -1, 'err_msg': 'Data Struct Error'}), 422)
        
                

        # Validate 
        if len(RequestPost['mobile'])!=10:
            return make_response(jsonify({'err': -1, 'err_msg': 'Mobile type error'}), 422)
        
        queryMail=Employee.query.filter_by(email=RequestPost['email']).count()
        queryMobile=Employee.query.filter_by(mobile=RequestPost['mobile']).count()
        
        if queryMail > 0 :   
            return make_response(jsonify({'err': -1, 'err_msg': 'Mail exist'}), 422)
        elif queryMobile > 0 :
            return make_response(jsonify({'err': -1, 'err_msg': 'Mobile exist'}), 422)
        
        # db commit
        db.session.add(NewEmployee)
        db.session.commit()

        return jsonify({'err': 0, 'err_msg': f'id = {NewEmployee.id}'})


api.add_resource(EmployeeResource_NeedID, '/employee/<string:user_id>')
api.add_resource(EmployeeResource,'/employee')





AdminSchema=models.AdminSchema()


class AdminResource_Create(Resource):
    def post(self):
        RequestPost = request.get_json(force=True)
        if not RequestPost:
            return make_response(jsonify({'err': -1, 'err_msg': 'No input data provided'}), 400)
        queryAdmin=Admin.query.filter_by(username=RequestPost['username']).count()
        
        if queryAdmin > 0 :   
            return make_response(jsonify({'err': -1, 'err_msg': 'Admin exist'}), 422)
    
        # check data struct
        try :
            NewAdmin = Admin(
                                username=RequestPost['username'], 
                                key=RequestPost['key'],

                                )
        except:
            return make_response(jsonify({'err': -1, 'err_msg': 'Data Struct Error'}), 422)
        # db commit
        db.session.add(NewAdmin)
        db.session.commit()

        return jsonify({'err': 0, 'err_msg': f'id = {NewAdmin.id}'})

    

class AdminResource(Resource):
    
    def post(self):
        RequestPost = request.get_json(force=True)
        if not RequestPost:
            return make_response(jsonify({'err': -1, 'err_msg': 'No input data provided'}), 400)
        # check data struct
        if "username" in RequestPost and "key" in RequestPost:
            pass
        else: 
            return make_response(jsonify({'err': -1, 'err_msg': 'Data Struct Error'}), 422)
        
        
        queryAdmin=Admin.query.filter_by(username=RequestPost['username']).count()
        
        if queryAdmin == 0 :   
            return make_response(jsonify({'err': -1, 'err_msg': 'Admin not found'}), 422)            

        # session cookie set
        import datetime
        
        loginUser=session.get('loginUser',None)
        if loginUser==None:
            
            token= RequestPost["username"]+str(datetime.datetime.now())
            token=token.replace(" ","")
            session[token]=RequestPost['username']
            session['loginUser']={RequestPost['username']:token}
            
        else:
            if RequestPost['username'] in session['loginUser']:
                old_token=session['loginUser'][RequestPost['username']]
                del session[old_token]
                del session['loginUser'][RequestPost['username']]
            
            token= RequestPost["username"]+str(datetime.datetime.now())
            token=token.replace(" ","")
            session[token]=RequestPost['username']
            session['loginUser'][RequestPost['username']]=token

        
        
        session.permanent = True
        app.permanent_session_lifetime = datetime.timedelta(seconds=60*30)
        session.modified = True
        

        return make_response(jsonify({'err': 0, 'acess_token': f'token {token}'}),200)


api.add_resource(AdminResource_Create, '/create_admin')
api.add_resource(AdminResource, '/auth')



