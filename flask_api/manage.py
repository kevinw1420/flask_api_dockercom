import employee_service


employee_service_app=employee_service.app
employee_service_db=employee_service.db



if __name__ == '__main__':
    employee_service_app.run(debug=True,port=8000)
    
    