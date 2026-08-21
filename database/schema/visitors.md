
---

### `database/schema/visitors.md`

```markdown
# Visitors Collection

Stores registered information about non-resident visitors.

## Document Structure

```json
{
  "_id": "ObjectId",
  "name": "string",
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