from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
import os
from core.config import settings


security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    
    token = credentials.credentials

    try:
        playload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        user_id = playload.get("sub")
        estabelecimento_id = playload.get("estabelecimento_id")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        
        return {
            "user_id": user_id,
            "estabelecimento_id": estabelecimento_id
        }
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
        