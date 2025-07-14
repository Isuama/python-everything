from core.ports.wage_adjustment_port import WageAdjustmentPort
from core.ports.servant_port import ServantPort
from core.domain.wageAdustment import WageAdjustment,WageAdjustmentDTO
from typing import List
from datetime import datetime
import uuid
from infrastructure.utils.cast_utils import safe_float

class WageAdjustmentService:
    def __init__(self, servant_repository: ServantPort, wage_repository: WageAdjustmentPort):
        self.servant_repository=servant_repository
        self.wage_repository = wage_repository

    def get_all_wage_adjustments(self) -> List[WageAdjustmentDTO]:
        # map servants
        servants = self.servant_repository.get_all_servants()
        servant_map = {s.id: s.name for s in servants}

        wage_adjustments_with_names = []
        wage_adustments = self.wage_repository.get_all_wage_adjustments()
        for adjustment in wage_adustments:
            servant_name = servant_map.get(adjustment.servant_id, "Unknown Servant")
            wage_adjustments_with_name = WageAdjustmentDTO(
                id=adjustment.id,
                servant_id=adjustment.servant_id,
                servant_name=servant_name,
                amount=adjustment.amount,
                adjustment_date=adjustment.adjustment_date,
                remarks=adjustment.remarks
            )
            wage_adjustments_with_names.append(wage_adjustments_with_name)
        
        return wage_adjustments_with_names
    
    def get_wage_adjustments_by_id(self, adjustment_id:str) -> WageAdjustment:
        return self.wage_repository.get_wage_adjustments_by_id(adjustment_id)

    def add_wage_adjustments(self, data) -> None:
        adjustment = {
            "id": str(uuid.uuid4()),
            "servant_id": data["servant_id"],
            "amount": data.get("amount", ""),
            "adjustment_date": data.get("adjustment_date", ""),
            "remarks": data.get("remarks", "")
        }
        self.wage_repository.add_wage_adjustments(adjustment)

    def update_wage_adjustment(self, data: dict):
        updated_adjustment = WageAdjustment(
            id=data["id"],
            servant_id=data["servant_id"],
            amount=float(data["amount"]),
            adjustment_date=data["adjustment_date"],
            remarks=data.get("remarks", "")
        )
        self.wage_repository.update_wage_adjustments(updated_adjustment)

    def delete_wage_adjustments(self, servant_id:str, wage_adjustment_id: str) -> None:
        self.wage_repository.delete_wage_adjustments(servant_id,wage_adjustment_id)