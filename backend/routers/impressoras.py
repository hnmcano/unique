from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.connection import get_db
from service.depencias import get_current_user
from models.estabelecimento import Estabelecimento as EstabelecimentoModel
from models.impressoras import Impressoras as ImpressoraModel
from schemas.impressoras import ImpressoraResponse
from schemas.impressoras import ImpressoraInput
from uuid import UUID

router = APIRouter()

@router.post("/default", status_code=status.HTTP_200_OK, response_model=ImpressoraResponse)
def definindo_impressora_padrao(data: ImpressoraInput,db: Session= Depends(get_db), user_current: dict = Depends(get_current_user)):
    estabelecimento = db.query(EstabelecimentoModel).filter(EstabelecimentoModel.id == user_current["estabelecimento_id"]).first()

    if not estabelecimento:
        raise HTTPException(status=404, detail="Estabelecimento não localizado na base!")

    data = ImpressoraModel(
        estabelecimento_id=estabelecimento.id,
        impressora=data.impressora,
        padrao=data.padrao
    )

    db.add(data)
    db.commit()
    db.flush()

    default = db.query(ImpressoraModel).filter(ImpressoraModel.estabelecimento_id == user_current["estabelecimento_id"], ImpressoraModel.padrao == True).first()

    default_serializado = ImpressoraResponse.modal_validate(default)

    return default_serializado

@router.get("/default/disponivel", response_model=ImpressoraResponse)
def extrair_impressora_padrao(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    default = db.query(ImpressoraModel).filter(ImpressoraModel.estabelecimento_id == user_current["estabelecimento_id"], ImpressoraModel.padrao == True).first()

    if not default:
        raise HTTPException(status=404, detail="Impressora padrão não definida, por favor defina em configuracoes!")

    default_serializado = ImpressoraResponse.model_validate(default)

    return default_serializado

@router.delete("/default/deletar/{impressora_id}", status_code=status.HTTP_200_OK)
def deletar_impressora(impressora_id: UUID, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    default = db.query(ImpressoraModel).filter(ImpressoraModel.estabelecimento_id == user_current["estabelecimento_id"], ImpressoraModel.impressora_id == impressora_id).first()

    if not default:
        raise HTTPExeception(status=404, detail="Impressora padrão não definida, por favor defina em configuracoes!")

    db.delete(default)
    db.commit()
    db.flush()
