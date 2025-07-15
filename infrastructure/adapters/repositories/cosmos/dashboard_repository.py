from core.ports.bonus_port import BonusPort
import uuid

class CosmosDashboardRepository(BonusPort):
    def __init__(self,container):
        self.container = container