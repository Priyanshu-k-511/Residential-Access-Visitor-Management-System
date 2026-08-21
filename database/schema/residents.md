# Residents Collection

Stores registered residents of the residential society.

## Document Structure

```json
{
  "_id": "ObjectId",
  "name": "string",
  "flatNumber": "string",
  "governmentId": {
    "type": "string",
    "lastFour": "string"
  },
  "vehicle": {
    "numberPlate":"string"
  },
  "phone": "string",
  "status": "active | inactive",
  "createdAt": "Date",
  "updatedAt": "Date"
}