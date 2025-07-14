from core.ports.attendance_port import AttendancePort
from core.domain.attendance import Attendance
from infrastructure.database.cosmos import CosmosDB

class CosmosAttendanceRepository(AttendancePort):
    def __init__(self):
        db = CosmosDB()
        self.container = db.get_container(container_name="Attendance", partition_key_path="/id")

    def get_attendance_records(self, start_date: str, end_date: str):
        query = f"""
            SELECT c.id, c.servant_id, c.date, c.present FROM c 
            WHERE c.date >= '{start_date}' AND c.date <= '{end_date}'
        """
        results = self.container.query_items(query=query, enable_cross_partition_query=True)
        return [Attendance(**item) for item in results]

    def create_attendance(self, attendance_item: dict):
        self.container.create_item(attendance_item)

    def delete_attendance(self, item_id: str, servant_id: str):
        self.container.delete_item(item=item_id, partition_key=servant_id)

    def get_attendance_dates_by_servant(self,servant_id, start_date, end_date):
        query = """
            SELECT c.date FROM c 
            WHERE c.servant_id = @sid AND c.present = true 
            AND c.date >= @start AND c.date < @end
            ORDER BY c.date
        """
        params = [
            {"name": "@sid", "value": servant_id},
            {"name": "@start", "value": start_date.strftime("%Y-%m-%d")},
            {"name": "@end", "value": end_date.strftime("%Y-%m-%d")},
        ]
        result = self.container.query_items(query=query, parameters=params, enable_cross_partition_query=True)
        return [record["date"] for record in result]