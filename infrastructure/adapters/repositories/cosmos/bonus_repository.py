from core.ports.bonus_port import BonusPort
from core.domain.bonus import Bonus
from infrastructure.database.cosmos import CosmosDB
import uuid

class CosmosBonusRepository(BonusPort):
    def __init__(self):
        self.container = CosmosDB().get_container("Bonuses", partition_key_path="/servant_id")

    def get_all_bonuses(self):
         query = "SELECT c.id, c.servant_id, c.amount, c.paid_date FROM c ORDER BY c.paid_date DESC"
         return [Bonus(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]
    
    def add_bonus(self, bonus:Bonus):
        self.container.create_item(bonus.model_dump())