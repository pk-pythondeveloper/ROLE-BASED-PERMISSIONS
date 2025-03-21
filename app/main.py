from fastapi import FastAPI, Depends, HTTPException, status
from database import get_db
from api import permissions,roles,users,assigne_role_to_users,assigne_permission_to_roles,products,auth
from database import init_db
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates




# from models.models import roles,users
app = FastAPI()
#The @app.on_event("startup") decorator in FastAPI is used to define a function that runs when the application starts.
@app.on_event("startup")
def startup_event():
    init_db()
#user api
app.include_router(users.router, prefix="/users", tags=["users"])
#role api
app.include_router(roles.router, prefix="/roles", tags=["roles"])
#permission api
app.include_router(permissions.router, prefix="/permissions", tags=["permissions"])
# assine role to user api
app.include_router(assigne_role_to_users.router, prefix="/assigne_role_to_users", tags=["assigne_role_to_users"])
#assine permission to role api
app.include_router(assigne_permission_to_roles.router, prefix="/assigne_permission_to_roles", tags=["assigne_permission_to_roles"])
#assine product api
app.include_router(products.router, prefix="/products", tags=["products"])
#loigin api
app.include_router(auth.router, prefix="/auth", tags=["auth"])



#frontend api
templates = Jinja2Templates(directory="static/templates")
@app.get("/hello")
async def read_hello(request: Request, name: str = "ramamam"):
    return templates.TemplateResponse("index.html", {"request": request, "name": name})