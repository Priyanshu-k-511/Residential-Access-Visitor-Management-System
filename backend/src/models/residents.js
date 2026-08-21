const mongoose = require("mongoose");

const residentSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      trim: true
    },
    flatNumber: {
      type: String,
      required: true,
      trim: true
    },
    governmentId: {
      type: {
        type: String,
        required: true,
        trim: true
      },
      lastFour: {
        type: String,
        required: true,
        trim: true,
        minlength: 4,
        maxlength: 4
      }
    },
    phone: {
      type: String,
      required: true,
      trim: true
    },
    vehicles: [
      {
        vehicleNumber: {
          type: String,
          required: true,
          trim: true
        },
        vehicleType: {
          type: String,
          enum: ["car", "motorcycle", "scooter", "other"],
          required: true
        }
      }
    ],
    status: {
      type: String,
      enum: ["active", "inactive"],
      default: "active"
    }
  },
  {
      timestamps: true
  }
);

module.exports = mongoose.model("Resident", residentSchema);