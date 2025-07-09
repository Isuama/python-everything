from core.ports.utility_settlement_port import UtilitySettlementPort
from core.ports.servant_port import ServantPort
from core.ports.utility_port import UtilityPort
from core.domain.utilitySettlement import UtilitySettlement,UtilitySettlementDTO
import uuid

class UtilitySettlementService:
    def __init__(self, servant_repo:ServantPort , utility_repo:UtilityPort, utility_settlement_repo: UtilitySettlementPort):
        self.servant_repo = servant_repo
        self.utility_repo=utility_repo
        self.utility_settlement_repo = utility_settlement_repo

    def get_all_utility_settlements(self) -> list[UtilitySettlement]:
        # map servants
        servants = self.servant_repo.get_all_servants()
        servant_map = {s.id: s.name for s in servants}

        #map utilities
        utilities = self.utility_repo.get_all_utilities()
        utility_map = {u.id: u.name for u in utilities}

        utility_settlements_with_names = []
        utility_settlements = self.utility_settlement_repo.get_all_utility_settlements()
        for settlement in utility_settlements:
            servant_name = servant_map.get(settlement.servant_id, "Unknown Servant")
            utility_type_name = utility_map.get(settlement.utility_type_id,"Unknown Utility")

            settlement_with_name = UtilitySettlementDTO (
                id=settlement.id,
                servant_id=settlement.servant_id,
                utility_type_id = settlement.utility_type_id,
                servant_name=servant_name,
                utility_type=utility_type_name,
                amount=settlement.amount,
                paid_date=settlement.paid_date
            )
            utility_settlements_with_names.append(settlement_with_name)
        return utility_settlements_with_names
    
    def add_utility_settlement(self, servant_id,utility_type_id,amount,paid_date):
        utility_settlement = UtilitySettlement(
            id = str(uuid.uuid4()),
            servant_id = servant_id,
            utility_type_id = utility_type_id,
            amount = amount,
            paid_date = paid_date
        )
        self.utility_settlement_repo.add_utility_settlement(utility_settlement)