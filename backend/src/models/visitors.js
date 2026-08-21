const mongoose = require("mongoose");

const visitorSchema = new mongoose.Schema(
  {
    name: {
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
      trim: true
    },
    visitingFlat: {
      type: String,
      required: true,
      trim: true
    },
    vehicle: {
      vehicleNumber: {
        type: String,
        trim: true
      },
      vehicleType: {
        type: String,
        enum: ["car", "motorcycle", "scooter", "other"]
      }
    },
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

module.exports = mongoose.model("Visitor", visitorSchema);