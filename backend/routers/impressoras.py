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
def definindo_impressora_padrao(data: ImpressoraInput, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    """
    Define uma impressora como padrão. 
    Remove a flag padrão de qualquer outra impressora do estabelecimento.
    """
    estabelecimento = db.query(EstabelecimentoModel).filter(
        EstabelecimentoModel.id == user_current["estabelecimento_id"]
    ).first()

    if not estabelecimento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estabelecimento não localizado na base!")

    # Desativa a impressora padrão anterior (se existir)
    impressora_anterior = db.query(ImpressoraModel).filter(
        ImpressoraModel.estabelecimento_id == user_current["estabelecimento_id"],
        ImpressoraModel.padrao == True
    ).first()

    if impressora_anterior:
        impressora_anterior.padrao = False

    # Cria a nova impressora como padrão
    nova_impressora = ImpressoraModel(
        estabelecimento_id=estabelecimento.id,
        impressora=data.impressora,
        padrao=True,  # Sempre True nesta rota
        tamanho=data.tamanho
    )

    db.add(nova_impressora)
    db.commit()
    db.refresh(nova_impressora)

    return ImpressoraResponse.model_validate(nova_impressora)


@router.get("/default/disponivel", response_model=ImpressoraResponse)
def extrair_impressora_padrao(db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    """
    Retorna a impressora padrão do estabelecimento.
    """
    default = db.query(ImpressoraModel).filter(
        ImpressoraModel.estabelecimento_id == user_current["estabelecimento_id"],
        ImpressoraModel.padrao == True
    ).first()

    if not default:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Impressora padrão não definida, por favor defina em configurações!"
        )

    return ImpressoraResponse.model_validate(default)


@router.delete("/default/deletar/{impressora_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_impressora(impressora_id: UUID, db: Session = Depends(get_db), user_current: dict = Depends(get_current_user)):
    """
    Deleta uma impressora do estabelecimento.
    """
    impressora = db.query(ImpressoraModel).filter(
        ImpressoraModel.estabelecimento_id == user_current["estabelecimento_id"],
        ImpressoraModel.impressora_id == impressora_id
    ).first()

    if not impressora:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Impressora não encontrada!"
        )

    db.delete(impressora)
    db.commit()