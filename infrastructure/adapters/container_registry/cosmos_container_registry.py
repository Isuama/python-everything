# infrastructure/db/container_registry.py

from infrastructure.database.cosmos import CosmosDB
from azure.cosmos.container import ContainerProxy

class CosmosContainerRegistry:
    def __init__(self, db: CosmosDB):
        self._containers: dict[str, ContainerProxy] = {
            "attendance": db.get_container("Attendance", "/servant_id"),
            "bonuses": db.get_container("Bonuses", "/servant_id"),
            "loans": db.get_container("Loans", "/servant_id"),
            "loanSettlements": db.get_container("LoanSettlements", "/servant_id"),
            "salaries": db.get_container("Salaries", "/servant_id"),
            "servants": db.get_container("Servants", "/id"),            
            "utility": db.get_container("Utility", "/id"),
            "utilitySettlement": db.get_container("UtilitySettlement", "/servant_id"),
            "wages": db.get_container("Salaries", "/servant_id"),
            "wageAdjustments": db.get_container("WageAdjustments", "/servant_id"),
            "weeklyCarryForward": db.get_container("WeeklyCarryForward", "/servant_id"),
        }

    def get(self, name: str) -> ContainerProxy:
        if name not in self._containers:
            raise ValueError(f"Container '{name}' not registered.")
        return self._containers[name]
