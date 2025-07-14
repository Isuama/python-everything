from core.ports.wage_port import WagePort
from core.domain.wage import Wage, WageWithServantName 
from core.ports.servant_port import ServantPort
from core.domain.servant import Servant
import uuid

class WageService:
    def __init__(self, servant_repo: ServantPort, wage_repo: WagePort):
        self.servant_repo = servant_repo
        self.wage_repo = wage_repo

    def get_all_wages_with_names(self) -> list[Wage]:
        wages = self.wage_repo.get_all()
        servants = self.servant_repo.get_all_active_servants()
        servant_map = {s.id: s.name for s in servants}
        wages_with_names = []
        for wage in wages:
            name = servant_map.get(wage.servant_id, "Unknown")
            # Build a new Wage model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         including name
            wage_with_name = WageWithServantName (
                id=wage.id,
                servant_id=wage.servant_id,
                name=name,
                amount=wage.amount,
                date=wage.date,
            )
            wages_with_names.append(wage_with_name)
        return wages_with_names
    
    def update_wage(self, servant_id: str, amount: float, date: str):
        # Check if a wage record exists for servant_id and date
        existing_wage = self.wage_repo.get_wage_by_servant_and_date(servant_id, date)
        print("ex",existing_wage)
        if existing_wage:
            # Update existing record
            existing_wage.amount = amount
            self.wage_repo.update(existing_wage)
        else:
            # Create new record
            new_wage = Wage(
                id=str(uuid.uuid4()),
                servant_id=servant_id,
                amount=amount,
                date=date
            )
            self.wage_repo.add(new_wage)