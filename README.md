# flask_api_dockercom
1. docker-compose up -d at docker-compose.yaml file path
2. POST /{{your_host}}/create_admin create admin account
3. POST /{{your_host}}/auth get access token ,access token expire at 30 min
4. GET /{{your_host}}/employee -> Read ,header need include Authorization
5. POST /{{your_host}}/employee -> Create ,header need include Authorization
6. PUT /{{your_host}}/employee -> Update ,header need include Authorization
7. DELETE /{{your_host}}/employee -> Delete ,header need include Authorization
8. API test file is test.http (need VsCode Package: 
                                REST Client
                                Id: humao.rest-client
                                Description: REST Client for Visual Studio Code
                                Version: 0.24.5
                                Publisher: Huachao Mao
                                VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

9. app folder is a blank folder ,my real app at flask_api folder
