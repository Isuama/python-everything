from domain.ports.bonus_port import BonusPort
from domain.ports.servant_port import ServantPort
from domain.models.bonus import Bonus,BonusDTO
import uuid

class BonusService:
    def __init__(self, servant_repo:ServantPort , bonus_repo: BonusPort):
        self.servant_repo = servant_repo
        self.bopnus_repo = bonus_repo

    def get_all_bonuses(self) -> list[Bonus]:
        # map servants
        servants = self.servant_repo.get_all_servants()
        servant_map = {s.id: s.name for s in servants}

        bonuses_with_names = []
        paid_bonuses = self.bopnus_repo.get_all_bonuses()
        for bonus in paid_bonuses:
            servant_name = servant_map.get(bonus.servant_id, "Unknown Servant")

            bonus_with_name = BonusDTO(
                id=bonus.id,
                servant_id=bonus.servant_id,
                servant_name=servant_name,
                amount=bonus.amount,
                paid_date=bonus.paid_date
            )
            bonuses_with_names.append(bonus_with_name)
        return bonuses_with_names
    
    def add_bonus(self,servant_id,amount,paid_date):
        bonus = Bonus(
            id = str(uuid.uuid4()),
            servant_id = servant_id,
            amount = amount,
            paid_date = paid_date
        )
        self.bopnus_repo.add_bonus(bonus)