from dataclasses import dataclass, field
from xmlrpc.client import boolean

@dataclass
class MeteoriteFinding:
    name: str
    id: int
    nametype: str
    meteoriteclass: str
    mass: float = field(metadata={"units":"grams"})
    fall: str
    year: str
    latitude: float = field(metadata={"units":"decimal degrees"})
    longitude: float = field(metadata={"units":"decimal degrees"})

    def __gt__(self,other):
            return self.mass > other.mass
    def __eq__(self,other):
            return self.mass == other.mass
    def __ge__(self,other):
            return self.mass >= other.mass

    
import csv

# import from the CSV into a list of meteorite findings
findings = list()
with open("Meteorite_Landings.csv","r",newline='',encoding="utf-8-sig") as csvfile:
    meteorite_reader = csv.DictReader(csvfile)
    for row in meteorite_reader:
        finding = MeteoriteFinding(row['name'],row['id'],row['nametype'],row['recclass'],row['mass (g)'],row['fall'],row['year'],row['reclat'],row['reclong'])
        findings.append(finding)

print(findings[0] > findings[10])


@dataclass
class Orders:
    OrderID: int
    CustomerID: int
    SalesPersonID: int
    ContactPersonID: int
    BackorderOrderID: int
    OrderDate: "date"
    ExpectedDeliveryDate: "date"
    CustomerPurchaseOrderNumber: str
    IsUndersupplyBackOrder: bool
    Comments: str
    DeliveryInstructions: str
    InternalComments: str
    PickingCompleteWhen: "date"
    LastEditedBy: int
    LastEditedWhen: "date"

    def __gt__(self,other):
            return self.OrderID > other.OrderID
    def __eq__(self,other):
            return self.OrderID == other.OrderID
    def __ge__(self,other):
            return self.OrderID >= other.OrderID
