from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from models.estabelecimento import Estabelecimento as EstabelecimentoModel

def get_estabelecimento(x_tenant_slug: str = Header(None), db: Session = Depends(get_db)):    
    if not x_tenant_slug:
        raise HTTPException(status_code=400, detail="x-tenant-slug header is required")
    
    estabelecimento = db.query(EstabelecimentoModel).filter(
        EstabelecimentoModel.subdominio == x_tenant_slug
    ).first()
        
    if not estabelecimento:
        raise HTTPException(status_code=404, detail="Estabelecimento not found")

    if not estabelecimento.ativo:
        raise HTTPException(status_code=400, detail="Estabelecimento is not active")

    return estabelecimento